from behave import given, when, then


@given('user nagigates to {site_id}')
def user_nav_to_link(context, site_id):
    context.app.model3_inv_page.user_nav_to_link(site_id)


@when('add zipcode {zip_id}')
def user_add_zipcode(context, zip_id):
    context.app.model3_inv_page.user_add_zipcode(zip_id)


@then('verify that user sees to')
def user_sees_model3_title(context):
    context.app.model3_inv_page.user_sees_model3_title()