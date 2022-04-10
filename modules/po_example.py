from page_objects import PageElement, PageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



class Example(PageObject):
    search_bar_xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    search_button_xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]"
    
    search_bar = PageElement(xpath=search_bar_xpath)
    search_button = PageElement(xpath=search_button_xpath)
    results = PageElement(id_="result-stats")
    
    def type_on_search(self, text): 
        wait = WebDriverWait(self.w, 5)
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.search_bar_xpath)
            )
        )
        self.search_bar.send_keys(text)
    
    def click_on_search(self):
        wait = WebDriverWait(self.w, 5)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.search_button_xpath)
            )
        )
        self.search_button.click()
