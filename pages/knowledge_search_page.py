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

    def test_default_fast_filter(self):
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')
        delayed_assert.expect("Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"')
        delayed_assert.expect("Холдинги" in list_filter, 'Отсутствует блок фильтра "Холдинги"')
        delayed_assert.expect("Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"')
        delayed_assert.expect("Подразделение-исполнитель" in list_filter, 'Отсутствует блок фильтра "Подразделение-исполнитель"')
        delayed_assert.expect("Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"')
        delayed_assert.expect("Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"')

        """
        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()
        web_elements_found = self.browser.find_elements(*KnowledgeSearchLocators.TYPES_ON_ALL_FOUND_ELEMENT)
        list_found_element = item_text_collector()
        for item in web_elements_found:
            list_found_element.append(item.text)
        """

    def test_fast_filter_project(self):
        # Активируем чек-бокс "Проект"
        project_checkbox = self.browser.find_element(*KnowledgeSearchLocators.PROJECT_CHECKBOX)
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
        delayed_assert.expect("Подразделение-исполнитель" in list_filter, 'Отсутствует блок фильтра "Подразделение-исполнитель"')
        delayed_assert.expect("Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"')
        delayed_assert.expect("Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"')

        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()

        # Проверяем фильтрацию по чек-боксу "Проект"
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_ON_ALL_FOUND_ELEMENT)
        delayed_assert.expect("ПРОЕКТ" in (set(list_found_element)), f'Отображены сущности {set(list_found_element)}\nОжидаемый результат: отображены сущности типа "Проект"')
        delayed_assert.expect(len(set(list_found_element)) == 1, "Отображены сущности не только категории Проект")

        # Деактивируем чек-бокс фильтрации по сущности "Проект"
        project_checkbox.click()
        assert project_checkbox.get_attribute("aria-checked") == "false", 'Чек-бокс "Проект" не деактивирован'


    def test_fast_filter_contract(self):
        # Активируем чек-бокс "Договор(контракт)"
        contract_checkbox = self.browser.find_element(*KnowledgeSearchLocators.CONTRACT_CHECKBOX)
        contract_checkbox.click()
        # Проверяем активацию чек-бокса
        assert contract_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Договор(контракт)" не активирован'
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Договор/контракт"
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')
        delayed_assert.expect("Стоимость проекта (руб.)" in list_filter, 'Отсутствует блок фильтра "Стоимость проекта (руб.)"')
        delayed_assert.expect("Дата заключения" in list_filter, 'Отсутствует блок фильтра "Дата заключения"')
        delayed_assert.expect("Дата завершения" in list_filter, 'Отсутствует блок фильтра "Дата завершения"')
        delayed_assert.expect("Статус контракта" in list_filter, 'Отсутствует блок фильтра "Статус контракта"')
        delayed_assert.expect("Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"')
        # delayed_assert.expect("Холдинги" in list_filter, 'Отсутствует блок фильтра "Холдинги"')
        delayed_assert.expect("Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"')
        delayed_assert.expect("Подразделение-исполнитель" in list_filter, 'Отсутствует блок фильтра "Подразделение-исполнитель"')
        delayed_assert.expect("Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"')
        delayed_assert.expect("Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"')

        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()

        # Проверяем фильтрацию по чек-боксу "Договоры (контракты)"
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_ON_ALL_FOUND_ELEMENT)
        delayed_assert.expect("ДОГОВОР/КОНТРАКТ" in (set(list_found_element)),
                              f'Отображены сущности {set(list_found_element)} \nОжидаемый результат: "Договор/Контракт"')
        delayed_assert.expect(len(set(list_found_element)) == 1, "Отображены сущности не только категории Договор/Контракт")

        # Деактивируем чек-бокс фильтрации по сущности "Договор/контракт"
        contract_checkbox.click()
        # Проверяем деактивацию чек-бокса
        assert contract_checkbox.get_attribute("aria-checked") == "false", 'Чек-бокс "Договор(контракт)" не деактивирован'

    def test_fast_filter_division(self):
        # Активируем чек-бокс ""
        division_checkbox = self.browser.find_element(*KnowledgeSearchLocators.DIVISION_CHECKBOX)
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
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()

        # Проверяем фильтрацию по чек-боксу "Подразделение"
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_ON_ALL_FOUND_ELEMENT)
        delayed_assert.expect("ПОДРАЗДЕЛЕНИЕ" in (set(list_found_element)),
                              f'Отображены сущности {set(list_found_element)}\nОжидаемый результат: "Подразделение"')
        delayed_assert.expect(len(set(list_found_element)) == 1, "Отображены сущности не только категории Подразделение")

        # Деактивируем чек-бокс фильтрации по сущности "Подразделение"
        division_checkbox.click()
        # Проверяем деактивацию чек-бокса "Подразделение"
        assert division_checkbox.get_attribute("aria-checked") == "false", 'Чек-бокс "Подразделение" не деактивирован'

    def test_fast_filter_technology(self):
        # Активируем чек-бокс "Технологию"
        technology_checkbox = self.browser.find_element(*KnowledgeSearchLocators.TECHNOLOGY_CHECKBOX)
        technology_checkbox.click()

        # Проверяем активацию чек-бокса "Технологию"
        assert technology_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Технологию" не активирован'
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Подразделение"
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect(len(list_filter) == 1, 'Отображены лишние категории фильтров для блока "Технологии"')
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')

        """
        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()
            
        # Проверяем фильтрацию по чек-боксу "Технология"
        list_found_element = item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FOUND_ELEMENT)
        assert "ТЕХНОЛОГИЯ" in (set(list_found_element)), f'Отображены сущности {set(list_found_element)} ' \
                                                             f'\nОжидаемый результат: "Подразделение"'
        assert len(set(list_found_element)) == 1, "Отображены сущности не только категории Подразделение"
        """

        # Деактивируем чек-бокс фильтрации по сущности "Технология"
        technology_checkbox.click()

        # Проверяем деактивацию чек-бокса
        assert technology_checkbox.get_attribute("aria-checked") == "false", 'Чек-бокс "Технологию" не деактивирован'

    def test_fast_filter_legal(self):
        # Активируем чек-бокс "Юр.лицо/ИП"
        legal_checkbox = self.browser.find_element(*KnowledgeSearchLocators.LEGAL_CHECKBOX)
        legal_checkbox.click()

        # Проверяем активацию чек-бокса "Юр.лицо/ИП"
        assert legal_checkbox.get_attribute("aria-checked") == "true", 'Чек-бокс "Юр.лицо/ИП" не активирован'
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Юр.лицо/ИП"
        list_filter = self.item_text_collector(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        delayed_assert.expect(len(list_filter) == 1, 'Отображены лишние категории фильтров для блока "Технологии"')
        delayed_assert.expect("Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"')

        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()

        # Проверяем фильтрацию по чек-боксу "Юр.лицо/ИП"
        list_found_element = self.item_text_collector(*KnowledgeSearchLocators.TYPES_ON_ALL_FOUND_ELEMENT)
        delayed_assert.expect("ЮР.ЛИЦО/ИП" in (set(list_found_element)),
                              f'Отображены сущности {set(list_found_element)}\nОжидаемый результат: "Юр.лицо/ИП"')
        delayed_assert.expect(len(set(list_found_element)) == 1, "Отображены сущности не только категории Юр.лицо/ИП")

        # Деактивируем чек-бокс фильтрации по сущности "Юр.лицо/ИП"
        legal_checkbox.click()

        # Проверяем деактивацию чек-бокса
        assert legal_checkbox.get_attribute("aria-checked") == "false", 'Чек-бокс "Юр.лицо/ИП" не деактивирован'

    def test_search_line(self, data_dict):
        split_name = data_dict["fullName"].split(",")
        # Вводим первую часть названия
        self.browser.find_element(*KnowledgeSearchLocators.SEARCH_LINE).send_keys(split_name[0])
        time.sleep(3)
        # Проверяем названия найденных сущностей по первой части с служебными символами []
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAME_ON_ALL_FOUND_ELEMENT)
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
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAME_ON_ALL_FOUND_ELEMENT)
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
        list_name_found = self.item_text_collector(*KnowledgeSearchLocators.NAME_ON_ALL_FOUND_ELEMENT)
        if len(list_name_found) > 0:
            if list_name_found.count(data_dict["fullName"]) == 0:
                assert list_name_found.count(data_dict["fullName"]) == 1, \
                    f'Не найдено сущности "{data_dict["fullName"]}" по поиску значения {data_dict["fullName"]}'
        else:
            print("Не найдено результатов удовлетворяющих запросу")

        # Сбрасываем все настройки нажатием кнопки "Сбросить"
        self.browser.find_element(*KnowledgeSearchLocators.CLEAR_LINE_BUTTON).click()






























