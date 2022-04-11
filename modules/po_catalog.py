from page_objects import PageElement, PageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CatalogPage(PageObject):
    span_producst_title = '//*[@id="header_container"]/div[2]/span'
    items = '//div[@class="inventory_item"]'
    button = '//*[@id="remove-sauce-labs-backpack"]'


    def is_on_catalog_page(self):
        return bool(self.wait_for_element_by_xpath(self.span_producst_title))


    def are_products_displayed(self):
        return bool(self.wait_for_element_by_xpath(self.items))
    
    
    def add_item_by_index(self, index):
        items = self.w.find_elements_by_xpath(By.XPATH, "")
        items[index].click()


    def get_first_item(self):
        return self.wait_for_element_by_xpath(self.items)

    def check_item_button(self, item_locator):
        
        
    
    def wait_for_element_by_xpath(self, element):
        wait = WebDriverWait(self.w, 5)
        try:
            element_found = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, element)
                )
            )
        except TimeoutException:
            return False
        if element_found:
            return element_found
