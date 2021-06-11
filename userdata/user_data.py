import json
import os


class UserData:

    user_account = {r"Mr_KSUP_Seller": "AsdGhj-5681-Sle",
                    r"Mr_KSUP_Dir": "AsdGhj-5681-Dri",
                    r"Mr_KSUP_Seller2": "AsdGhj-5681-2Les",
                    r"Mr_KSUP_Dir2": "AsdGhj-5681-2Rid",
                    r"Mr_KSUP_Legal": "AsdGhj-5681-Lge",
                    r"Mr_KSUP_Count": "*AF5hcnEfF8D2g8a",
                    r"Mr_KSUP_Fin": "AsdGhj-5681-Fni",
                    r"Mr_KSUP_UDPRPO": "lPRvCNi9m9zU8gb",
                    r"Mr_KSUP_KKP": "su@rMpuYu{^}bOI5Z",
                    r"Mr_KSUP_Admin": "AsdGhj-2038-dAm",
                    r"Mr_KSUP_LegalDir": "D7udLkntip{!}8tav",
                    r"sa_dks_ksup_audit": "zTpILFRgPyVFP{!}e",
                    r"sa_KSUP_Admin": "erNui-72004ixghi",
                    r"Mr_KSUP_Res": "AsdGhj-5681-Rse"}

    # Группа файлов и их путей для прикрепления
    # Значение пути в переменную для прикрепляемых файлов
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    name_jpg_to_link = 'test_jpg.jpg'
    name_doc_to_link = 'test_doc.docx'
    name_excel_to_link = 'test_excel.xlsx'
    name_mp4_to_link = 'test_video.mp4'
    name_pdf_to_link = 'test_pdf.pdf'
    user_file_to_link = 'Служебная записка 26.03.21.docx'
    # Путь для добавления файла в прикрепленные
    file_path_for_link_jpg = os.path.join(current_dir, name_jpg_to_link)
    file_path_for_link_doc = os.path.join(current_dir, name_doc_to_link)
    file_path_for_link_excel = os.path.join(current_dir, name_excel_to_link)
    file_path_for_link_mp4 = os.path.join(current_dir, name_mp4_to_link)
    file_path_for_link_pdf = os.path.join(current_dir, name_pdf_to_link)
    file_path_fo_link_userfile = os.path.join(current_dir, user_file_to_link)

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

    # Комментарии при согласовании и отклонении
    comment_approval_depatment_head = "Успешное согласование за руководителя подразделения"
    comment_approval_egrul_head = "Успешное согласование за руководителя юр.лица/ИП"
    comment_approval_legal = "Успешное согласование за Юридическую службу"
    comment_approval_count = "Успешное согласование за Бухгалтерию"
    comment_approval_fin = "Успешное согласование за финансовую службу"
    comment_approval_udprpo = "Успешное согласование за УДПР ПО"
    comment_approval_kkp = "Успешное согласование за ККП"
    comment_approval_audit = "Успешное согласование за службу внутреннего аудита и контроля"
    comment_reject_depatment_head = "Отклонение сущности за руководителя подразделения"
    comment_reject_egrul_head = "Отклонение сущности за руководителя юр.лица/ИП"
    comment_reject_legal = "Отклонение сущности за Юридическую службу"
    comment_reject_count = "Отклонение сущности за Бухгалтерию"
    comment_reject_fin = "Отклонение сущности за финансовую службу"
    comment_reject_udprpo = "Отклонение сущности за УДПР ПО"
    comment_reject_kkp = "Отклонение сущности за ККП"
    comment_reject_audit = "Отклонение сущности за службу внутреннего аудита и контроля"
    comment_escalation_kkp = "Эскалирование сущности на ККП"
    comment_revision_kkp = "Отправка на доработку создателю сущности"
    comment_reject_presale_with_sales = "Отклонение сущности Пресейловая активность в качестве Продавца"
    comment_reject_presale_with_executive = "Отклонение сущности Пресейловая активность в качестве Исполнителя"
    comment_withdraw = "Отзыв сущности"

    egrulHead = {"Mr_KSUP_Dir": 'ООО \"ЗЛЫЕ МАРСИАНЕ\"',
                 "Mr_KSUP_Dir2": "",
                 "Mr_KSUP_LegalDir": 'ООО \"НУЖНО БОЛЬШЕ ЗОЛОТА\"'}

