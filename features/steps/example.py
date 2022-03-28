from behave import given, when, then
from modules.po_example import Example


@given("step 1")
def function_name(context):
    pass


@given("step 2")
def function_name2(context):
    pass

@when("step 3")
def function_name3(context):
    exp = Example(context.driver)
    exp.po_function()


@then("step 4")
def function_name4(context):
    pass
