from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MODEL3INVENTORYPAGE(Page):

    MODEL3_INV_PAGE = (By.XPATH, "//article[@class='result card' and @data-id='278_b8af95e46257142c4f98bda77492ad1c-search-result-container']//h3[@class='tds-text--h4']")
                       #"//article[@data-id='278_fa63d9fe83302f6484f589f28937991b-search-result-container']//h3[@class='tds-text--h4']")
                       #'[data-id="278_fa63d9fe83302f6484f589f28937991b-search-result-container"] h3')
    ZIP_ID_BOX = (By.CSS_SELECTOR, '.tds-form-input [data-id="registration-postal-code-textbox"]')

    def user_nav_to_link(self, site_id):
        self.open_url(site_id)

    def user_add_zipcode(self, zip_id):
        self.input_text(zip_id, *self.ZIP_ID_BOX)

    def user_sees_model3_title(self):
        expected = 'Model 3'
        actual = self.find_element(*self.MODEL3_INV_PAGE).text
        assert expected in actual,  f'{expected} is not in {actual}'
