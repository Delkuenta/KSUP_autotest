import time

from pages.base_page import BasePage
from pages.locators import ProjectElementLocators


def converting_values_to_strings(list_values):
    converted_string = ""
    for element in list_values:
        converted_string = converted_string + element + "; "
    converted_string = converted_string[0:(len(converted_string) - 2)]
    return converted_string


class ProjectElementPage(BasePage):

    def verify_general_information_in_project(self, user_data_dict):

        # Назначем неявное ожидание в этом методе
        self.browser.implicitly_wait(0)

        # Проверяем отображение кнопки "Показать подробную информацию" при открытии проекта
        assert self.is_element_text(*ProjectElementLocators.SLIDE_CONTENT_ELEMENT) == "Показать подробную информацию о проекте",  \
            "При открытии проекта должна отображаться краткая информация"

        # Проверяем отображение полей в кратком списке полей
        assert self.browser.find_element(*ProjectElementLocators.CUSTOMER_VALUE).is_displayed(), \
            'Поле "Заказчики" не отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.INDUSTRY_VALUE).is_displayed(), \
            'Поле "Отрасль" не отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.WORK_SERVICES_TYPE_VALUE).is_displayed(), \
            'Поле "Тип работ и услуг" не отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.PERFOMER_DIVISION_VALUE).is_displayed(), \
            'Поле "Исполнитель основной" не отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.PROJECT_STAGE_VALUE).is_displayed(), \
            'Поле "Стадия проекта" не отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.RP_LANIT_VALUE).is_displayed(), \
            'Поле "Контактное лицо от ЛАНИТ" не отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.TERRITORY_VALUE).is_displayed(), \
            'Поле "Территория применения" не отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.TECHNOLOGIES_VALUE).is_displayed(), \
            'Поле "Технологии" не отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.PERFORMER_LEGAL_VALUE).is_displayed() is False, \
            'Поле "Исполнитель (юридическое лицо)" отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.PERFOMER_DIVISIONS_VALUE).is_displayed() is False, \
            'Поле "Соисполнители" отображено в краткой информации'

        if len(user_data_dict["contracts"]) > 0:
            assert self.browser.find_element(*ProjectElementLocators.CONTRACTS_VALUE).is_displayed() is False, \
                'Поле "Связанные договоры/контракты" отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.START_DATE_VALUE).is_displayed() is False, \
            'Поле "Срок начала" отображено в краткой информации'

        if len(user_data_dict["vendors"]) > 0:
            assert self.browser.find_element(*ProjectElementLocators.VENDORS_VALUE).is_displayed() is False, \
                'Поле "Вендоры" отображено в краткой информации'

        if len(user_data_dict["tags"]) > 0:
            assert self.browser.find_element(*ProjectElementLocators.TAGS_VALUE).is_displayed() is False, \
                'Поле "Теги" отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.MANAGERS_PROJECT_VALUE).is_displayed() is False, \
            'Поле "Менеджеры проекта" отображено в краткой информации'

        if len(user_data_dict["endDate"]) > 0:
            assert self.browser.find_element(*ProjectElementLocators.END_DATE_VALUE).is_displayed() is False, \
                'Поле "Дата реализации" отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.SUM_VALUE).is_displayed() is False, \
            'Поле "Сумма по всем договорам/контрактам" отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.PROJECT_CATEGORY_VALUE).is_displayed() is False, \
            'Поле "Категория" отображено в краткой информации'

        assert self.browser.find_element(*ProjectElementLocators.SERVICES_VALUE).is_displayed() is False, \
            'Поле "Цели и задачи" отображено в краткой информации'

        if len(user_data_dict["quantitativeIndicatorsProject"]) > 0:
            assert self.browser.find_element(*ProjectElementLocators.PROJECT_RESULT_VALUE).is_displayed() is False, \
                'Поле "Ожидаемые результаты проекта" отображено в краткой информации'

        if len(user_data_dict["interestInformation"]) > 0:
            assert self.browser.find_element(*ProjectElementLocators.INTEREST_INFORMATION_VALUE).is_displayed() is False, \
                'Поле "Информация о заинтересованности" отображено в краткой информации'

        if len(user_data_dict["description"]) > 0:
            assert self.browser.find_element(*ProjectElementLocators.DESCRIPTION_VALUE).is_displayed() is False, \
                'Поле "Описание" отображено в краткой информации'

        # Жмем кнопку "Показать подробную информацию о проекте"
        self.browser.find_element(*ProjectElementLocators.SLIDE_CONTENT_ELEMENT).click()
        time.sleep(2)

        # Проверяем отображение кнопки "Показать подробную информацию" при открытии проекта
        assert self.is_element_text(*ProjectElementLocators.SLIDE_CONTENT_ELEMENT) == "Скрыть подробную информацию о проекте",  \
            'При развороте полной информации должна быть отображена кнопка "Скрыть подробную информацию о проекте"'

        # Проверяем название в титуле
        assert self.is_element_text(*ProjectElementLocators.TITLE_VALUE) == user_data_dict["fullName"], \
            f'Некорректное значение в Титула карточки сущности \n ' \
            f'Ожидаемый результат: {user_data_dict["fullName"]}\n ' \
            f'Фактический результат:{self.is_element_text(*ProjectElementLocators.TITLE_VALUE)}'

        # Проверяем значение в поле "Заказчики"
        customers_str = converting_values_to_strings(user_data_dict["customer"])
        assert self.is_element_text(*ProjectElementLocators.CUSTOMER_VALUE) == customers_str, \
            f'Некорректное значение в поле "Заказчики".\n ' \
            f'Ожидаемый результат: {customers_str}\n ' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.CUSTOMER_VALUE)}'

        # Проверяем значение в поле "Отрасль"
        industry_str = converting_values_to_strings(user_data_dict["industry"])
        assert self.is_element_text(*ProjectElementLocators.INDUSTRY_VALUE) == industry_str, \
            f'Некорректное значение в поле "Отрасль".\n ' \
            f'Ожидаемый результат: {industry_str}\n ' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.INDUSTRY_VALUE)}'

        # Проверяем значение в поле "Тип работ и услуг"
        typeOfWorkServices_str = converting_values_to_strings(user_data_dict["typeOfWorkServices"])
        assert self.is_element_text(*ProjectElementLocators.WORK_SERVICES_TYPE_VALUE) == typeOfWorkServices_str, \
            f'Некорректное значение в поле "Тип работ и услуг".\n ' \
            f'Ожидаемый результат: {typeOfWorkServices_str}\n ' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.WORK_SERVICES_TYPE_VALUE)}'

        # Проверяем значение в поле "Исполнитель основной"
        assert self.is_element_text(*ProjectElementLocators.PERFOMER_DIVISION_VALUE) == user_data_dict["executiveUnit"], \
            f'Некорректное значение в поле "Исполнитель основной".\n ' \
            f'Ожидаемый результат: {user_data_dict["executiveUnit"]}\n ' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.PERFOMER_DIVISION_VALUE)}'

        # Проверяем значение в поле "Стадия проекта"
        assert self.is_element_text(*ProjectElementLocators.PROJECT_STAGE_VALUE) == user_data_dict["projectStage"], \
            f'Некорректное значение в поле "Стадия проекта".\n ' \
            f'Ожидаемый результат: {user_data_dict["projectStage"]}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.PROJECT_STAGE_VALUE)}'

        # Проверяем значение в поле "Контактное лицо от ЛАНИТ"
        rp_lanit_str = user_data_dict["rpLanit"]
        rp_lanit_str = rp_lanit_str.replace("@LANIT", "")
        assert self.is_element_text(*ProjectElementLocators.RP_LANIT_VALUE) == rp_lanit_str, \
            f'Некорректное значение в поле "Контактное лицо от ЛАНИТ".\n ' \
            f'Ожидаемый результат: {rp_lanit_str}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.RP_LANIT_VALUE)}'

        # Проверяем значение в поле "Территория применения"
        territory_str = converting_values_to_strings(user_data_dict["territory"])
        assert self.is_element_text(*ProjectElementLocators.TERRITORY_VALUE) == territory_str, \
            f'Некорректное значение в поле "Территория применения".\n ' \
            f'Ожидаемый результат: {territory_str}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.TERRITORY_VALUE)}'

        # Проверяем значение в поле "Технологии"
        technologies_str = converting_values_to_strings(user_data_dict["technologies"])
        assert self.is_element_text(*ProjectElementLocators.TECHNOLOGIES_VALUE) == technologies_str, \
            f'Некорректное значение в поле "Технологии".\n ' \
            f'Ожидаемый результат: {technologies_str}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.TECHNOLOGIES_VALUE)}'

        # Проверяем значение в поле "Исполнитель (юридическое лицо)"
        assert self.is_element_text(*ProjectElementLocators.PERFORMER_LEGAL_VALUE) == user_data_dict["executiveUnitLegal"], \
            f'Некорректное значение в поле "Исполнитель (юридическое лицо)".\n ' \
            f'Ожидаемый результат: {user_data_dict["executiveUnitLegal"]}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.PERFORMER_LEGAL_VALUE)}'

        # Проверяем значение в поле "Соисполнители"
        if len(user_data_dict["salesUnit"]) > 0:
            salesUnit_str = converting_values_to_strings(user_data_dict["salesUnit"])
            assert self.is_element_text(*ProjectElementLocators.PERFOMER_DIVISIONS_VALUE) == salesUnit_str,\
                f'Некорректное значение в поле "Соисполнители".\n ' \
                f'Ожидаемый результат: {user_data_dict["salesUnit"]}\n' \
                f'Фактический результат: {self.is_element_text(*ProjectElementLocators.PERFOMER_DIVISIONS_VALUE)}'
        else:
            assert self.browser.find_element(*ProjectElementLocators.PERFOMER_DIVISIONS_VALUE).is_displayed() is False, \
                'Отображено пустое поле "Соисполнители"'

        # Проверяем значение в поле "Связанные договоры/контракты"
        if len(user_data_dict["contracts"]) > 0:
            contacts_str = ""
            for element in user_data_dict["contracts"]:
                contacts_str = contacts_str + element + "\n"
            contacts_str = contacts_str.strip()
            assert self.is_element_text(*ProjectElementLocators.CONTRACTS_VALUE) == contacts_str, \
                f'Некорректное значение в поле "Связанные договоры/контракты".\n' \
                f'Ожидаемый результат: {contacts_str}\n' \
                f'Фактический результат: {self.is_element_text(*ProjectElementLocators.CONTRACTS_VALUE)}'
        else:
            assert len(self.browser.find_elements(*ProjectElementLocators.CONTRACTS_VALUE)) == 0, \
                'Отображено пустое поле "Связанные договоры/контракты"'

        # Проверяем значение в поле "Срок начала"
        assert self.is_element_text(*ProjectElementLocators.START_DATE_VALUE) == user_data_dict["startDate"], \
            f'Некорректное значение в поле "Срок начала".\n' \
            f'Ожидаемый результат: {user_data_dict["startDate"]}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.START_DATE_VALUE)}'
        
        # Проверяем значение в поле "Вендоры"
        if len(user_data_dict["vendors"]) > 0:
            vendors_str = converting_values_to_strings(user_data_dict["vendors"])
            assert self.is_element_text(*ProjectElementLocators.VENDORS_VALUE) == vendors_str, \
                f'Некорректное значение в поле "Вендоры".\n ' \
                f'Ожидаемый результат: {vendors_str}\n' \
                f'Фактический результат: {self.is_element_text(*ProjectElementLocators.VENDORS_VALUE)}'
        else:
            assert len(self.browser.find_elements(*ProjectElementLocators.VENDORS_VALUE)) == 0, \
                'Отображено пустое поле "Вендоры"'

        # Проверяем поле "Теги"
        if len(user_data_dict["tags"]) > 0:
            tags_str = converting_values_to_strings(user_data_dict["tags"])
            assert self.is_element_text(*ProjectElementLocators.TAGS_VALUE) == tags_str, \
                f'Некорректное значение в поле "Теги".\n ' \
                f'Ожидаемый результат: {tags_str}\n' \
                f'Фактический результат: {self.is_element_text(*ProjectElementLocators.TAGS_VALUE)}'
        else:
            assert len(self.browser.find_elements(*ProjectElementLocators.TAGS_VALUE)) == 0, \
                'Отображено пустое поле "Теги"'

        # Проверяем поле "Менеджеры проекта"
        manager_str = converting_values_to_strings(user_data_dict["salesManager"])
        assert self.is_element_text(*ProjectElementLocators.MANAGERS_PROJECT_VALUE) == manager_str, \
            f'Некорректное значение в поле "Менеджеры проекта".\n ' \
            f'Ожидаемый результат: {manager_str}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.MANAGERS_PROJECT_VALUE)}'

        # Проверяем поле "Срок реализации"
        if len(user_data_dict["endDate"]) > 0:
            assert self.is_element_text(*ProjectElementLocators.END_DATE_VALUE) == user_data_dict["endDate"], \
                f'Некорректное значение в поле "Срок реализации".\n ' \
                f'Ожидаемый результат: {user_data_dict["endDate"]}\n' \
                f'Фактический результат: {self.is_element_text(*ProjectElementLocators.END_DATE_VALUE)}'
        else:
            assert len(self.browser.find_elements(*ProjectElementLocators.END_DATE_VALUE)) == 0, \
                'Отображено пустое поле "Срок реализации"'

        # Проверяем поле "Сумма по всем договорам/контрактам"
        assert self.is_element_text(*ProjectElementLocators.SUM_VALUE) == user_data_dict["sum"], \
            f'Некорректное значение в поле "Сумма по всем договорам/контрактам".\n ' \
            f'Ожидаемый результат: {user_data_dict["sum"]}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.SUM_VALUE)}'

        # Проверяем поле "Категория"
        assert self.is_element_text(*ProjectElementLocators.PROJECT_CATEGORY_VALUE) == user_data_dict["projectCategory"], \
            f'Некорректное значение в поле "Категория".\n ' \
            f'Ожидаемый результат: {user_data_dict["projectCategory"]}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.PROJECT_CATEGORY_VALUE)}'

        # Проверяем поле "Цели и задачи"
        assert self.is_element_text(*ProjectElementLocators.SERVICES_VALUE) == user_data_dict["descriptionText"], \
            f'Некорректное значение в поле "Цели и задачи".\n ' \
            f'Ожидаемый результат: {user_data_dict["descriptionText"]}\n' \
            f'Фактический результат: {self.is_element_text(*ProjectElementLocators.SERVICES_VALUE)}'

        # Проверяем поле "Ожидаемые результаты проекта"
        if len(user_data_dict["quantitativeIndicatorsProject"]) > 0:
            assert self.is_element_text(*ProjectElementLocators.PROJECT_RESULT_VALUE) == user_data_dict["quantitativeIndicatorsProject"], \
                f'Некорректное значение в поле "Ожидаемые результаты проекта".\n ' \
                f'Ожидаемый результат: {user_data_dict["quantitativeIndicatorsProject"]}\n' \
                f'Фактический результат: {self.is_element_text(*ProjectElementLocators.PROJECT_RESULT_VALUE)}'
        else:

            assert len(self.browser.find_elements(*ProjectElementLocators.PROJECT_RESULT_VALUE)) == 0, \
                'Отображено пустое поле "Ожидаемые результаты проекта"'

        # Проверяем поле "Информация о заинтересованности"
        if len(user_data_dict["interestInformation"]) > 0:
            assert self.is_element_text(*ProjectElementLocators.INTEREST_INFORMATION_VALUE) == user_data_dict["interestInformation"], \
                f'Некорректное значение в поле "Информация о заинтересованности".\n ' \
                f'Ожидаемый результат: {user_data_dict["interestInformation"]}\n' \
                f'Фактический результат: {self.is_element_text(*ProjectElementLocators.INTEREST_INFORMATION_VALUE)}'
        else:
            assert len(self.browser.find_elements(*ProjectElementLocators.INTEREST_INFORMATION_VALUE)) == 0, \
                'Отображено пустое поле "Информация о заинтересованности"'

        # Проверяем поле "Описание"
        if len(user_data_dict["description"]) > 0:
            assert self.is_element_text(*ProjectElementLocators.DESCRIPTION_VALUE) == user_data_dict["description"], \
                f'Некорректное значение в поле "Информация о заинтересованности".\n ' \
                f'Ожидаемый результат: {user_data_dict["description"]}\n' \
                f'Фактический результат: {self.is_element_text(*ProjectElementLocators.DESCRIPTION_VALUE)}'
        else:
            assert len(self.browser.find_elements(*ProjectElementLocators.DESCRIPTION_VALUE)) == 0, \
                'Отображено пустое поле "Информация о заинтересованности"'
