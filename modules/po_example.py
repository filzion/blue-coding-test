from page_objects import PageElement, PageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Example(PageObject):
    title = "G1 - O portal de notícias da Globo"

    banners = PageElement(xpath='//div[@class="bstn-hl-wrapper"]')

    def reached_home_page(self):
        return self.w.title == self.title

        

    def click_on_first_banner(self):
        clickable_banners = self.w.find_elements_by_xpath('//div[@class="bstn-hl-wrapper"]')
        clickable_banners[0].click()
