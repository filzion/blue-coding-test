from page_objects import PageElement, PageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class LoginPage(PageObject):
    input_username = PageElement(id_='user-name')
    input_password = PageElement(id_='password')
    button_login = PageElement(id_='login-button')

    def do_login(self, username, password):
        self.input_username.send_keys(username)
        self.input_password.send_keys(password)
        self.button_login.click()
