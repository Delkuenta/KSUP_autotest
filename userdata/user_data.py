import codecs
import os
import time

class UserData:
    #name_file_for_user_data = 'Test1.1_Seller_PaZpDk_tender_catA_razrabPO.txt'
    name_file_to_link = 'test.jpg'
    # Скрипт для добавления файлов из текущей директории тестов
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path_for_link_file = os.path.join(current_dir, name_file_to_link)

    # Метод чтения переменных из файла txt
    #file_path_for_user_data = os.path.join(current_dir, name_file_for_user_data)
    #with codecs.open(file_path_for_user_data, 'r', encoding='utf-8') as f:
      # exec(f.read())

    link = "https://Mr_KSUP_Seller:AsdGhj-5681-Sle@ksup-tst.lanit/_trust"
    # УЗ для согласования, статичные.
    login_legal = ["Lanit\Mr_KSUP_Legal", "AsdGhj-5681-Lge"]
    login_count = ["Lanit\Mr_KSUP_Count", "*AF5hcnEfF8D2g8a"]
    login_fin = ["Lanit\Mr_KSUP_Fin", "AsdGhj-5681-Fni"]
    login_udprpo = ["Lanit\Mr_KSUP_UDPRPO", "lPRvCNi9m9zU8gb"]
    login_kkp = ["Lanit\Mr_KSUP_KKP", "su@rMpuYu{^}bOI5Z"]


    # Под какими УЗ создаем сущности?:
    login_for_create_presale = ["Lanit\Mr_KSUP_Seller", "AsdGhj-5681-Sle"]
    login_for_create_zakup = ["Lanit\Mr_KSUP_Seller", "AsdGhj-5681-Sle"]
    login_for_create_contract = ["Lanit\Mr_KSUP_Seller", "AsdGhj-5681-Sle"]

    # переменные для пресейловой активности. Запрос цен и услуг, категория А,разработка ПО, Самостоятельная продажа
    name_presale = "t2e1_тест_ПА_ЗапросЦен_самостПрод_катА"  # + str(time.time())
    type_presale = "Запрос цен товаров, работ, услуг"
    customer = "ООО \"МОНОЛИТ\""
    divisions_seller = "ОНЛАНТА"
    seller_responsible = "Бравосов Андрей Игоревич"
    division_performer = "ОНЛАНТА"
    performer_responsible = "Бравосов Андрей Игоревич"
    performer_legal = "ООО \"ОНЛАНТА\""
    sale_law_type = "44-ФЗ"
    group_category = "TIE_6"
    category = "Разработка заказного ПО"
    sum = 52000000
    currency = "Рубль"
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

    # переменные в закупочной процедуре, остальные предзаполняются из ПА
    name_zp_based_on_presale = "t2e2_тест_ЗП_ЗапросЦен_самостПрод_катА"
    price_information_deadline = "16.07.2020"  # только в ЗП запросе цен и услуг
    purchase_start_date_from = "17.07.2020"  # только в ЗП запросе цен и услуг
    purchase_start_date_to = "18.07.2020"  # только в ЗП запросе цен и услуг
    eis_price_number = "ZP/0003-AT-Price"
    eis_price_link = "example@link.com"
    project_risk_department = "тестовое сообщение_Риски проекта с точки зрения Департамента"

    # Переменные в форме создания Договор/контракт, остальные предзаполняются из ЗП и ПА
    name_contract_based_on_zakup = "t2e3_тест_ЗП_ЗапросЦен_самостПрод_катА"
    number_contract = "DK/0003-AT"
    purchase_number = "ZP/0003-AT"
    purchase_link = "testlink_zakup_proc.com"
    eis_contract_link = "test_link_eis@mail.com"
    group_territory = "TIE_3"
    territory = "Архангельская область"
    technologies = "Jira"
    quantitative_indicators_project = "тестовый текст в поле Количественные показатели реализации проекта"
    project_unique_code = "2hMuCr3"

    # Комментарии при согласовании и отклонении
    comment_approval_legal = "Успешное согласование за Юридическую службу"
    comment_approval_count = "Успешное согласование за Бухгалтерию"
    comment_approval_fin = "Успешное согласование за финансовую службу"
    comment_approval_udprpo = "Успешное согласование за УДПР ПО"
    comment_approval_kkp = "Успешное согласование за ККП"





