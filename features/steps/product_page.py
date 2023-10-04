from behave import given, when, then


@given('user navigates to {link_id}')
def Navigate_to_product_page(context, link_id):
    context.app.product_page.Navigate_to_product_page(link_id)


@then('verify all product components')
def user_sees_all_product_components(context):
    context.app.product_page.user_sees_all_product_components()


@then('verify all model3 product components are present')
def user_sees_all_model3_product_components(context):
    context.app.product_page.user_sees_all_model3_product_components()