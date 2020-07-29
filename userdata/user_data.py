import codecs
import os
import time

class UserData:
    name_file_for_user_data = 'Test13_zaprocCen_Seller_PaZp_Dk_catA_razrabPO.txt'
    name_file_to_link = 'test.jpg'
    # Скрипт для добавления файлов из текущей директории тестов
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path_for_link_file = os.path.join(current_dir, name_file_to_link)

    # Метод чтения переменных из файла txt
    file_path_for_user_data = os.path.join(current_dir, name_file_for_user_data)
    with codecs.open(file_path_for_user_data, 'r', encoding='utf-8') as f:
       exec(f.read())

    link = "https://Mr_KSUP_Seller:AsdGhj-5681-Sle@ksup-tst.lanit/_trust"
    # УЗ для согласования, статичные.
    login_legal = ["Lanit\Mr_KSUP_Legal", "AsdGhj-5681-Lge"]
    login_count = ["Lanit\Mr_KSUP_Count", "*AF5hcnEfF8D2g8a"]
    login_fin = ["Lanit\Mr_KSUP_Fin", "AsdGhj-5681-Fni"]
    login_udprpo = ["Lanit\Mr_KSUP_UDPRPO", "lPRvCNi9m9zU8gb"]
    login_kkp = ["Lanit\Mr_KSUP_KKP", "su@rMpuYu{^}bOI5Z"]

    # -------------------------------------------------------------

    # Под какими УЗ создаем сущности?:
    login_for_create_presale = ["Lanit\Mr_KSUP_Seller", "AsdGhj-5681-Sle"]

    # переменные для пресейловой активности. Тендер, категория А,разработка ПО, Самостоятельная продажа
    name_presale = "Тест Seller Одиночная Пресейловая активность, тип: Тендер, категория А, НЕ самостоятельная продажа"  # + str(time.time())
    type_presale = "Тендерная заявка"
    customer = "ООО \"МОНОЛИТ\""
    divisions_seller = "Дирекция по работе с государственным сектором"
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
    separate_sale = "Нет"
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