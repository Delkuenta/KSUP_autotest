import codecs
import os
import time

class UserData:
    name_file_for_user_data = 'Test3_Seller2_PaZpDk_tender_catA_razrabPO.txt'
    name_file_to_link = 'test.jpg'
    # Скрипт для добавления файлов из текущей директории тестов
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path_for_link_file = os.path.join(current_dir, name_file_to_link)

    # Метод чтения переменных из файла txt
    file_path_for_user_data = os.path.join(current_dir, name_file_for_user_data)
    with codecs.open(file_path_for_user_data, 'r', encoding='utf-8') as f:
       exec(f.read())
