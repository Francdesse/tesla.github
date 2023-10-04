from behave import given, when, then


@given('user nagigates to {site_id}')
def user_nav_to_link(context, site_id):
    context.app.model3_inv_page.user_nav_to_link(site_id)


@when('add zipcode {zip_id}')
def user_add_zipcode(context, zip_id):
    context.app.model3_inv_page.user_add_zipcode(zip_id)

@when('user hover over model')
def user_hover_over_first_option(context):
    context.app.model3_inv_page.user_hover_over_first_option()


@then('verify that user sees {expected_result}')
def user_sees_model3_title(context, expected_result):
    context.app.model3_inv_page.user_sees_model3_title(expected_result)


@when('user clicks on first product listed')
def user_clicks_on_first_model3(context):
    context.app.model3_inv_page.user_clicks_on_first_model3()

@when('store original window')
def storing_original_window(context):
    context.app.model3_inv_page.storing_original_window()


@when('switching to Tesla Model 3 product page')
def model3_opens_to_new_page(context):
    context.app.model3_inv_page.model3_opens_to_new_page()


@then('close the Model 3 product page')
def closing_model3_product_page(context):
    context.app.model3_inv_page.closing_model3_product_page()


@then('switch back to the inventory page')
def switching_back_to_inv_page(context):
    context.app.model3_inv_page.switching_back_to_inv_page()
