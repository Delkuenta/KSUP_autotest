import os


class UserData:
    # Значение пути в переменную для прикрепляемых файлов
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    name_jpg_to_link = 'test_jpg.jpg'
    name_doc_to_link = 'test_doc.docx'
    name_excel_to_link = 'test_excel.xlsx'
    name_mp4_to_link = 'test_video.mp4'
    # Путь для добавления файла в прикрепленные
    file_path_for_link_jpg = os.path.join(current_dir, name_jpg_to_link)
    file_path_for_link_doc = os.path.join(current_dir, name_doc_to_link)
    file_path_for_link_excel = os.path.join(current_dir, name_excel_to_link)
    file_path_for_link_mp4 = os.path.join(current_dir, name_mp4_to_link)


    link = "https://Mr_KSUP_Seller:AsdGhj-5681-Sle@ksup-tst.lanit/_trust"
    # УЗ для согласования, статичные.
    login_seller = [r"Lanit\Mr_KSUP_Seller", "AsdGhj-5681-Sle"]
    login_dir = [r"Lanit\Mr_KSUP_Dir", "AsdGhj-5681-Dri"]
    login_seller2 = [r"Lanit\Mr_KSUP_Seller2", "AsdGhj-5681-2Les"]
    login_dir2 = [r"Lanit\Mr_KSUP_Dir2", "AsdGhj-5681-2Rid"]
    login_legal = [r"Lanit\Mr_KSUP_Legal", "AsdGhj-5681-Lge"]
    login_count = [r"Lanit\Mr_KSUP_Count", "*AF5hcnEfF8D2g8a"]
    login_fin = [r"Lanit\Mr_KSUP_Fin", "AsdGhj-5681-Fni"]
    login_udprpo = [r"Lanit\Mr_KSUP_UDPRPO", "lPRvCNi9m9zU8gb"]
    login_kkp = [r"Lanit\Mr_KSUP_KKP", "su@rMpuYu{^}bOI5Z"]

    user_data_dict = {
        "fullName": "[АТест] ПА+ЗП+ДК, Тендер, категория Б, разработка ПО, Самостоятельная продажа",
        "contractorType": "Тендерная заявка",
        "customer": "КАЗНАЧЕЙСТВО РОССИИ",
        "salesUnit": "ОНЛАНТА",
        "salesManager": "Бравосов Андрей Игоревич",
        "executiveUnit": "ОНЛАНТА",
        "executiveManager": "Бравосов Андрей Игоревич",
        "executiveUnitLegal": "ООО \"ОНЛАНТА\"",
        "saleLawType": "44-ФЗ",
        "typeOfWorkServices": ["Разработка заказного ПО", "Тестирование ПО"],
        "sum": 642800,
        "currency": "Доллар",
        "applicationSize": "1000,00",
        "contractSize": "2000,00",
        "separateSale": "Да",
        "competitionDeadlineFrom": "15.07.2020",
        "startDate": "1.07.2020",
        "endDate": "01.07.2021",
        "projectProbability": 100,
        "descriptionText": "Краткое описание текст",
        "risksText": "Текст_риски_тест",
        "purchase_number": "ZP/0001-AT",
        "purchase_link": "testlink_zakup_proc.com",
        "project_risk_department": "тестовое сообщение_Риски проекта с точки зрения Департамента",
        "price_information_deadline": "16.07.2020",
        "purchase_start_date_from": "17.07.2020",
        "purchase_start_date_to": "18.07.2020",
        "eis_price_number": "ZP/0013-AT-Price",
        "eis_price_link": "example@link.com",
        "number_contract": "DK/0013-AT",
        "eis_contract_link": "test_link_eis@mail.com",
        "territory": "Архангельская область",
        "technologies": "Jira",
        "quantitative_indicators_project": "тестовый текст в поле Количественные показатели реализации проекта",
        "project_unique_code": "2hMuCr13",
        "payments": [
            {
                "sum": 200000,
                "year": 2020,
                "quarter": 3
            },
            {
                "sum": 100000,
                "year": 2020,
                "quarter": 4
            },
            {
                "sum": 700000,
                "year": 2021,
                "quarter": 1
            },
            {
                "sum": 200000,
                "year": 2021,
                "quarter": 2
            },
            {
                "sum": 72800,
                "year": 2021,
                "quarter": 3
            }


        ]
    }
