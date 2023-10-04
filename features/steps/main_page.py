from behave import given, when, then


@given('user navigate to homepage')
def user_nav_to_homepage(context):
    context.app.main_page.user_nav_to_homepage()


@when('user clicks on order now')
def user_clicks_on_order_now(context):
    context.app.main_page.user_clicks_on_order_now()


@when('user clicks on demo drive')
def user_clicks_on_demo_drive(context):
    context.app.main_page.user_clicks_on_demo_drive()


@when('clicks on explore inventory')
def user_clicks_on_inventory(context):
    context.app.main_page.user_clicks_on_inventory()


@when('scroll down the page to model 3')
def user_scroll_down(context):
    context.app.main_page.user_scroll_down()


@when('user clicks on Tesla Model 3 Demo Drive')
def user_clicks_on_Model3_Demo_page(context):
    context.app.main_page.user_clicks_on_Model3_Demo_page()


@then('user is taken to demo drive page')
def user_taken_to_demo_drive_page(context):
    context.app.main_page.user_taken_to_demo_drive_page()



