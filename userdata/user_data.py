import codecs
import os
import time

class UserData:
    #name_file_for_user_data = 'Test1_PaZpDk_tender_catA_razrabPO.txt'
    name_file_to_link = 'test.jpg'
    # Скрипт для добавления файлов из текущей директории тестов
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path_for_link_file = os.path.join(current_dir, name_file_to_link)

    # Метод чтения переменных из файла txt
   # file_path_for_user_data = os.path.join(current_dir, name_file_for_user_data)
    #with codecs.open(file_path_for_user_data, 'r', encoding='utf-8') as f:
    #    exec(f.read())

    # переменные для пресейловой активности. Тендер, категория А,разработка ПО, Самостоятельная продажа
    name_presale = "t1e1_тест_ПА_тендер_самостПрод_катА"  #+ str(time.time())
    type_presale = "Тендерная заявка"
    customer = "ООО \"ДЕКОР\""
    divisions_seller = "ОНЛАНТА"
    seller_responsible = "Бравосов Андрей Игоревич"
    division_performer = "ОНЛАНТА"
    performer_responsible = "Бравосов Андрей Игоревич"
    performer_legal = "ООО \"ОНЛАНТА\""
    sale_law_type = "44-ФЗ"
    group_category = "TIE_6"

    # -------------------------------------------------------------------------------
    # Подсказка при заполнении группы категории
    # TIE_6 = Программное обеспечение. LBL_7 = Cтроительство. LBL_5 = Обучение.
    # LBL_4 = Дистрибуция и ритейл. LBL_3 = Аппаратное обеспечение и инфраструктура
    # -------------------------------------------------------------------------------

    category = "Разработка заказного ПО"
    sum = 52000000
    currency = "Доллар"
    application_size = "1000"
    contract_size = "2000"
    separate_sale = "Да"
    competition_deadline_From = "15.07.2020"
    plan_date_contract_conclusion = "1.07.2020"
    plan_Date_contract_finish = "30.12.2020"
    project_probability = "100"
    description_plain_text = "Краткое описание текст"
    risks = "Текст_риски_тест"
    yeartable_1line = 2020
    yeartable_2line = 2020
    quarter_1line = "3 квартал"
    quarter_2line = "4 квартал"

    # переменные в закупочной процедуре(поля  отмеченнные # предзаполняются из ПА)
    name_zp_based_on_presale = "t1e2_тест_ЗП_тендер_самостПрод_катА"
    # type_presale = "Тендерная заявка"
    # divisions_seller = "ОНЛАНТА"
    # seller_responsible = "Бравосов Андрей Игоревич"
    # division_performer = "ОНЛАНТА"
    # performer_responsible = "Бравосов Андрей Игоревич"
    # customer = "ООО \"ДЕКОР\""
    # group_category = "TIE_6"

    # -------------------------------------------------------------------------------
    # Подсказка при заполнении группы категории
    # TIE_6 = Программное обеспечение. LBL_7 = Cтроительство. LBL_5 = Обучение.
    # LBL_4 = Дистрибуция и ритейл. LBL_3 = Аппаратное обеспечение и инфраструктура
    # -------------------------------------------------------------------------------

    # category = "Разработка заказного ПО"
    # performer_legal = "ООО \"ОНЛАНТА\""
    # sum = 52000000
    # currency = "Доллар"
    # sale_law_type = "44-ФЗ"
    # application_size = "1000"
    # contract_size = "2000"
    # competition_deadline_From = "15.07.2020"
    # plan_date_contract_conclusion = "1.07.2020"
    # plan_Date_contract_finish = "30.12.2020"
    # name_presale = "t1e1_тест_ПА_тендер_самостПрод_катА"
    # project_probability = "100"
    purchase_number = "ZP/0001-AT"
    purchase_link = "testlink_zakup_proc.com"
    # description_plain_text = "Краткое описание текст"
    project_risk_department = "тестовое сообщение_Риски проекта с точки зрения Департамента"

    # Переменные в форме создания Договор/контракт (поля  отмеченнные # предзаполняются из ПА и ЗП)
    name_contract_based_on_zakup = "t1e3_тест_ДК_тендер_самостПрод_катА"
    # customer = "ООО \"ДЕКОР\""
    # divisions_seller = "ОНЛАНТА"
    # seller_responsible = "Бравосов Андрей Игоревич"
    # division_performer = "ОНЛАНТА"
    # performer_responsible = "Бравосов Андрей Игоревич"
    # performer_legal = "ООО \"ОНЛАНТА\""
    # group_category = "TIE_6"

    # -------------------------------------------------------------------------------
    # Подсказка при заполнении группы категории
    # TIE_6 = Программное обеспечение. LBL_7 = Cтроительство. LBL_5 = Обучение.
    # LBL_4 = Дистрибуция и ритейл. LBL_3 = Аппаратное обеспечение и инфраструктура
    # -------------------------------------------------------------------------------

    # category = "Разработка заказного ПО"
    # sum = 52000000
    # currency = "Доллар"
    number_contract = "DK/0001-AT"
    eis_contract_link = "test_link_eis@mail.com"
    # competition_deadline_From = "15.07.2020"
    # plan_Date_contract_finish = "30.12.2020"
    # purchase_number = "ZP/0001-AT"
    # purchase_link = "testlink_zakup_proc.com"
    # name_presale = "t1e1_тест_ПА_тендер_самостПрод_катА"
    # name_zp_based_on_presale = "t1e2_тест_ЗП_тендер_самостПрод_катА"
    group_territory = "TIE_3"
    territory = "Архангельская область"
    technologies = "Microsoft Visual Studio"
    # description_plain_text = "Краткое описание текст"
    quantitative_indicators_project = "тестовый текст в поле Количественные показатели реализации проекта"
    project_unique_code = "2hMuCr"
    # yeartable_1line = 2020
    # eartable_2line = 2020
    # quarter_1line = "3 квартал"
    # quarter_2line = "4 квартал"

    # Комментарии при согласовании и отклонении
    comment_approval_legal = "Успешное согласование за Юридическую службу"
    comment_approval_count = "Успешное согласование за Бухгалтерию"
    comment_approval_fin = "Успешное согласование за финансовую службу"
    comment_approval_udprpo = "Успешное согласование за УДПР ПО"
    comment_approval_kkp = "Успешное согласование за ККП"

    # Комментарии при согласовании и отклоении Договор/Контракта