from page_objects import PageElement, PageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Example(PageObject):
    element_example = PageElement(id_='id_of_element')

    def po_function(self):
        pass
