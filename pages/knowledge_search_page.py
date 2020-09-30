import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import KnowledgeSearchLocators


class KnowledgeSearchPage(BasePage):

    def test_default_fast_filter(self):
        web_elements_group_filter = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        list_filter = []
        for item in web_elements_group_filter:
            list_filter.append(item.text)
        assert "Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"'
        assert "Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"'
        # assert "Холдинги" in list_filter, 'Отсутствует блок фильтра "Холдинги"'
        assert "Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"'
        assert "Подразделение-исполнитель" in list_filter, 'Отсутствует блок фильтра "Подразделение-исполнитель"'
        assert "Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"'
        assert "Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"'

        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()
        web_elements_found = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FOUND_ELEMENT)
        list_found_element = []
        for item in web_elements_found:
            list_found_element.append(item.text)

    def test_filter_project(self):
        self.browser.find_element(*KnowledgeSearchLocators.PROJECT_CHECKBOX).click()
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Проект"
        web_elements_group_filter = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        list_filter = []
        for item in web_elements_group_filter:
            list_filter.append(item.text)
        assert "Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"'
        # assert "Год" in list_filter, 'Отсутствует блок фильтра "Год"'
        # assert "Наполнение для маркетинга" in list_filter, 'Отсутствует блок фильтра "Наполнение для маркетинга"'
        # assert "Интерес маркетинга к проекту" in list_filter, 'Отсутствует блок фильтра "Интерес маркетинга к проекту"'
        # assert "Холдинги" in list_filter, 'Отсутствует блок фильтра "Холдинги"'
        assert "Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"'
        assert "Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"'
        assert "Подразделение-исполнитель" in list_filter, 'Отсутствует блок фильтра "Подразделение-исполнитель"'
        assert "Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"'
        assert "Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"'

        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()

        # Проверяем фильтрацию по чек-боксу "Проект"
        web_elements_found = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FOUND_ELEMENT)
        list_found_element = []
        for item in web_elements_found:
            list_found_element.append(item.text)
        assert "ПРОЕКТ" in (set(list_found_element)), f'Отображены сущности {set(list_found_element)} ' \
                                                      f'\nОжидаемый результат: "Проект"'
        assert len(set(list_found_element)) == 1, "Отображены сущности не только категории Проект"

        # Деактивируем чек-бокс фильтрации по сущности "Проект"
        self.browser.find_element(*KnowledgeSearchLocators.PROJECT_CHECKBOX).click()

    def test_filter_contract(self):
        self.browser.find_element(*KnowledgeSearchLocators.CONTRACT_CHECKBOX).click()
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Договор/контракт"
        web_elements_group_filter = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        list_filter = []
        for item in web_elements_group_filter:
            list_filter.append(item.text)
        assert "Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"'
        assert "Стоимость проекта (руб.)" in list_filter, 'Отсутствует блок фильтра "Стоимость проекта (руб.)"'
        assert "Дата заключения" in list_filter, 'Отсутствует блок фильтра "Дата заключения"'
        assert "Дата завершения" in list_filter, 'Отсутствует блок фильтра "Дата завершения"'
        assert "Статус контракта" in list_filter, 'Отсутствует блок фильтра "Статус контракта"'
        assert "Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"'
        # assert "Холдинги" in list_filter, 'Отсутствует блок фильтра "Холдинги"'
        assert "Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"'
        assert "Подразделение-исполнитель" in list_filter, 'Отсутствует блок фильтра "Подразделение-исполнитель"'
        assert "Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"'
        assert "Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"'

        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()

        # Проверяем фильтрацию по чек-боксу "Договоры (контракты)"
        web_elements_found = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FOUND_ELEMENT)
        list_found_element = []
        for item in web_elements_found:
            list_found_element.append(item.text)
        assert "ДОГОВОР/КОНТРАКТ" in (set(list_found_element)), f'Отображены сущности {set(list_found_element)} ' \
                                                      f'\nОжидаемый результат: "Договор/Контракт"'
        assert len(set(list_found_element)) == 1, "Отображены сущности не только категории Договор/Контракт"

        # Деактивируем чек-бокс фильтрации по сущности "Договор/контракт"
        self.browser.find_element(*KnowledgeSearchLocators.CONTRACT_CHECKBOX).click()

    def test_filter_division(self):
        self.browser.find_element(*KnowledgeSearchLocators.DIVISION_CHECKBOX).click()
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Подразделение"
        web_elements_group_filter = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        list_filter = []
        for item in web_elements_group_filter:
            list_filter.append(item.text)
        assert len(list_filter) == 5, 'Отображены лишние категории фильтров для блока "Подразделение"'
        assert "Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"'
        assert "Заказчик" in list_filter, 'Отсутствует блок фильтра "Заказчик"'
        assert "Юр.лицо-исполнитель" in list_filter, 'Отсутствует блок фильтра "Юр.лицо-исполнитель"'
        assert "Тип работ и услуг" in list_filter, 'Отсутствует блок фильтра "Тип работ и услуг"'
        assert "Технологии" in list_filter, 'Отсутствует блок фильтра "Технологии"'

        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()

        # Проверяем фильтрацию по чек-боксу "Подразделение"
        web_elements_found = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FOUND_ELEMENT)
        list_found_element = []
        for item in web_elements_found:
            list_found_element.append(item.text)
        assert "ПОДРАЗДЕЛЕНИЕ" in (set(list_found_element)), f'Отображены сущности {set(list_found_element)} ' \
                                                      f'\nОжидаемый результат: "Подразделение"'
        assert len(set(list_found_element)) == 1, "Отображены сущности не только категории Подразделение"

        # Деактивируем чек-бокс фильтрации по сущности "Подразделение"
        self.browser.find_element(*KnowledgeSearchLocators.DIVISION_CHECKBOX).click()

    def test_filter_technology(self):
        self.browser.find_element(*KnowledgeSearchLocators.TECHNOLOGY_CHECKBOX).click()
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Подразделение"
        web_elements_group_filter = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        list_filter = []
        for item in web_elements_group_filter:
            list_filter.append(item.text)
        assert len(list_filter) == 1, 'Отображены лишние категории фильтров для блока "Технологии"'
        assert "Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"'

        """
        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()
            
        # Проверяем фильтрацию по чек-боксу "Технология"
        web_elements_found = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FOUND_ELEMENT)
        list_found_element = []
        for item in web_elements_found:
            list_found_element.append(item.text)
        assert "ТЕХНОЛОГИЯ" in (set(list_found_element)), f'Отображены сущности {set(list_found_element)} ' \
                                                             f'\nОжидаемый результат: "Подразделение"'
        assert len(set(list_found_element)) == 1, "Отображены сущности не только категории Подразделение"
        """

        # Деактивируем чек-бокс фильтрации по сущности "Технология"
        self.browser.find_element(*KnowledgeSearchLocators.TECHNOLOGY_CHECKBOX).click()

    def test_filter_legal(self):
        self.browser.find_element(*KnowledgeSearchLocators.LEGAL_CHECKBOX).click()
        time.sleep(1)

        # Проверяем отображаемые категории быстрых фильтров для сущности "Юр.лицо/ИП"
        web_elements_group_filter = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FAST_FILTER)
        list_filter = []
        for item in web_elements_group_filter:
            list_filter.append(item.text)
        assert len(list_filter) == 1, 'Отображены лишние категории фильтров для блока "Технологии"'
        assert "Нужно найти" in list_filter, 'Отсутствует блок фильтра "Нужно найти"'

        # Подгружаем весь список найденных сущностей
        while self.is_visibility_of_element_located(*KnowledgeSearchLocators.LOAD_MORE_BUTTON):
            self.browser.find_element(*KnowledgeSearchLocators.LOAD_MORE_BUTTON).click()

        # Проверяем фильтрацию по чек-боксу "Юр.лицо/ИП"
        web_elements_found = self.browser.find_elements(*KnowledgeSearchLocators.ALL_TITLE_IN_FOUND_ELEMENT)
        list_found_element = []
        for item in web_elements_found:
            list_found_element.append(item.text)
        assert "ЮР.ЛИЦО/ИП" in (set(list_found_element)), f'Отображены сущности {set(list_found_element)} ' \
                                                      f'\nОжидаемый результат: "Юр.лицо/ИП"'
        assert len(set(list_found_element)) == 1, "Отображены сущности не только категории Юр.лицо/ИП"

        # Деактивируем чек-бокс фильтрации по сущности "Юр.лицо/ИП"
        self.browser.find_element(*KnowledgeSearchLocators.LEGAL_CHECKBOX).click()



















