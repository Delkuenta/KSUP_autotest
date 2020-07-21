import codecs
import os

class UserData:
    #name_file = 'Presale_tender_catA_razrabPO.txt'
    # Скрипт для добавления файлов из текущей директории тестов
   # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    #file_path = os.path.join(current_dir, name_file)
    #with codecs.open(file_path, 'r', encoding='utf-8') as f:
       # exec(f.read())

    # переменные для пресейловой активности. Тендер, категория А,разработка ПО, Самостоятельная продажа
    name_presale = "t1e1_тест_ПА_тендер_самостПрод_катА"
    type_presale = "Тендерная заявка"
    customer = "ООО \"ДЕКОР\""
    divisions_seller = "ОНЛАНТА"
    division_performer = "ОНЛАНТА"
    performer_responsible = "Бравосов Андрей Игоревич"
    performer_legal = "ООО \"ОНЛАНТА\""
    sale_law_type = "44-ФЗ"
    group_category = "TIE_6"
    # TIE_6 = Программное обеспечение. LBL_7 = Cтроительство. LBL_5 = Обучение.
    # LBL_4 = Дистрибуция и ритейл. LBL_3 = Аппаратное обеспечение и инфраструктура
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