from behave import given, when, then


@given("I am on Login page")
def open_login_page(context):
    context.app.launch_page.login_with_existing_account()


@when("I login to account")
def login_with_email_and_password(context):
    context.app.login_page.login_with_email_and_password()


@then("I shall land on account home page dashboard")
def verify_main_page_open(context):
    context.app.main_page.verify_main_page_is_open()
