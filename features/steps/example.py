from behave import given, when, then
from modules.po_example import Example
from time import sleep


@given("step 1")
def function_name(context):
    context.driver.get("http://www.g1.globo.com")
    exp=Example(context.driver)
    assert exp.reached_home_page()


@given("step 2")
def function_name2(context):
    pass

@when("step 3")
def function_name3(context):
    exp = Example(context.driver)
    a = exp.click_on_first_banner()


@then("step 4")
def function_name4(context):
    sleep(5)
