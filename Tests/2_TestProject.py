import pytest

from pages.base_page import BasePage
from pages.login_data import LoginData
from pages.Project.project_create_form_page import ProjectFormCreate
from pages.Project.project_element_page import ProjectElementPage
from pages.Project.project_list_page import ProjectPage


# 2_[Atest_Dir] Project_required fields, categoryA, softwareDev.json
# 1_[Atest_Dir] Project, categoryA, softwareDev.json
# TestProject.json
# TestProject2.json

@pytest.mark.parametrize('path_data_file',
                         [r"PPAC\2_Project\TestProject.json"])
class TestProject:

    def test_create_project(self, browser_function, path_data_file):
        user_data_dict = BasePage.read_file_json(browser_function, path_data_file)
        print(user_data_dict)
        link = LoginData.link
        login_page = LoginData(browser_function, link)
        login_page.open()
        login_page.login(user_data_dict["createAccount"])
        login_page.verify_username(user_data_dict["createAccount"])
        login_page.go_to_project_list(link)
        project_list_page = ProjectPage(browser_function, link)
        project_list_page.go_to_create_project()
        project_create_page = ProjectFormCreate(browser_function, link)
        project_create_page.form_create_project(user_data_dict)
        project_element_page = ProjectElementPage(browser_function, link)
        project_element_page.verify_general_information_in_project(user_data_dict)
