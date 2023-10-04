from behave import given, when, then


@then('Verify user is on Demo Drive page')
def user_verify_demo_page(context):
    context.app.model3_demo_page.user_verify_demo_page()