import codecs
import os
import time

class UserData:
    name_file_for_user_data = 'Test1_tender_Seller_PaZpDk_catA_razrabPO.txt'
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