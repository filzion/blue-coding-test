from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def before_all(context):
    context.username = context.config.userdata.get("username")
    context.password = context.config.userdata.get("password")

    chrome_options = Options()

    context.driver = Chrome(chrome_options=chrome_options)
    context.driver.maximize_window()
    


def after_all(context):
    context.driver.quit()
