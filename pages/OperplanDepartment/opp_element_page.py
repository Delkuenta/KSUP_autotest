import time

from selenium.webdriver.support.color import Color

from pages.base_page import BasePage
from pages.locators import OpElementLocators


class OppElementPage(BasePage):

    def verify_element_in_operplan(self, year, type_element, user_data_dict):
        how, what = OpElementLocators.ROW_ELEMENT_IN_OPERPLAN
        what = what.replace("fullName", user_data_dict["fullName"])
        assert len(self.browser.find_elements(how, what)) > 0, \
            f'В оперплане отсутствует строчка сущности с названием {user_data_dict["fullName"]}'

        # Добавляем id строки оперплана в словарь сущности
        how, what = OpElementLocators.ROW_ELEMENT_IN_OPERPLAN
        what = what.replace("fullName", user_data_dict["fullName"])
        id_element = self.browser.find_element(how, what).get_attribute("id")
        id_dict = {"idElementInOpp": id_element}
        user_data_dict.update(id_dict)

        # Проверка значений в строке сущности ОП
        how, what = OpElementLocators.CUSTOMER_VALUE_IN_ROW
        what = what.replace("idElementInOpp", user_data_dict["idElementInOpp"])
        assert self.is_element_text(how, what) == user_data_dict["customer"], \
            f'Не корректная информация в поле "Заказчик" в строке сущности: "{user_data_dict["fullName"]}"'

        # Проверка значения в поле департамента
        how, what = OpElementLocators.EXECUTIVE_UNIT_IN_ROW
        what = what.replace("idElementInOpp", user_data_dict["idElementInOpp"])
        assert self.is_element_text(how, what) == user_data_dict["executiveUnit"], \
            f'Не корректная информация в поле "Департамент" в строке сущности: "{user_data_dict["fullName"]}"'

        # Проверка значения в поле "Дата заключения"
        how, what = OpElementLocators.START_DATE_IN_ROW
        what = what.replace("idElementInOpp", user_data_dict["idElementInOpp"])
        assert self.is_element_text(how, what) == user_data_dict["startDate"], \
            f'Не корректная информация в поле "Дата заключения" в строке сущности: "{user_data_dict["fullName"]}"'

        # Проверка значения в поле "Дата окончания"
        how, what = OpElementLocators.END_DATE_IN_ROW
        what = what.replace("idElementInOpp", user_data_dict["idElementInOpp"])
        assert self.is_element_text(how, what) == user_data_dict["endDate"], \
            f'Не корректная информация в поле "Дата окончания" в строке сущности: "{user_data_dict["fullName"]}"'

        # Вычисление суммы за год
        sum_per_year = 0
        count_payments_line = len(user_data_dict["payments"])
        current_line = 0
        while current_line < count_payments_line:
            if user_data_dict["payments"][current_line]["year"] == year:
                if user_data_dict["currency"] == "Доллар":
                    sum_in_rub = user_data_dict["payments"][current_line]["sum"] * 75
                    sum_per_year += sum_in_rub
                elif user_data_dict["currency"] == "Евро":
                    sum_in_rub = user_data_dict["payments"][current_line]["sum"] * 95
                    sum_per_year += sum_in_rub
                else:
                    sum_per_year += user_data_dict["payments"][current_line]["sum"]
            current_line += 1

        # Форматирование суммы
        sum_per_year_str = ('{:,d}'.format(sum_per_year)).replace(",", " ") + ' ₽'

        # Проверка значения в поле "Итого за год, руб."
        how, what = OpElementLocators.SUM_IN_ROW
        what = what.replace("idElementInOpp", user_data_dict["idElementInOpp"])
        assert self.is_element_text(how, what) == sum_per_year_str, \
            f'Не корректная информация в поле "Итого за год, руб." в строке сущности: "{user_data_dict["fullName"]}"'

        # Проверка значения в поле "Вероятность"(для сущности ДК всегда 100%)
        how, what = OpElementLocators.PROBABILITY_IN_ROW
        what = what.replace("idElementInOpp", user_data_dict["idElementInOpp"])
        if type_element == "presale":
            assert self.is_element_text(how, what) == str(user_data_dict["projectProbability"]) + "%", \
                f'Не корректная информация в поле "Вероятность" в строке сущности: "{user_data_dict["fullName"]}"' \
                f'ОР - {user_data_dict["projectProbability"]}' \
                f'ФР - "{self.is_element_text(how, what)}"'
        else:
            assert self.is_element_text(how, what) == "100%", \
                f'Не корректная информация в поле "Вероятность" в строке сущности: "{user_data_dict["fullName"]}"'

        # Проверка значения в поле "Итого за год с учетом вероятности, руб."
        if type_element == "presale":
            sum_per_year_with_probability = int(sum_per_year / 100 * user_data_dict["projectProbability"])
        else:
            sum_per_year_with_probability = sum_per_year

        # Форматирование суммы с учетом вероятности
        sum_per_year_with_probability_str = ('{:,d}'.format(sum_per_year_with_probability)).replace(",", " ") + ' ₽'
        how, what = OpElementLocators.SUM_PROBABILITY_IN_ROW
        what = what.replace("idElementInOpp", user_data_dict["idElementInOpp"])
        assert self.is_element_text(how, what) == sum_per_year_with_probability_str, \
            f'Не корректная информация в поле "Итого за год с учетом ' \
            f'вероятности, руб." в строке сущности: "{user_data_dict["fullName"]}"'

        # Проверка значения в поле "Номер договора/контракта"
        how, what = OpElementLocators.CONTRACT_NUMBER_IN_ROW
        what = what.replace("idElementInOpp", user_data_dict["idElementInOpp"])
        if type_element == "contract":
            assert self.is_element_text(how, what) == user_data_dict["numberContract"], \
                f'Не корректная информация в поле "Номер договора/контракта ' \
                f'вероятности, руб." в строке сущности: "{user_data_dict["fullName"]}"'
        else:
            assert self.browser.find_element(how, what).text == "", \
                f'Не корректная информация в поле "Номер договора/контракта ' \
                f'вероятности, руб." в строке сущности: "{user_data_dict["fullName"]}"'

    def go_to_update_operplan(self):
        self.browser.implicitly_wait(2)
        # Нажимаем кнопку "Обновить"
        self.browser.find_element(*OpElementLocators.UPDATE_OPERPLAN_BUTTON).click()

        # Ожидаем поиск измененых сущностей
        self.is_disappeared(*OpElementLocators.FIND_UPDATED_ELEMENT)

        # Активируем чек-бокс обновить все найденные новые сущности и измененные
        checkbox_activate_all = self.browser.find_elements(*OpElementLocators.ADD_ALL_ELEMENT)
        for element in checkbox_activate_all:
            element.click()

        # Жмем кнопку "Добавить в оперплан"
        self.browser.find_element(*OpElementLocators.CONFIRM_UPDATE_OPERPLAN).click()
        time.sleep(3)

    def verify_color_element(self, user_data_dict, color):
        color_dict = {"red": "#ff8080", "green": "#adebad", "gray": "#d9d9d9", "orange": "#ffb833"}
        # Добавляем id строки оперплана в словарь сущности
        how, what = OpElementLocators.ROW_ELEMENT_IN_OPERPLAN
        what = what.replace("fullName", user_data_dict["fullName"])
        id_element = self.browser.find_element(how, what).get_attribute("id")
        id_dict = {"idElementInOpp": id_element}
        user_data_dict.update(id_dict)

        # Проверяем цвет ячеек в строке
        how, what = OpElementLocators.ALL_FIELD_IN_ROW
        what = what.replace("idElementInOpp", user_data_dict["idElementInOpp"])

        list_all_field_in_row = self.browser.find_elements(how, what)

        for element in list_all_field_in_row:
            color_in_element = (Color.from_string(element.value_of_css_property('background-color'))).hex
            assert color_in_element == color_dict[color], \
                f'Не корректный цвет строки сущности {user_data_dict["fullName"]}'


