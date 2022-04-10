from behave import given, when, then
from modules.po_example import Example
from time import sleep


@given("I'm on google home page")
def function_name(context):
    context.driver.get("https://www.google.com")
    sleep(3)


@when('I search for "{text}"')
def function_name2(context, text):
    exp = Example(context.driver)
    exp.type_on_search(text)
    exp.click_on_search()

@when("step 3")
def function_name3(context):
    sleep(4)
    # exp = Example(context.driver)
    # exp.po_function()
