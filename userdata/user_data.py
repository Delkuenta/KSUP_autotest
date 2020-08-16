import json
import os


class UserData:
    # Группа файлов и их путей для прикрепления
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

    # Список категорий которые входят в группу "Программное обеспечение"
    group_software = ["Аутсорсинг разработки (включая аутстаффинг)",
                      "Внедрение готовых программных продуктов и решений (типа CRM, PLM)",
                      "Информационная безопасность в части ПО",
                      "Поддержка пользователей информационных систем",
                      "Поставка лицензий на ПО",
                      "Проектирование и иная разработка документации для ПО",
                      "Прочие работы и услуги в части ПО",
                      "Разработка заказного ПО",
                      "Тестирование ПО",
                      "Техническая поддержка ПО"]

    # Ссылка на ресурс
    link = "https://Mr_KSUP_Seller:AsdGhj-5681-Sle@ksup-tst.lanit/_trust"

    # Учетные записи, статичные.
    login_seller = [r"Lanit\Mr_KSUP_Seller", "AsdGhj-5681-Sle"]
    login_dir = [r"Lanit\Mr_KSUP_Dir", "AsdGhj-5681-Dri"]
    login_seller2 = [r"Lanit\Mr_KSUP_Seller2", "AsdGhj-5681-2Les"]
    login_dir2 = [r"Lanit\Mr_KSUP_Dir2", "AsdGhj-5681-2Rid"]
    login_legal = [r"Lanit\Mr_KSUP_Legal", "AsdGhj-5681-Lge"]
    login_count = [r"Lanit\Mr_KSUP_Count", "*AF5hcnEfF8D2g8a"]
    login_fin = [r"Lanit\Mr_KSUP_Fin", "AsdGhj-5681-Fni"]
    login_udprpo = [r"Lanit\Mr_KSUP_UDPRPO", "lPRvCNi9m9zU8gb"]
    login_kkp = [r"Lanit\Mr_KSUP_KKP", "su@rMpuYu{^}bOI5Z"]

    # Комментарии при согласовании и отклонении
    comment_approval_legal = "Успешное согласование за Юридическую службу"
    comment_approval_count = "Успешное согласование за Бухгалтерию"
    comment_approval_fin = "Успешное согласование за финансовую службу"
    comment_approval_udprpo = "Успешное согласование за УДПР ПО"
    comment_approval_kkp = "Успешное согласование за ККП"

    # Чтение json и присвоение словаря в переменную
    name_data_file = "[АТест_Seller] ПА+ЗП+ДК, Тендерная заявка, категория A, разработка заказного ПО, НЕсамостоятельная продажа.json"
    file_path_for_data = os.path.join(current_dir, name_data_file)
    with open(file_path_for_data, "r", encoding='utf-8') as file:
        data = json.load(file)
    user_data_dict = dict(data['main_data'])

