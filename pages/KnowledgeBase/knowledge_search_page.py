import time
import delayed_assert
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.locators import KnowledgeSearchLocators


class KnowledgeSearchPage(BasePage):

    # Вспомогательный метод: Прогрузка всех найденных результатов.
    def load_all_result(self):
        self.browser.implicitly_wait(1)
        if self.is_visibility_of_element_located(*KnowledgeSearchLocators.NOT_FOUND_RESULT, 2) is False:
            # Подгружаем весь список найденных сущностей
            while self.is_visibility_of_element_located(*KnowledgeSearchLocators.END_LOAD_BUTTON, 2) is False:
                self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()
                if self.browser.find_element(*KnowledgeSearchLocators.END_LOAD_BUTTON).is_displayed() is True:
                    break

    # Вспомогательный метод: Проверяет наличие искомого названия сущности в результатах поиска.
    def checking_the_found_name(self, name, field):
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f'Не найдено ни одной сущности при фильтрации: {field}'
        assert name in list_name_found, \
            f'После фильтрации по полю: {field} не отображено искомой сущности\n ' \
            f'Ожидаемый результат: {name}\n ' \
            f'Фактические результаты: {set(list_name_found)}'

    # Вспомогательный метод: Удаление пробелов из значений списка.
    def delete_spaces(self, raw_list):
        new_list = []
        for element in raw_list:
            new_element = element.replace[" ", ""]
            new_list = new_list.append(new_element)
        return new_list

    def activate_checkbox_need_to_find(self, name):
        # Активируем чек-бокс в блоке "Нужно найти"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", name)
        checkbox = self.browser.find_element(how, what)
        checkbox.click()

        # Проверяем активацию чек-бокса в блоке "Нужно найти"
        assert checkbox.get_attribute("aria-checked") == "true", \
            f'Чек-бокс "{name}" в блоке "Нужно найти" не активирован'
        time.sleep(1)

    def deactivate_checkbox_need_to_find(self, name):
        # деактивируем чек-бокс в блоке "Нужно найти"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", name)
        checkbox = self.browser.find_element(how, what)
        checkbox.click()

        # Проверяем деактивацию чек-бокса в блоке "Нужно найти"
        assert checkbox.get_attribute("aria-checked") == "false", \
            f'Чек-бокс "{name}" в блоке "Нужно найти" не ДЕактивирован'
        time.sleep(1)

    def reset_button_knowledge(self):
        # Жмем кнопку "Сбросить"
        self.browser.find_element(*KnowledgeSearchLocators.RESET_BUTTON).click()

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
        # Проверяем отображаемые категории быстрых фильтров для сущности "Проект".
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

        # Подгружаем весь список найденных сущностей.
        self.load_all_result()

        # Проверяем фильтрацию по чек-боксу "Проект".
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_OF_ALL_FOUND_ELEMENT)
        delayed_assert.expect("ПРОЕКТ" in (set(list_found_element)),
                              f'Отображены сущности {set(list_found_element)}\nОжидаемый результат: отображены сущности типа "Проект"')
        delayed_assert.expect(len(set(list_found_element)) == 1, "Отображены сущности не только категории Проект")

    def verify_fast_filter_contract(self):
        # Проверяем отображаемые категории быстрых фильтров для сущности "Договор/контракт".
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

    def verify_fast_filter_division(self):
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

    def verify_fast_filter_technology(self):
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

    def verify_fast_filter_legal(self):
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

    def search_line_by_name(self, name):
        # Проверяем наличие разделителя: ","
        if name.find(",") >= 0:
            split_name = name.split(",")
            # Вводим первую часть названия
            self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(split_name[0])
            time.sleep(3)
            # Проверяем названия найденных сущностей по первой части с служебными символами []
            list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
            if len(list_name_found) > 0:

                assert list_name_found.count(name) == 1, \
                    f'Не найдено сущности "{name}" по поиску значения {split_name[0]}'
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
                if list_name_found.count(name) == 0:
                    assert list_name_found.count(name) == 1, \
                        f'Не найдено сущности "{name}" по поиску значения {split_name[1]}'
            else:
                print("Не найдено результатов удовлетворяющих запросу")
            # Очищаем строку поиска
            self.browser.find_element(*KnowledgeSearchLocators.CLEAR_LINE_BUTTON).click()

        # Удаляем спецсимволы из переменной
        if name.find('"') >= 0:
            name = name.replace('"', "")

        # Вводим полное название
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(name)
        time.sleep(3)
        # Проверяем названия найденных сущностей по целому названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f'Не найдено сущностей по вводу в строку поиска значение {name}'
        assert name in list_name_found, f'Не найдено сущности "{name}" по вводу значения в строку поиска - {name}. ' \
                                        f'Отображенные сущности: {list_name_found}'

        # Сбрасываем все настройки нажатием кнопки "Сбросить"
        self.browser.find_element(*KnowledgeSearchLocators.CLEAR_LINE_BUTTON).click()

    def search_line_by_department(self, data_dict):
        # Вводим в строку значение подразделение
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(data_dict["executiveUnit"])
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f'Не отображено найденных проектов при вводе " \
                                         f"в строку поиска значение Подразделение - {data_dict["executiveUnit"]}'
        assert data_dict["fullName"] in list_name_found, \
            f'Не найдена сущность по поиску значения Подразделение - "{data_dict["executiveUnit"]}"  в строке поиска'

        # Проверяем отображение поля "Подразделение" и значение в нем
        list_department_found = self.item_text_collector(*KnowledgeSearchLocators.DEPARTMENT_VALUE_IN_RESULT)
        assert len(list_department_found) > 0, 'Не отображено поле "Подразделение" или ' \
                                               'значение в поле карточки сущности'
        for element in set(list_department_found):
            assert data_dict["executiveUnit"] in element, \
                f'Отображены сущности без значения "{data_dict["executiveUnit"]}" ' \
                f'в поле Подразделение при вводе в строку поиска.'

    def search_line_by_executive_unit_legal(self, data_dict):
        exec_unit_legal = data_dict["executiveUnitLegal"]
        exec_unit_legal = exec_unit_legal.replace('"', "")
        # Вводим в строку значение юр.лицо-исполнитель
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(exec_unit_legal)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные результаты по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f'Не отображено найденных проектов при вводе " \
                                         f"в строку поиска значение Юр.лицо-исполнитель - {exec_unit_legal}'
        assert data_dict["fullName"] in list_name_found, \
            f'Не найдена сущность по поиску значения Исполнитель - "{exec_unit_legal}" в строке поиска'

        # Проверяем отображение поля "Юр.лицо-исполнитель" и значение в нем
        list_department_found = self.item_text_collector(*KnowledgeSearchLocators.LEGAL_VALUE_IN_RESULT)
        assert len(list_department_found) > 0, 'Не отображено значений или не отображено поле Юр.лицо-Исполнитель ' \
                                               'в карточке сущности'
        for element in set(list_department_found):
            assert data_dict["executiveUnitLegal"] in element, \
                f'Отображены сущности без значения "{data_dict["executiveUnitLegal"]}" в поле Подразделение при вводе в строку поиска. ' \
                f'Искомое значение отсутствует в сущности: "{element}"'

    def search_line_by_customer(self, data_dict):
        if isinstance(data_dict["customer"], str):
            name_customer = [data_dict["customer"]]
        else:
            name_customer = data_dict["customer"][0]
        # Вводим в строку значение заказчика
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(name_customer)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные результаты по названию сущности
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f'Не отображено найденных проектов при вводе " \
                                         f"в строку поиска значение Заказчики - {name_customer}'
        assert data_dict["fullName"] in list_name_found, \
            f'Не найдена сущность по поиску значения Заказчик - "{name_customer}" в строке поиска'

        # Проверяем отображение поля "Заказчик" и значение в нем
        list_customer_found = self.item_text_collector(*KnowledgeSearchLocators.CUSTOMER_VALUE_IN_RESULT)
        assert len(list_customer_found) > 0, 'Не отображено значений или не отображено поле Заказчик в карточке сущности'
        for element in list_customer_found:
            assert name_customer in element, \
                f'Отображены сущности без значения "{name_customer}" в поле Заказчик при вводе в строку поиска. ' \
                f'Искомое значение отсутствует в сущности: "{element}"'

    def search_line_by_type_works_and_services(self, data_dict):
        name_type_work = data_dict["typeOfWorkServices"][0]
        # Вводим в строку значение тип работ и услуг
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(name_type_work)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f"Не отображено найденных проектов при вводе " \
                                         f"в строку поиска значение Тип работ и услуг - {name_type_work}"
        assert data_dict["fullName"] in list_name_found, \
            f'Не найдена сущность по поиску значения Тип работ и услуг - "{name_type_work}" в строке поиска'

        # Проверяем отображение поля "Тип работ и услуг" и значение в нем
        list_type_work_found = self.item_text_collector(*KnowledgeSearchLocators.TYPE_WORKS_VALUE_IN_RESULT)
        assert len(list_type_work_found) > 0, 'Не отображено поле "Тип работ и услуг" ' \
                                              'или значение в поле в карточке сущности'
        for element in list_type_work_found:
            assert name_type_work in element, \
                f'Отображены сущности без значения "{name_type_work}" в поле Тип работ и услуг при вводе в строку поиска. ' \
                f'Искомое значение отсутствует в значении: "{element}"'

    def search_line_by_technologies(self, data_dict):
        name_technologies = data_dict["technologies"][0]
        # Вводим в строку значение технологии
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(name_technologies)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f"Не отображено найденных проектов при вводе " \
                                         f"в строку поиска значение Технология - {name_technologies}"
        assert data_dict["fullName"] in list_name_found, \
            f'Не найдена сущность по поиску значения Технология - "{name_technologies}" в строке поиска'

        # Проверяем отображение поля "Технология" и значение в нем
        list_tecnologies_found = self.item_text_collector(*KnowledgeSearchLocators.TECHNOLOGIES_VALUE_IN_RESULT)
        assert len(list_tecnologies_found) > 0, 'Не отображено поле "Технологии" или значение в поле в карточке сущности'
        for element in list_tecnologies_found:
            assert name_technologies in element, \
                f'Отображены сущности без значения "{list_tecnologies_found}" в поле Технологии при вводе в строку поиска. ' \
                f'Искомое значение отсутствует в значении: "{element}"'

    def search_line_by_category(self, project_data_dict):
        name_category = project_data_dict["projectCategory"]
        # Вводим в строку значение категории
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(name_category)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f"Не отображено найденных проектов при вводе " \
                                         f"в строку поиска значение Категория - {name_category}"
        assert project_data_dict["fullName"] in list_name_found, \
            f'Не найдена сущность по поиску значения Категория - "{name_category}" в строке поиска'

        # Проверяем отображение поля "Категория" и значение в нем
        list_categories_found = self.item_text_collector(*KnowledgeSearchLocators.CATEGORY_VALUE_IN_RESULT)
        assert len(list_categories_found) > 0, 'Не отображено поле "Категория" или значение в поле в карточке сущности Проект'
        for element in list_categories_found:
            assert name_category in element, \
                f'Отображены сущности без значения "{list_categories_found}" в поле Категория при вводе в строку поиска. ' \
                f'Искомое значение отсутствует в сущности: "{element}"'

    def search_line_by_number(self, contract_data_dict):
        number_contract = contract_data_dict["numberContract"]
        # Вводим в строку значение номер контракта
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(number_contract)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f"Не отображено найденных договор/контрактов при вводе " \
                                         f"в строку поиска значение Номер контракта - {number_contract}"
        assert contract_data_dict["fullName"] in list_name_found, \
            f'Не найдена сущность по поиску значения Номер контракта - "{number_contract}" в строке поиска'

        # Проверяем отображение поля "Номер" и значение в нем
        list_number_found = self.item_text_collector(*KnowledgeSearchLocators.CONTRACT_NUMBER_VALUE_IN_RESULT)
        assert len(list_number_found) > 0, 'Не отображено поле "Номер" или значение в поле в карточке сущности Договор/контракт'
        assert number_contract in list_number_found, \
                f'Отображены сущности без значения "{number_contract}" в поле Номер при вводе в строку поиска. ' \
                f'Список найденных значений: "{list_number_found}"'

    def search_line_ulip_by_name(self, data_dict):
        # Удаляем спецсимволы из переменной
        short_name = data_dict["shortName"].replace('"', "")
        # Вводим полное название
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(short_name)
        time.sleep(3)
        # Проверяем названия найденных сущностей по целому названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f'Не найдено сущностей по вводу в строку поиска значение {short_name}'
        new_list_name_found = []
        for element in list_name_found:
            new_element = element.replace('"', "")
            new_list_name_found.append(new_element)
        assert short_name in new_list_name_found, f'Не найдено сущности "{data_dict["shortName"]}" по вводу значения в строку поиска - {short_name}. ' \
                                        f'Отображенные сущности: {new_list_name_found}'

        # Сбрасываем все настройки нажатием кнопки "Сбросить"
        self.browser.find_element(*KnowledgeSearchLocators.CLEAR_LINE_BUTTON).click()

    def search_line_by_industry(self, ulip_data_dict):
        industry = ulip_data_dict["industry"]
        # Вводим в строку значение отрасль
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(industry)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f"Не отображено найденных Юр.лиц/ИП при вводе " \
                                         f"в строку поиска значение Отрасль - {industry}"
        assert ulip_data_dict["shortName"] in list_name_found, \
            f'Не найдена сущность с названием {ulip_data_dict["shortName"]} по поиску значения ' \
            f'Отрасль - "{industry}" в строке поиска'

        # Проверяем отображение поля "Отрасль" и значение в нем
        list_industry_found = self.item_text_collector(*KnowledgeSearchLocators.INDUSTRY_VALUE_IN_RESULT)
        assert len(list_industry_found) > 0, 'Не отображено поле "Отрасль" или значение в поле в карточке сущности Юр.лицо/ИП'
        assert industry in list_industry_found, \
                f'Отображены сущности без значения "{industry}" в поле Отрасль при вводе в строку поиска. ' \
                f'Список найденных значений: "{list_industry_found}"'

    def search_line_by_ogrn(self, ulip_data_dict):
        ogrn = ulip_data_dict["ogrn"]
        # Вводим в строку значение ОГРН
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(ogrn)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f"Не отображено найденных Юр.лиц/ИП при вводе " \
                                         f"в строку поиска значение ОГРН - {ogrn}"
        assert ulip_data_dict["shortName"] in list_name_found, \
            f'Не найдена сущность с названием {ulip_data_dict["shortName"]} по поиску значения ' \
            f'ОГРН - "{ogrn}" в строке поиска'

        # Проверяем отображение поля "ОГРН" и значение в нем
        list_ogrn_found = self.item_text_collector(*KnowledgeSearchLocators.OGRN_VALUE_IN_RESULT)
        assert len(list_ogrn_found) > 0, 'Не отображено поле "ОГРН" или значение в поле в карточке сущности Юр.лицо/ИП'
        assert ogrn in list_ogrn_found, \
                f'Отображены сущности без значения(с пробелами) "{ogrn}" в поле ОГРН при вводе в строку поиска. ' \
                f'Список найденных значений: "{list_ogrn_found}"'

    def search_line_by_inn(self, ulip_data_dict):
        inn = ulip_data_dict["inn"]
        # Вводим в строку значение ИНН
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(inn)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f"Не отображено найденных Юр.лицо при вводе " \
                                         f"в строку поиска значение ИНН - {inn}"
        assert ulip_data_dict["shortName"] in list_name_found, \
            f'Не найдена сущность с названием {ulip_data_dict["shortName"]} по поиску значения ' \
            f'ИНН - "{inn}" в строке поиска'

        # Проверяем отображение поля "ИНН" и значение в нем
        list_inn_found = self.item_text_collector(*KnowledgeSearchLocators.INN_VALUE_IN_RESULT)
        assert len(list_inn_found) > 0, 'Не отображено поле "ИНН" или значение в поле в карточке сущности Юр.лицо'
        assert inn in list_inn_found, \
                f'Отображены сущности без значения(с пробелами) "{inn}" в поле ИНН при вводе в строку поиска. ' \
                f'Список найденных значений: "{list_inn_found}"'

    def search_line_by_kpp(self, ulip_data_dict):
        kpp = ulip_data_dict["kpp"]
        # Вводим в строку значение КПП
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(kpp)
        time.sleep(3)

        # Подгружаем весь список найденных сущностей
        self.load_all_result()

        # Проверяем найденные по названию
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAMES_OF_ALL_FOUND_ELEMENT)
        assert len(list_name_found) > 0, f"Не отображено найденных Юр.лицо при вводе " \
                                         f"в строку поиска значение КПП - {kpp}"
        assert ulip_data_dict["shortName"] in list_name_found, \
            f'Не найдена сущность с названием {ulip_data_dict["shortName"]} по поиску значения ' \
            f'КПП - "{kpp}" в строке поиска'

        # Проверяем отображение поля "ИНН" и значение в нем
        list_kpp_found = self.item_text_collector(*KnowledgeSearchLocators.KPP_VALUE_IN_RESULT)
        assert len(list_kpp_found) > 0, 'Не отображено поле "КПП" или значение в поле в карточке сущности Юр.лицо'
        assert kpp in list_kpp_found, \
                f'Отображены сущности без значения(с пробелами) "{kpp}" в поле КПП при вводе в строку поиска. ' \
                f'Список найденных значений: "{list_kpp_found}"'


    def search_with_customer_block_filter(self, data_dict):
        # Жмем кнопку "Весь список" в блоке "Заказчик"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Свернуть")
        #
        if isinstance(data_dict["customer"], str):
            original_list_customer = [data_dict["customer"]]
        else:
            original_list_customer = data_dict["customer"]
        # Поиск и активация чек-боксов
        for element in original_list_customer:
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
            time.sleep(2)

            # Проверяем результаты фильтраци по названию сущности
            self.checking_the_found_name(data_dict["fullName"], "Заказчик")

            # Проверяем результаты фильтрации по полю "Заказчик"
            list_customer_found = self.item_text_collector(*KnowledgeSearchLocators.CUSTOMER_VALUE_IN_RESULT)
            result = 0
            for found_value in list_customer_found:
                if element in found_value:
                    result += 1
            assert result > 1, \
                f'После фильтрации по полю "Заказчик" не отображено ожидаемого результата ' \
                f'или в карточке отсутствует поле "Заказчик"\n ' \
                f'Ожидаемый результат: Значение "{element}" в поле "Заказчик"\n ' \
                f'Фактические результаты: {set(list_customer_found)}'

        # Деактивируем чек-боксы
        for element in original_list_customer:
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
        # Жмем кнопку "Весь список" у блока "Юр.лицо-исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK, "Свернуть")

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
        time.sleep(2)

        """
        # Поле "Юр.лицо-исполнитель" не отображено в карточке "Проект"
        # Проверяем найденные значения по блоку "Юр.лицо-исполнитель"
        list_legal_found = self.item_text_collector(*KnowledgeSearchLocators.LEGAL_VALUE_IN_RESULT)
        assert data_dict["executiveUnitLegal"] in set(list_legal_found), \
            f'После фильтрации по полю "Заказчик" не отображено ожидаемого результата\n ' \
            f'Ожидаемый результат: {data_dict["executiveUnitLegal"]}\n ' \
            f'Фактические результаты: {set(list_legal_found)}'
        """

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Юр.лицо-исполнитель")

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
        time.sleep(2)

        # Проверяем найденные значения по блоку "Подразделение-исполнитель"
        list_executive_found = self.item_text_collector(*KnowledgeSearchLocators.DEPARTMENT_VALUE_IN_RESULT)
        assert data_dict["executiveUnit"] in set(list_executive_found), \
            f'После фильтрации по полю "Подразделение-исполнитель" не отображено значения "Юр.лицо-исполнитель" в найденных результатах\n ' \
            f'Ожидаемый результат: {data_dict["executiveUnit"]}\n ' \
            f'Фактические результаты: {set(list_executive_found)}'

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Подразделение-исполнитель")

        # Вводим повторно значение в строку поиска
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
            data_dict["executiveUnit"])

        # Деактивируем чек-бокс в блоке "Подразделение-исполнитель"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", data_dict["executiveUnit"])
        self.browser.find_element(how, what).click()

        # Закрываем "Весь список" в блоке "Подразделение-исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_PERFORMER_BLOCK, "Весь список")

    def search_with_type_works_block_filter(self, data_dict):

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
            time.sleep(2)

            """
            # Не отображено поле "Тип работ и услуг" в карточке "Проект"
            # Проверяем результаты фильтрации по полю "Тип работ и услуг"
            list_type_works_found = self.item_text_collector(*KnowledgeSearchLocators.TYPE_WORKS_VALUE_IN_RESULT)
            
            """

            # Проверяем результаты фильтраци по названию сущности
            self.checking_the_found_name(data_dict["fullName"], "Тип работ и услуг")

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
            time.sleep(2)

            # Проверяем результаты фильтрации по полю "Технологии"
            list_technologies_found = self.item_text_collector(*KnowledgeSearchLocators.TECHNOLOGIES_VALUE_IN_RESULT)
            result = 0
            for found_value in set(list_technologies_found):
                if element in found_value:
                    result += 1
            assert result > 0, \
                f'После фильтрации по полю "Технология" не отображено ожидаемого результата ' \
                f'или в карточке отсутствует поле "Технология"\n ' \
                f'Ожидаемый результат: {element}\n ' \
                f'Фактические результаты: {set(list_technologies_found)}'

            # Проверяем результаты фильтраци по названию сущности
            self.checking_the_found_name(data_dict["fullName"], "Технологию")

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
        # Жмем кнопку "Весь список" в блоке "Заказчик"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Свернуть")

        # Активируем чек-боксы в категории "Заказчик"
        for element in data_dict["customer"]:
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
            self.checking_the_found_name(data_dict["fullName"], "Заказчик")

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
        self.checking_the_found_name(data_dict["fullName"], "Юр.лицо-исполнитель")

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
        self.checking_the_found_name(data_dict["fullName"], "Подразделение-исполнитель")

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
            self.checking_the_found_name(data_dict["fullName"], "Тип работ и услуг")

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
            self.checking_the_found_name(data_dict["fullName"], "Технологии")

        # Закрываем "Весь список" в блоке "Технологии"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK, "Весь список")

    def search_with_sum_block_filter(self, data_dict):
        self.browser.implicitly_wait(1)
        # Переменные в поле От и До

        sum_from = data_dict["sumInRub"]
        sum_to = data_dict["sumInRub"]

        # Заполняем поле "Стоимость проекта (руб.) ОТ"
        self.browser.find_element(*KnowledgeSearchLocators.SUM_FROM).send_keys(sum_from)
        time.sleep(2)

        # Подгружаем весь список найденных результатов
        self.load_all_result()

        # Проверяем что список найденных сущностей не пустой
        list_sum_from_found = self.item_text_collector(*KnowledgeSearchLocators.SUM_VALUE_IN_RESULT)
        assert len(list_sum_from_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле "Сумма контракта ОТ" ({sum_from})'

        # Проверяем найденные сущности на соответствие фильтрации по полю "Сумма контракта ОТ"
        for element in list_sum_from_found:
            if element.find(".") > 0:
                element = float(element.replace(" ", ""))
            else:
                element = int(element.replace(" ", ""))
            assert sum_from <= element, \
                f'Условие: Показать сущности где сумма больше или равна {sum_from}, отображена сущность со значением {element}'

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Сумма контракта ОТ")

        # Очищаем поле "Сумма контракта ОТ"
        self.browser.find_element(*KnowledgeSearchLocators.SUM_FROM).clear()

        # Заполняем поле "Стоимость проекта (руб.) ДО"
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

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Сумма контракта ДО")

        # Очищаем поле "Сумма контракта ДО"
        self.browser.find_element(*KnowledgeSearchLocators.SUM_TO).clear()

        # Заполняем поле "Стоимость проекта (руб.) ОТ"
        self.browser.find_element(*KnowledgeSearchLocators.SUM_FROM).send_keys(data_dict["sumInRub"])

        # Заполняем поле "Стоимость проекта (руб.) ДО"
        self.browser.find_element(*KnowledgeSearchLocators.SUM_TO).send_keys(data_dict["sumInRub"])
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

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Сумма контракта ОТ и Сумма контракта ДО")

    def search_with_start_date_block_filter(self, data_dict):
        self.browser.implicitly_wait(2)
        # Преобразовываем строку в дату.
        # Переменная для ввода в поле ОТ.
        start_date_from_dt = (datetime.strptime(data_dict["startDate"], '%d.%m.%Y'))

        # Переменная для ввода в поле ДО.
        start_date_to_dt = (datetime.strptime(data_dict["startDate"], '%d.%m.%Y'))

        # Заполняем поле "Дата заключения ОТ"
        start_date_from_element = (self.browser.find_elements(*KnowledgeSearchLocators.START_DATE)[0])
        start_date_from_element.send_keys(start_date_from_dt.strftime('%d.%m.%Y'))

        # Для отображения результата нажимаем 'Tab' (необходимо переключение на другой элемент)
        start_date_from_element.send_keys(u'\ue004')
        time.sleep(2)

        # Подгружаем весь список найденных результатов
        self.load_all_result()

        # Проверяем найденные результаты по фильтрации по полю "Дата заключения ОТ"
        list_startdate_from_found = self.item_text_collector(*KnowledgeSearchLocators.START_DATE_VALUE_IN_RESULT)
        assert len(list_startdate_from_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле ' \
            f'"Дата заключения ОТ" ({start_date_from_dt.strftime("%d.%m.%Y")}) '

        for element in list_startdate_from_found:
            fact_start_date_from = datetime.strptime(element, '%d.%m.%Y')
            assert start_date_from_dt <= fact_start_date_from, \
                f'Условие: Показать сущности где дата больше(ОТ) или равна {start_date_from_dt.strftime("%d.%m.%Y")}' \
                f', отображена сущность датой {fact_start_date_from.strftime("%d.%m.%Y")}'

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Дата заключения ОТ")

        # Очищаем строку "Дата заключения ОТ"
        start_date_from_element.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        time.sleep(1)

        # Заполняем поле "Дата заключения ДО"
        start_date_to_element = (self.browser.find_elements(*KnowledgeSearchLocators.START_DATE)[1])
        start_date_to_element.send_keys(start_date_to_dt.strftime('%d.%m.%Y'))

        # Для отображения результата нажимаем 'Tab' (необходимо переключение на другой элемент)
        start_date_to_element.send_keys(u'\ue004')
        time.sleep(2)

        # Проверяем найденные результаты по фильтрации по полю "Дата заключения ДО"
        list_startdate_to_found = self.item_text_collector(*KnowledgeSearchLocators.START_DATE_VALUE_IN_RESULT)
        assert len(list_startdate_to_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле ' \
            f'"Дата заключения ДО" ({start_date_to_dt.strftime("%d.%m.%Y")}) '

        for element in list_startdate_to_found:
            fact_start_date_to = datetime.strptime(element, '%d.%m.%Y')
            assert start_date_to_dt >= fact_start_date_to, \
                f'Условие: Показать сущности где дата меньше(ДО) или равна {start_date_to_dt.strftime("%d.%m.%Y")}' \
                f', отображена сущность датой {fact_start_date_to.strftime("%d.%m.%Y")}'

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Дата заключения ДО")

        # Очищаем строку "Дата заключения ДО"
        start_date_to_element.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        time.sleep(1)

        # Заполняем поле "Дата заключения ОТ"
        start_date_from_element = (self.browser.find_elements(*KnowledgeSearchLocators.START_DATE)[0])
        start_date_from_element.send_keys(start_date_from_dt.strftime('%d.%m.%Y'))
        start_date_to_element.send_keys(u'\ue004')

        # Заполняем поле "Дата заключения ДО"
        start_date_to_element = (self.browser.find_elements(*KnowledgeSearchLocators.START_DATE)[1])
        start_date_to_element.send_keys(start_date_to_dt.strftime('%d.%m.%Y'))
        start_date_to_element.send_keys(u'\ue004')

        time.sleep(2)
        # Проверяем найденные результаты по фильтрации по полю "Дата заключения ОТ и "Дата заключения ДО"
        list_start_date_from_to_found = self.item_text_collector(*KnowledgeSearchLocators.START_DATE_VALUE_IN_RESULT)
        assert len(list_start_date_from_to_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле ' \
            f'"Дата заключения ОТ" ({data_dict["startDate"]}) и Дата заключения ДО ({data_dict["startDate"]})'

        for element in list_start_date_from_to_found:
            fact_start_date_to = datetime.strptime(element, '%d.%m.%Y')
            assert start_date_from_dt <= fact_start_date_to <= start_date_to_dt, \
                f'Условие: Показать сущности где дата больше(ОТ) или равна {start_date_from_dt.strftime("%d.%m.%Y")} И' \
                f'Показать сущности где дата меньше(ДО) или равна {start_date_to_dt.strftime("%d.%m.%Y")}, ' \
                f'отображена сущность датой {fact_start_date_to.strftime("%d.%m.%Y")}'

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Дата заключения ОТ и Дата заключения ДО")

    def search_with_end_date_block_filter(self, data_dict):
        # Преобразовываем строку в дату.
        # Переменная для ввода в поле ОТ.
        end_date_from_dt = (datetime.strptime(data_dict["endDate"], '%d.%m.%Y'))

        # Переменная для ввода в поле ДО.
        end_date_to_dt = (datetime.strptime(data_dict["endDate"], '%d.%m.%Y'))

        # Заполняем поле "Дата завершения ОТ"
        end_date_from_element = (self.browser.find_elements(*KnowledgeSearchLocators.END_DATE)[0])
        end_date_from_element.send_keys(end_date_from_dt.strftime('%d.%m.%Y'))

        # Для отображения результата нажимаем 'Tab' (необходимо переключение на другой элемент)
        end_date_from_element.send_keys(u'\ue004')
        time.sleep(1)

        # Подгружаем весь список найденных результатов
        self.load_all_result()

        # Проверяем найденные результаты по фильтрации по полю "Дата заключения ОТ"
        list_end_date_from_found = self.item_text_collector(*KnowledgeSearchLocators.END_DATE_VALUE_IN_RESULT)
        assert len(list_end_date_from_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле ' \
            f'"Дата завершения ОТ" ({end_date_from_dt.strftime("%d.%m.%Y")}) '

        for element in list_end_date_from_found:
            fact_end_date_from = datetime.strptime(element, '%d.%m.%Y')
            assert end_date_from_dt <= fact_end_date_from, \
                f'Условие: Показать сущности где дата завершения больше(ОТ) или равна {end_date_from_dt.strftime("%d.%m.%Y")}' \
                f', отображена сущность датой {fact_end_date_from.strftime("%d.%m.%Y")}'

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Дата завершения ОТ")

        # Очищаем строку "Дата заключения ОТ"
        end_date_from_element.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        time.sleep(2)

        # Заполняем поле "Дата завершения ДО"
        end_date_to_element = (self.browser.find_elements(*KnowledgeSearchLocators.END_DATE)[1])
        end_date_to_element.send_keys(end_date_to_dt.strftime('%d.%m.%Y'))

        # Для отображения результата нажимаем 'Tab' (необходимо переключение на другой элемент)
        end_date_to_element.send_keys(u'\ue004')
        time.sleep(1)

        # Подгружаем весь список найденных результатов
        self.load_all_result()

        # Проверяем найденные результаты по фильтрации по полю "Дата завершения ДО"
        list_end_date_to_found = self.item_text_collector(*KnowledgeSearchLocators.START_DATE_VALUE_IN_RESULT)
        assert len(list_end_date_to_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле ' \
            f'"Дата завершения ДО" ({end_date_to_dt.strftime("%d.%m.%Y")}) '

        for element in list_end_date_to_found:
            fact_end_date_to = datetime.strptime(element, '%d.%m.%Y')
            assert end_date_to_dt >= fact_end_date_to, \
                f'Условие: Показать сущности где дата завершения меньше(ДО) или равна {end_date_to_dt.strftime("%d.%m.%Y")}' \
                f', отображена сущность датой {fact_end_date_to.strftime("%d.%m.%Y")}'

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Дата завершения ДО")

        # Очищаем строку "Дата завершения ДО"
        end_date_to_element.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        time.sleep(2)

        # Заполняем поле "Дата завершения ОТ"
        end_date_from_element = (self.browser.find_elements(*KnowledgeSearchLocators.END_DATE)[0])
        end_date_from_element.send_keys(end_date_from_dt.strftime('%d.%m.%Y'))
        end_date_to_element.send_keys(u'\ue004')

        # Заполняем поле "Дата завершения ДО"
        end_date_to_element = (self.browser.find_elements(*KnowledgeSearchLocators.END_DATE)[1])
        end_date_to_element.send_keys(end_date_to_dt.strftime('%d.%m.%Y'))
        end_date_to_element.send_keys(u'\ue004')

        time.sleep(1)
        # Проверяем найденные результаты по фильтрации по полю "Дата завершения ОТ и "Дата завершения ДО"
        list_end_date_from_to_found = self.item_text_collector(*KnowledgeSearchLocators.END_DATE_VALUE_IN_RESULT)
        assert len(list_end_date_from_to_found) > 0, \
            f'Не найдено ни одного результата по вводу значения в поле: ' \
            f'"Дата заключения ОТ" ({end_date_from_dt.strftime("%d.%m.%Y")}) И ' \
            f'Дата заключения ДО ({end_date_to_dt.strftime("%d.%m.%Y")})'

        for element in list_end_date_from_to_found:
            fact_end_date_to = datetime.strptime(element, '%d.%m.%Y')
            assert end_date_from_dt <= fact_end_date_to <= end_date_to_dt, \
                f'Условие: Показать сущности где дата  завершения больше(ОТ) или равна {end_date_from_dt.strftime("%d.%m.%Y")} И ' \
                f'Показать сущности где дата завершения меньше(ДО) или равна {end_date_to_dt.strftime("%d.%m.%Y")}, ' \
                f'отображена сущность датой {fact_end_date_to.strftime("%d.%m.%Y")}'

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Дата завершения ОТ и Дата завершения ДО")

        # Жмем кнопку "Сбросить"
        self.browser.find_element(*KnowledgeSearchLocators.RESET_BUTTON).click()

    def search_with_status_block_filter(self, data_dict):
        # Активируем чек-бокс "Проект" в блоке фильтрации "Статус контракта"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Проект")
        status_checkbox = self.browser.find_elements(how, what)[1]
        status_checkbox.click()
        # Проверяем активацию чек-бокса в блоке "Статус контракта"
        assert status_checkbox.get_attribute("aria-checked") == "true", \
            f'Чек-бокс {"Проект"} в блоке "Статус контракта" не активирован'
        time.sleep(2)

        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], 'Чек-бокс "Проект" в блоке "Статус контракта"')

        # Деактивируем чек-бокс "Проект" в блоке фильтрации "Статус контракта"
        status_checkbox.click()
        # Проверяем деактивацию чек-бокса в блоке "Статус контракта"
        assert status_checkbox.get_attribute("aria-checked") == "false", \
            f'Чек-бокс {"Проект"} в блоке "Статус контракта" не ДЕактивирован'

    def search_with_all_fast_filter_on_contract(self, data_dict):

        # Заполняем поле "Стоимость проекта (руб.) ОТ"
        self.browser.find_element(*KnowledgeSearchLocators.SUM_FROM).send_keys(data_dict["sumInRub"])
        time.sleep(2)
        # Подгружаем весь список найденных результатов
        self.load_all_result()
        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Сумма контракта ОТ")

        # Заполняем поле "Стоимость проекта (руб.) ДО"
        self.browser.find_element(*KnowledgeSearchLocators.SUM_TO).send_keys(data_dict["sumInRub"] + 1000000)
        time.sleep(2)
        # Подгружаем весь список найденных результатов
        self.load_all_result()
        # Проверяем результаты фильтраци по названию сущности
        self.checking_the_found_name(data_dict["fullName"], "Сумма контракта ОТ и Сумма контракта ДО")

        # Заполняем поле "Дата заключения ОТ"
        start_date_from_element = (self.browser.find_elements(*KnowledgeSearchLocators.START_DATE)[0])
        start_date_from_element.send_keys(data_dict["startDate"])
        # Для отображения результата нажимаем 'Tab' (необходимо переключение на другой элемент)
        start_date_from_element.send_keys(u'\ue004')
        time.sleep(2)
        # Подгружаем весь список найденных результатов
        self.load_all_result()
        # Проверяем результат по названию сущности
        # self.checking_the_found_name(data_dict["fullName"], "Дата заключения От")

        # Заполняем поле "Дата заключения ДО"
        start_date_to_element = (self.browser.find_elements(*KnowledgeSearchLocators.START_DATE)[1])
        start_date_to_element.send_keys(data_dict["startDate"])
        # Для отображения результата нажимаем 'Tab' (необходимо переключение на другой элемент)
        start_date_to_element.send_keys(u'\ue004')
        time.sleep(2)
        # Подгружаем весь список найденных результатов
        self.load_all_result()
        # Проверяем результат по названию сущности
        # self.checking_the_found_name(data_dict["fullName"], "Дата заключения До")

        # Заполняем поле "Дата завершения ОТ"
        end_date_from_element = (self.browser.find_elements(*KnowledgeSearchLocators.END_DATE)[0])
        end_date_from_element.send_keys(data_dict["endDate"])
        # Для отображения результата нажимаем 'Tab' (необходимо переключение на другой элемент)
        end_date_from_element.send_keys(u'\ue004')
        time.sleep(1)
        # Подгружаем весь список найденных результатов
        self.load_all_result()
        # Проверяем результат по названию сущности
        # self.checking_the_found_name(data_dict["fullName"], "Дата заключения До")

        # Заполняем поле "Дата завершения ДО"
        end_date_to_element = (self.browser.find_elements(*KnowledgeSearchLocators.END_DATE)[1])
        end_date_to_element.send_keys(data_dict["endDate"])
        end_date_to_element.send_keys(u'\ue004')
        time.sleep(1)
        # Подгружаем весь список найденных результатов
        self.load_all_result()
        # Проверяем результат по названию сущности
        # self.checking_the_found_name(data_dict["fullName"], "Дата заключения До")

        # Активируем чек-бокс "Проект" в блоке фильтрации "Статус контракта"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", "Проект")
        status_checkbox = self.browser.find_elements(how, what)[1]
        status_checkbox.click()
        # Проверяем активацию чек-бокса в блоке "Статус контракта"
        assert status_checkbox.get_attribute("aria-checked") == "true", \
            f'Чек-бокс {"Проект"} в блоке "Статус контракта" не активирован'
        time.sleep(2)

        # Жмем кнопку "Весь список" в блоке "Заказчик"
        if isinstance(data_dict["customer"], list):
            customer = data_dict["customer"][0]
        else:
            customer = data_dict["customer"]
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Свернуть")
        # Вводим в строку поиска первое значение "Заказчик"
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(customer)
        # Активируем найденный чек-бокс
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", customer)
        customer_checkbox = self.browser.find_element(how, what)
        customer_checkbox.click()
        # Проверяем активацию чек-бокса в блоке "Заказчик"
        assert self.browser.find_element(how, what).get_attribute("aria-checked") == "true", \
            f'Чек-бокс {customer} в блоке "Заказчик" не активирован'
        time.sleep(2)
        # Проверяем результат по названию сущности
        # self.checking_the_found_name(data_dict["fullName"], "Дата заключения До")
        # Закрываем "Весь список" в блоке "Заказчики"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_CUSTOMER_BLOCK, "Весь список")

        # Жмем кнопку "Весь список" у блока "Юр.лицо-исполнитель"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_LEGAL_BLOCK, "Свернуть")
        # В строку поиска блока "Юр.лицо-исполнитель" вводим значение
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE_IN_BLOCK_FILTER).send_keys(
            data_dict["executiveUnitLegal"])
        # Активируем найденный чек-бокс в блоке "Юр.лицо-исполнитель"
        how, what = KnowledgeSearchLocators.TEMPLATE_CHECKBOX
        what = what.replace("name", data_dict["executiveUnitLegal"])
        self.browser.find_element(how, what).click()
        # Проверяем результаты фильтраци по названию сущности
        #self.checking_the_found_name(data_dict["fullName"], "Юр.лицо-исполнитель")
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
        time.sleep(2)
        # Проверяем результаты фильтраци по названию сущности
        #self.checking_the_found_name(data_dict["fullName"], "Подразделение-исполнитель")
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
            time.sleep(2)
            # Проверяем результаты фильтраци по названию сущности
            #self.checking_the_found_name(data_dict["fullName"], "Тип работ и услуг")
        # Закрываем "Весь список" в блоке "Тип работ и услуг"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TYPEWORKS_BLOCK, "Весь список")

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
            time.sleep(2)
            # Проверяем результаты фильтраци по названию сущности
            #self.checking_the_found_name(data_dict["fullName"], "Технологию")
        # Закрываем "Весь список" в блоке "Технологии"
        self.browser.find_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK).click()
        self.is_text_to_be_present_in_element(*KnowledgeSearchLocators.ALL_LIST_TECHNOLOGIES_BLOCK, "Весь список")
        breakpoint()



