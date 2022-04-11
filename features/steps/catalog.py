from behave import given, when, then
from modules.po_login import LoginPage
from modules.po_catalog import CatalogPage
from time import sleep


@given("he is logged in")
def login(context):
    context.driver.get('https://www.saucedemo.com/')
    lp = LoginPage(context.driver)
    lp.do_login(context.username, context.password)


@given("he is on the catalog page")
def go_to_catalog_page(context):
    cp = CatalogPage(context.driver)
    assert cp.is_on_catalog_page()


@given("there are products on the page")
def check_if_products(context):
    cp = CatalogPage(context.driver)
    assert cp.are_products_displayed()
    # exp = Example(context.driver)
    # exp.po_function()


@given('The "{button}" button should appear for the first item')
def check_button(context, button):
    cp = CatalogPage(context.driver)
    first_item = cp.get_first_item()
    displayed_button = cp.check_item_button(first_item)
    import ipdb; ipdb.sset_trace()
    # assert displayed_button == button
