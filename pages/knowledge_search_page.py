import time
import delayed_assert
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import KnowledgeSearchLocators


class KnowledgeSearchPage(BasePage):
    # Вспомогательный метод собирает текст у всех найденных элементов в список
    def item_text_collector(self, how, what):
        web_elements = self.browser.find_elements(how, what)
        list_text_element = []
        for item in web_elements:
            list_text_element.append(item.text)
        return list_text_element

    def load_all_result(self):
        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()
            if self.browser.find_element(*KnowledgeSearchLocators.END_LOAD_BUTTON).is_displayed() is True:
                break

    def verify_default_fast_filter(self):
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')
        delayed_assert.expect("Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"')
        delayed_assert.expect("Холдинги" in list_filter, 'Отсутствует блок фильтра "Холдинги"')
        delayed_assert.expect("Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"')
        delayed_assert.expect("Подразделение-исполнитель" in list_filter,
                              'Отсутствует блок фильтра "Подразделение-исполнитель"')
        delayed_assert.expect("Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"')
        delayed_assert.expect("Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"')

    def verify_fast_filter_project(self):
        self.browser.implicitly_wait(1)
        # Активируем чек-бокс "Проект"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Проект")
        project_checkbox = self.browser.find_element(how, what)
        project_checkbox.click()

        # Проверяем активацию чек-бокса
        assert project_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Проект" не активирован'
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Проект"
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')
        # delayed_assert.expect("Год" in list_filter, 'Отсутствует блок фильтра "Год"')
        # delayed_assert.expect("Наполнение для маркетинга" in list_filter, 'Отсутствует блок фильтра "Наполнение для маркетинга"')
        # delayed_assert.expect("Интерес маркетинга к проекту" in list_filter, 'Отсутствует блок фильтра "Интерес маркетинга к проекту"')
        # delayed_assert.expect("Холдинги" in list_filter, 'Отсутствует блок фильтра "Холдинги"')
        delayed_assert.expect("Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"')
        delayed_assert.expect("Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"')
        delayed_assert.expect("Подразделение-исполнитель" in list_filter,
                              'Отсутствует блок фильтра "Подразделение-исполнитель"')
        delayed_assert.expect("Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"')
        delayed_assert.expect("Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"')

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем фильтрацию по чек-боксу "Проект"
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_OF_ALL_FOUND_ELEMENT)
        delayed_assert.expect("ПРОЕКТ" in (set(list_found_element)),
                              f'Отображены сущности {set(list_found_element)}\nОжидаемый результат: отображены сущности типа "Проект"')
        delayed_assert.expect(len(set(list_found_element)) == 1, "Отображены сущности не только категории Проект")

        # Деактивируем чек-бокс фильтрации по сущности "Проект"
        project_checkbox.click()
        assert project_checkbox.get_attribute("aria-checked") == "false", 'Чек-бокс "Проект" не деактивирован'

    def verify_fast_filter_contract(self):
        # Активируем чек-бокс "Договор(контракт)"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Договор (контракт)")
        contract_checkbox = self.browser.find_element(how, what)
        contract_checkbox.click()

        # Проверяем активацию чек-бокса
        assert contract_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Договор(контракт)" не активирован'
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Договор/контракт"
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')
        delayed_assert.expect("Стоимость проекта (руб.)" in list_filter,
                              'Отсутствует блок фильтра "Стоимость проекта (руб.)"')
        delayed_assert.expect("Дата заключения" in list_filter, 'Отсутствует блок фильтра "Дата заключения"')
        delayed_assert.expect("Дата завершения" in list_filter, 'Отсутствует блок фильтра "Дата завершения"')
        delayed_assert.expect("Статус контракта" in list_filter, 'Отсутствует блок фильтра "Статус контракта"')
        delayed_assert.expect("Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"')
        # delayed_assert.expect("Холдинги" in list_filter, 'Отсутствует блок фильтра "Холдинги"')
        delayed_assert.expect("Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"')
        delayed_assert.expect("Подразделение-исполнитель" in list_filter,
                              'Отсутствует блок фильтра "Подразделение-исполнитель"')
        delayed_assert.expect("Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"')
        delayed_assert.expect("Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"')

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем фильтрацию по чек-боксу "Договоры (контракты)"
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_OF_ALL_FOUND_ELEMENT)
        delayed_assert.expect("ДОГОВОР/КОНТРАКТ" in (set(list_found_element)),
                              f'Отображены сущности {set(list_found_element)} \nОжидаемый результат: "Договор/Контракт"')
        delayed_assert.expect(len(set(list_found_element)) == 1,
                              "Отображены сущности не только категории Договор/Контракт")

        # Деактивируем чек-бокс фильтрации по сущности "Договор/контракт"
        contract_checkbox.click()
        # Проверяем деактивацию чек-бокса
        assert contract_checkbox.get_attribute(
            "aria-checked") == "false", 'Чек-бокс "Договор(контракт)" не деактивирован'

    def verify_fast_filter_division(self):
        # Активируем чек-бокс "Подразделение"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Подразделение")
        division_checkbox = self.browser.find_element(how, what)
        division_checkbox.click()

        # Проверяем активацию чек-бокса "Подразделение"
        assert division_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Подразделение" не активирован'
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Подразделение"
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect(len(list_filter) == 5, 'Отображены лишние категории фильтров для блока "Подразделение"')
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')
        delayed_assert.expect("Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"')
        delayed_assert.expect("Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"')
        delayed_assert.expect("Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"')
        delayed_assert.expect("Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"')

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем фильтрацию по чек-боксу "Подразделение"
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_OF_ALL_FOUND_ELEMENT)
        delayed_assert.expect("ПОДРАЗДЕЛЕНИЕ" in (set(list_found_element)),
                              f'Отображены сущности {set(list_found_element)}\nОжидаемый результат: "Подразделение"')
        delayed_assert.expect(len(set(list_found_element)) == 1,
                              "Отображены сущности не только категории Подразделение")

        # Деактивируем чек-бокс фильтрации по сущности "Подразделение"
        division_checkbox.click()
        # Проверяем деактивацию чек-бокса "Подразделение"
        assert division_checkbox.get_attribute("aria-checked") == "false", 'Чек-бокс "Подразделение" не деактивирован'

    def verify_fast_filter_technology(self):
        # Активируем чек-бокс "Технологию"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Технологию")
        technology_checkbox = self.browser.find_element(how, what)
        technology_checkbox.click()

        # Проверяем активацию чек-бокса "Технологию"
        assert technology_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Технологию" не активирован'
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Подразделение"
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect(len(list_filter) == 1, 'Отображены лишние категории фильтров для блока "Технологии"')
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')

        # Подгружаем весь список найденных сущностей
        self.load_all_result()
        """
        # Проверяем фильтрацию по чек-боксу "Технология"
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_ON_ALL_FOUND_ELEMENT)
        assert "ТЕХНОЛОГИЯ" in (set(list_found_element)), f'Отображены сущности {set(list_found_element)} ' \
                                                             f'\nОжидаемый результат: "Подразделение"'
        assert len(set(list_found_element)) == 1, "Отображены сущности не только категории Подразделение"
        """

        # Деактивируем чек-бокс фильтрации по сущности "Технология"
        technology_checkbox.click()

        # Проверяем деактивацию чек-бокса
        assert technology_checkbox.get_attribute("aria-checked") == "false", 'Чек-бокс "Технологию" не деактивирован'

    def verify_fast_filter_legal(self):
        # Активируем чек-бокс "Юр.лицо/ИП"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Юр.лицо/ИП")
        legal_checkbox = self.browser.find_element(how, what)
        legal_checkbox.click()

        # Проверяем активацию чек-бокса "Юр.лицо/ИП"
        assert legal_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Юр.лицо/ИП" не активирован'
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Юр.лицо/ИП"
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect(len(list_filter) == 1, 'Отображены лишние категории фильтров для блока "Технологии"')
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем фильтрацию по чек-боксу "Юр.лицо/ИП"
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_OF_ALL_FOUND_ELEMENT)
        delayed_assert.expect("ЮР.ЛИЦО/ИП" in (set(list_found_element)),
                              f'Отображены сущности {set(list_found_element)}\nОжидаемый результат: "Юр.лицо/ИП"')
        delayed_assert.expect(len(set(list_found_element)) == 1, "Отображены сущности не только категории Юр.лицо/ИП")

        # Деактивируем чек-бокс фильтрации по сущности "Юр.лицо/ИП"
        legal_checkbox.click()

        # Проверяем деактивацию чек-бокса
        assert legal_checkbox.get_attribute("aria-checked") == "false", 'Чек-бокс "Юр.лицо/ИП" не деактивирован'

    def search_line(self, data_dict):
        split_name = data_dict["fullName"].split(",")
        if len(split_name) > 1:
            # Вводим первую часть названия
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(split_name[0])
            time.sleep(3)
            # Проверяем названия найденных сущностей по первой части с служебными символами []
            list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
            if len(list_name_found) > 0:

                assert list_name_found.count(data_dict["fullName"]) == 1, \
                    f'Не найдено сущности "{data_dict["fullName"]}" по поиску значения {split_name[0]}'
            else:
                print("Не найдено ни одного результата удовлетворяющего запросу")

            # Очищаем строку поиска
            self.browser.find_element(*KnowledgeSearchLocators.CLEAR_LINE_BUTTON).click()

            # Вводим вторую часть названия
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(split_name[1])
            time.sleep(3)
            # Проверяем названия найденных сущностей по второй части названия
            list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
            if len(list_name_found) > 0:
                if list_name_found.count(data_dict["fullName"]) == 0:
                    assert list_name_found.count(data_dict["fullName"]) == 1, \
                        f'Не найдено сущности "{data_dict["fullName"]}" по поиску значения {split_name[1]}'
            else:
                print("Не найдено результатов удовлетворяющих запросу")

            # Очищаем строку поиска
            self.browser.find_element(*KnowledgeSearchLocators.CLEAR_LINE_BUTTON).click()

        # Вводим полное название
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(data_dict["fullName"])
        time.sleep(3)
        # Проверяем названия найденных сущностей по целому названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        if len(list_name_found) > 0:
            if list_name_found.count(data_dict["fullName"]) == 0:
                assert list_name_found.count(data_dict["fullName"]) == 1, \
                    f'Не найдено сущности "{data_dict["fullName"]}" по поиску значения {data_dict["fullName"]}'
        else:
            print("Не найдено результатов удовлетворяющих запросу")

        # Сбрасываем все настройки нажатием кнопки "Сбросить"
        self.browser.find_element(*KnowledgeSearchLocators.CLEAR_LINE_BUTTON).click()

    def search_with_customer_block_filter(self, data_dict):
        # Активируем чек-бокс "Проект"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Проект")
        project_checkbox = self.browser.find_element(how, what)
        project_checkbox.click()

        # Проверяем активацию чек-бокса "Проект" в блоке "Нужно найти"
        assert project_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Проект" не активирован'
        time.sleep(1)

        # Жмем кнопку "Весь список" в блоке "Заказчик"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Свернуть")

        for element in data_dict["customers"]:
            # Вводим в строку поиска первое значение "Заказчик"
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
                element)
            # Активируем найденный чек-бокс
            how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
            what = what.replace("name", element)
            customer_checkbox = self.browser.find_element(how, what)
            customer_checkbox.click()

            # Проверяем активацию чек-бокса в блоке "Заказчик"
            assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
                f'Чек-бокс {element} в блоке "Заказчик" не активирован'

            # Проверяем результаты фильтрации по полю "Заказчик"
            list_customer_found = self.item_text_collector(*KnowledgeSearchLocators.CUSTOMER_VALUE_IN_RESULT)
            for str_customer in list_customer_found:
                assert element in str_customer, \
                    f'После фильтрации по полю "Заказчик" не отображено ожидаемого результата\n ' \
                    f'Ожидаемый результат: {element}\n ' \
                    f'Фактические результаты: {set(list_customer_found)}'

            # Проверяем результаты фильтраци по названию сущности
            list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
            assert data_dict["fullName"] in list_name_found, \
                f'После фильтрации по полю "Заказчик" не отображено ожидаемого результата\n ' \
                f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
                f'Фактические результаты: {list_name_found}'

        # Деактивируем чек-боксы
        for element in data_dict["customers"]:
            # Вводим в строку поиска первое значение "Заказчик"
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(element)

            # Деактивируем чек-бокс в блоке "Заказчик"
            how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
            what = what.replace("name", element)
            self.browser.find_element(how, what).click()
            # Проверяем деактивацию чек-бокса в блоке "Заказчик"
            assert self.browser.find_element(how, what).get_attribute("aria-checked") == "false", \
                f'Чек-бокс {element} в блоке "Заказчик" не деактивирован'

        # Закрываем "Весь список" в блоке "Заказчики"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Весь список")

    def search_with_legal_block_filter(self, data_dict):
        # Активируем чек-бокс "Проект"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Проект")
        project_checkbox = self.browser.find_element(how, what)
        project_checkbox.click()

        # Проверяем активацию чек-бокса "Проект" в блоке "Нужно найти"
        assert project_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Проект" не активирован'
        time.sleep(1)

        # Жмем кнопку "Весь список" у блока "Юр.лицо-исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Свернуть")

        # В строку поиска блока "Юр.лицо-исполнитель" вводим значение
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
            data_dict["executiveUnitLegal"])

        # Активируем найденный чек-бокс в блоке "Юр.лицо-исполнитель"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", data_dict["executiveUnitLegal"])
        self.browser.find_element(how, what).click()

        # Проверяем активацию чек-бокса в блоке "Юр.лицо-исполнитель"
        assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
            f'Чек-бокс {data_dict["executiveUnitLegal"]} в блоке "Юр.лицо-исполнитель" не активирован'

        """
        Поле "Юр.лицо-исполнитель" не отображено в карточке "Проект"
        # Проверяем найденные значения по блоку "Юр.лицо-исполнитель"
        list_legal_found = self.item_text_collector(*KnowledgeSearchLocators.LEGAL_VALUE_IN_RESULT)
        assert data_dict["executiveUnitLegal"] in set(list_legal_found), \
            f'После фильтрации по полю "Юр.лицо-исполнитель" не отображено значения "Юр.лицо-исполнитель" в найденных результатах\n ' \
            f'Ожидаемый результат: {data_dict["executiveUnitLegal"]}\n ' \
            f'Фактические результаты: {list_legal_found}'
        """

        # Проверяем результаты фильтраци по названию сущности
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert data_dict["fullName"] in list_name_found, \
            f'После фильтрации по полю "Заказчик" не отображено ожидаемого результата\n ' \
            f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
            f'Фактические результаты: {list_name_found}'

        # Вводим повторно значение в строку поиска
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
            data_dict["executiveUnitLegal"])

        # Деактивируем чек-бокс в блоке "Юр.лицо-исполнитель"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", data_dict["executiveUnitLegal"])
        self.browser.find_element(how, what).click()

        # Проверяем деактивацию чек-бокса  в блоке "Юр.лицо-исполнитель"
        assert self.browser.find_element(how, what).get_attribute("aria-checked") == "false", \
            f'Чек-бокс {data_dict["executiveUnitLegal"]} в блоке "Юр.лицо-исполнитель" не деактивирован'

        # Закрываем "Весь список" в блоке "Юр.лицо - исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK, "Весь список")

    def search_with_performer_block_filter(self, data_dict):
        # Активируем чек-бокс "Проект"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Проект")
        project_checkbox = self.browser.find_element(how, what)
        project_checkbox.click()

        # Проверяем активацию чек-бокса "Проект" в блоке "Нужно найти"
        assert project_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Проект" не активирован'
        time.sleep(1)

        # Жмем кнопку "Весь список" у блока "Подразделение-исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK, "Свернуть")

        # В строку поиска блока "Подразделение-исполнитель" вводим значение
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
            data_dict["executiveUnit"])

        # Активируем найденный чек-бокс в блоке "Подразделение-исполнитель"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", data_dict["executiveUnit"])
        self.browser.find_element(how, what).click()

        # Проверяем активацию чек-бокса в блоке "Подразделение-исполнитель"
        assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
            f'Чек-бокс {data_dict["executiveUnit"]} в блоке "Подразделение-исполнитель" не активирован'

        # Проверяем найденные значения по блоку "Подразделение-исполнитель"
        list_executive_found = self.item_text_collector(*KnowledgeSearchLocators.PERFORMER_VALUE_IN_RESULT)
        assert data_dict["executiveUnit"] in set(list_executive_found), \
            f'После фильтрации по полю "Подразделение-исполнитель" не отображено значения "Юр.лицо-исполнитель" в найденных результатах\n ' \
            f'Ожидаемый результат: {data_dict["executiveUnit"]}\n ' \
            f'Фактические результаты: {set(list_executive_found)}'

        # Проверяем результаты фильтраци по названию сущности
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert data_dict["fullName"] in list_name_found, \
            f'После фильтрации по полю "Заказчик" не отображено ожидаемого результата\n ' \
            f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
            f'Фактические результаты: {set(list_name_found)}'

        # Вводим повторно значение в строку поиска
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
            data_dict["executiveUnit"])

        # Деактивируем чек-бокс в блоке "Юр.лицо-исполнитель"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", data_dict["executiveUnit"])
        self.browser.find_element(how, what).click()

        # Закрываем "Весь список" в блоке "Подразделение-исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK, "Весь список")

    def search_with_type_works_block_filter(self, data_dict):
        # Активируем чек-бокс "Проект"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Проект")
        project_checkbox = self.browser.find_element(how, what)
        project_checkbox.click()

        # Проверяем активацию чек-бокса "Проект" в блоке "Нужно найти"
        assert project_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Проект" не активирован'
        time.sleep(1)

        # Жмем кнопку "Весь список" у блока "Тип работ и услуг"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK, "Свернуть")

        for element in data_dict["typeOfWorkServices"]:
            # Вводим в строку поиска первое значение "Тип работ и услуг"
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
                element)
            # Активируем найденный чек-бокс
            how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
            what = what.replace("name", element)
            customer_checkbox = self.browser.find_element(how, what)
            customer_checkbox.click()

            # Проверяем активацию чек-бокса в блоке "Тип работ и услуг"
            assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
                f'Чек-бокс {element} в блоке "Тип работ и услуг" не активирован'

            """
            # Не отображено поле "Тип работ и услуг" в карточке "Проект"
            # Проверяем результаты фильтрации по полю "Тип работ и услуг"
            list_type_works_found = self.item_text_collector(*KnowledgeSearchLocators.TYPE_WORKS_VALUE_IN_RESULT)

            # Преобразовываем в строку с разделителем если значений больше одного
            str_element = str_element + element + ";"
            assert str_element[0:(len(str_element)-1)] in list_type_works_found, \
                f'После фильтрации по полю "Тип работ и услуг" не отображено ожидаемого результата\n ' \
                f'Ожидаемый результат: {str_element}\n ' \
                f'Фактические результаты: {set(list_type_works_found)}'
            """

            # Проверяем результаты фильтраци по названию сущности
            list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
            assert data_dict["fullName"] in list_name_found, \
                f'После фильтрации по полю "Тип работ и услуг" не отображено ожидаемого результата\n ' \
                f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
                f'Фактические результаты: {list_name_found}'

        # Деактивируем чек-боксы
        for element in data_dict["typeOfWorkServices"]:
            # Вводим в строку поиска первое значение "Тип работ и услуг"
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(element)

            # Деактивируем чек-бокс в блоке "Тип работ и услуг"
            how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
            what = what.replace("name", element)
            self.browser.find_element(how, what).click()

            # Проверяем деактивацию чек-бокса в блоке "Тип работ и услуг"
            assert self.browser.find_element(how, what).get_attribute("aria-checked") == "false", \
                f'Чек-бокс {element} в блоке "Тип работ и услуг" не деактивирован'

        # Закрываем "Весь список" в блоке "Тип работ и услуг"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK, "Весь список")

    def search_with_technologies_block_filter(self, data_dict):
        # Активируем чек-бокс "Проект"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Проект")
        project_checkbox = self.browser.find_element(how, what)
        project_checkbox.click()

        # Проверяем активацию чек-бокса "Проект" в блоке "Нужно найти"
        assert project_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Проект" не активирован'
        time.sleep(1)

        # Жмем кнопку "Весь список" у блока "Технологии"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK, "Свернуть")

        for element in data_dict["technologies"]:
            # Вводим в строку поиска первое значение "Технологии"
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
                element)

            # Активируем найденный чек-бокс
            how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
            what = what.replace("name", element)
            technology_checkbox = self.browser.find_element(how, what)
            technology_checkbox.click()

            # Проверяем активацию чек-бокса в блоке "Технологии"
            assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
                f'Чек-бокс {element} в блоке "Технологии" не активирован'

            # Проверяем результаты фильтрации по полю "Технологии"
            list_technologies_found = self.item_text_collector(*KnowledgeSearchLocators.TECHNOLOGIES_VALUE_IN_RESULT)
            for str_technologies in list_technologies_found:
                assert element in str_technologies, \
                    f'После фильтрации по полю "Технологии" не отображено ожидаемого результата\n ' \
                    f'Ожидаемый результат: {element}\n ' \
                    f'Фактические результаты: {str_technologies}'

            # Проверяем результаты фильтраци по названию сущности
            list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
            assert data_dict["fullName"] in list_name_found, \
                f'После фильтрации по полю "Технологии" не отображено ожидаемого результата\n ' \
                f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
                f'Фактические результаты: {list_name_found}'

        # Деактивируем чек-боксы
        for element in data_dict["technologies"]:
            # Вводим в строку поиска первое значение "Технологии"
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(element)

            # Деактивируем чек-бокс в блоке "Технологии"
            how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
            what = what.replace("name", element)
            self.browser.find_element(how, what).click()

            # Проверяем деактивацию чек-бокса в блоке "Технологии"
            assert self.browser.find_element(how, what).get_attribute("aria-checked") == "false", \
                f'Чек-бокс {element} в блоке "Технологии" не деактивирован'

        # Закрываем "Весь список" в блоке "Технологии"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK, "Весь список")

    def search_with_all_fast_filter_on_project(self, data_dict):

        # Активируем чек-бокс "Проект"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Проект")
        project_checkbox = self.browser.find_element(how, what)
        project_checkbox.click()

        # Проверяем активацию чек-бокса "Проект" в блоке "Нужно найти"
        assert project_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Проект" не активирован'
        time.sleep(1)

        # Жмем кнопку "Весь список" в блоке "Заказчик"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Свернуть")

        # Активируем чек-боксы в категории "Заказчик"
        for element in data_dict["customers"]:
            # Вводим в строку поиска первое значение "Заказчик"
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
                element)
            # Активируем найденный чек-бокс
            how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
            what = what.replace("name", element)
            customer_checkbox = self.browser.find_element(how, what)
            customer_checkbox.click()

            # Проверяем активацию чек-бокса в блоке "Заказчик"
            assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
                f'Чек-бокс {element} в блоке "Заказчик" не активирован'

            # Проверяем результаты фильтраци по названию сущности
            list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
            assert data_dict["fullName"] in list_name_found, \
                f'После фильтрации по полю "Заказчик" не отображено ожидаемого результата\n ' \
                f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
                f'Фактические результаты: {list_name_found}'

        # Закрываем "Весь список" в блоке "Заказчики"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Весь список")

        # Жмем кнопку "Весь список" у блока "Юр.лицо-исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Свернуть")

        # В строку поиска блока "Юр.лицо-исполнитель" вводим значение
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
            data_dict["executiveUnitLegal"])

        # Активируем найденный чек-бокс в блоке "Юр.лицо-исполнитель"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", data_dict["executiveUnitLegal"])
        self.browser.find_element(how, what).click()

        # Проверяем активацию чек-бокса в блоке "Юр.лицо-исполнитель"
        assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
            f'Чек-бокс {data_dict["executiveUnitLegal"]} в блоке "Юр.лицо-исполнитель" не активирован'

        # Проверяем результаты фильтраци по названию сущности
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert data_dict["fullName"] in list_name_found, \
            f'После фильтрации по полю "Заказчик" не отображено ожидаемого результата\n ' \
            f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
            f'Фактические результаты: {list_name_found}'

        # Закрываем "Весь список" в блоке "Юр.лицо - исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK, "Весь список")

        # Жмем кнопку "Весь список" у блока "Подразделение-исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK, "Свернуть")

        # В строку поиска блока "Подразделение-исполнитель" вводим значение
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
            data_dict["executiveUnit"])

        # Активируем найденный чек-бокс в блоке "Подразделение-исполнитель"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", data_dict["executiveUnit"])
        self.browser.find_element(how, what).click()

        # Проверяем активацию чек-бокса в блоке "Подразделение-исполнитель"
        assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
            f'Чек-бокс {data_dict["executiveUnit"]} в блоке "Подразделение-исполнитель" не активирован'

        # Проверяем результаты фильтраци по названию сущности
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert data_dict["fullName"] in list_name_found, \
            f'После фильтрации по полю "Заказчик" не отображено ожидаемого результата\n ' \
            f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
            f'Фактические результаты: {set(list_name_found)}'

        # Закрываем "Весь список" в блоке "Подразделение-исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK, "Весь список")

        # Жмем кнопку "Весь список" у блока "Тип работ и услуг"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK, "Свернуть")

        for element in data_dict["typeOfWorkServices"]:
            # Вводим в строку поиска первое значение "Тип работ и услуг"
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
                element)
            # Активируем найденный чек-бокс
            how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
            what = what.replace("name", element)
            customer_checkbox = self.browser.find_element(how, what)
            customer_checkbox.click()

            # Проверяем активацию чек-бокса в блоке "Тип работ и услуг"
            assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
                f'Чек-бокс {element} в блоке "Тип работ и услуг" не активирован'

            # Проверяем результаты фильтраци по названию сущности
            list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
            assert data_dict["fullName"] in list_name_found, \
                f'После фильтрации по полю "Тип работ и услуг" не отображено ожидаемого результата\n ' \
                f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
                f'Фактические результаты: {list_name_found}'

        # Закрываем "Весь список" в блоке "Тип работ и услуг"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK, "Весь список")

        # Жмем кнопку "Весь список" у блока "Технологии"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK, "Свернуть")

        for element in data_dict["technologies"]:
            # Вводим в строку поиска первое значение "Технологии"
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(element)

            # Активируем найденный чек-бокс
            how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
            what = what.replace("name", element)
            technology_checkbox = self.browser.find_element(how, what)
            technology_checkbox.click()

            # Проверяем активацию чек-бокса в блоке "Технологии"
            assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
                f'Чек-бокс {element} в блоке "Технологии" не активирован'

            # Проверяем результаты фильтраци по названию сущности
            list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
            assert data_dict["fullName"] in list_name_found, \
                f'После фильтрации по полю "Технологии" не отображено ожидаемого результата\n ' \
                f'Ожидаемый результат: {data_dict["fullName"]}\n ' \
                f'Фактические результаты: {list_name_found}'

        # Закрываем "Весь список" в блоке "Технологии"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK, "Весь список")

        # Жмем кнопку "Сбросить"
        self.browser.find_element(*KnowledgeSearchLocators.RESET_BUTTON).click()

    def search_with_sum_block_filter(self, data_dict):
        self.browser.implicitly_wait(1)
        # Активируем чек-бокс "Договор(контракт)"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Договор (контракт)")
        contract_checkbox = self.browser.find_element(how, what)
        contract_checkbox.click()

        # Проверяем активацию чек-бокса
        assert contract_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Договор(контракт)" не активирован'
        time.sleep(1)

        # Заполняем поле "Стоимость проекта (руб.) ОТ"
        sum_from = data_dict["sumInRub"]
        self.browser.find_element(*KnowledgeSearchLocators.SUM_FROM).send_keys(sum_from)
        time.sleep(2)

        # Подгружаем весь список найденных результатов
        self.load_all_result()

        # Проверяем найденные сущности на соответствие фильтрации по полю "Сумма контракта ОТ"
        list_sum_from_found = self.item_text_collector(*KnowledgeSearchLocators.SUM_VALUE_IN_RESULT)
        assert len(list_sum_from_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле "Сумма контракта ОТ" ({sum_from})'
        for element in list_sum_from_found:
            if element.find(".") > 0:
                element = float(element.replace(" ", ""))
            else:
                element = int(element.replace(" ", ""))
            assert sum_from <= element, \
                f'Условие: Показать сущности где сумма больше или равна {sum_from}, отображена сущность со значением {element}'

        # Очищаем поле "Сумма контракта ОТ"
        self.browser.find_element(*KnowledgeSearchLocators.SUM_FROM).clear()

        # Заполняем поле "Стоимость проекта (руб.) ДО"
        sum_to = data_dict["sumInRub"]
        self.browser.find_element(*KnowledgeSearchLocators.SUM_TO).send_keys(sum_to)
        time.sleep(2)

        # Подгружаем весь список найденных результатов
        self.load_all_result()

        # Проверяем найденные сущности на соответствие фильтрации по полю "Сумма контракта ДО"
        list_sum_to_found = self.item_text_collector(*KnowledgeSearchLocators.SUM_VALUE_IN_RESULT)
        assert len(list_sum_to_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле "Сумма контракта ДО" ({sum_from})'
        for element in list_sum_to_found:
            if element.find(".") > 0:
                element = float(element.replace(" ", ""))
            else:
                element = int(element.replace(" ", ""))
            assert sum_to >= element, \
                f'Условие: Показать сущности где сумма меньше или равна {sum_to}, ' \
                f'отображена сущность со значением {element}'

        # Заполняем поле "Стоимость проекта (руб.) ОТ"
        self.browser.find_element(*KnowledgeSearchLocators.SUM_FROM).send_keys(data_dict["sumInRub"])
        time.sleep(2)

        # Подгружаем весь список найденных результатов
        self.load_all_result()

        # Проверяем найденные сущности на соответствие фильтрации по полю "Сумма контракта ОТ" и "Сумма контракта ДО"
        list_sum_from_to_found = self.item_text_collector(*KnowledgeSearchLocators.SUM_VALUE_IN_RESULT)
        assert len(list_sum_from_to_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле "Сумма контракта ОТ" ({sum_from}) ' \
            f'и вводу значения в поле "Сумма контракта ДО" ({sum_to})'
        for element in list_sum_from_found:
            if element.find(".") > 0:
                element = float(element.replace(" ", ""))
            else:
                element = int(element.replace(" ", ""))
            assert sum_from <= element <= sum_to, \
                f'Условие: Показать сущности где сумма больше или равна {sum_from} и ' \
                f'сумма меньше или равна {sum_to}, отображена сущность со значением {element}'
        breakpoint()

