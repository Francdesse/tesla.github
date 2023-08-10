from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class MODEL3INVENTORYPAGE(Page):

    MODEL3_TITLE = (By.CSS_SELECTOR, '.results-container .result.card .tds-text--h4')
                       #'[data-id="278_fa63d9fe83302f6484f589f28937991b-search-result-container"] h3')
                       #"//article[@class='result card' and @data-id='278_b8af95e46257142c4f98bda77492ad1c-search-result-container']//h3[@class='tds-text--h4']")
                       #"//article[@data-id='278_fa63d9fe83302f6484f589f28937991b-search-result-container']//h3[@class='tds-text--h4']")

    ZIP_ID_BOX = (By.CSS_SELECTOR, '.tds-form-input [data-id="registration-postal-code-textbox"]')
    VIEW_DETAILS = (By.CSS_SELECTOR, '.results-container.results-container--grid .result-cta-btns')
                    #' .result-cta-btns .result-view-details-btn')
    #('[data-id="276_3947ca605de2c37ae4d7db8ad5d4ca62-search-result-container"] .result-view-details-btn.tds-btn.tds-btn--secondary')


    def user_nav_to_link(self, site_id):
        self.open_url(site_id)

    def user_add_zipcode(self, zip_id):
        self.find_element(*self.ZIP_ID_BOX).clear()
        self.input_text(zip_id, *self.ZIP_ID_BOX)

    def user_sees_model3_title(self, expected_result):
        actual = self.find_elements(*self.MODEL3_TITLE)[0].text
        print(actual)
        assert expected_result in actual,  f'{expected_result} is not in {actual}'

    def user_hover_over_first_option(self):

        mode3_hover=self.find_elements(*self.VIEW_DETAILS)

        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(*self.VIEW_DETAILS))
        actions.perform()
        sleep(5)

    def user_clicks_on_first_model3(self):
        clicks_on_title = self.find_elements(*self.VIEW_DETAILS)
        clicks_on_title[0].click()
        sleep(1)

    def storing_original_window(self):
        self.original_window = self.driver.current_window_handle

    # SWITCHING TO THE PRODUCT PAGE
    def model3_opens_to_new_page(self):
        self.driver.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

    def closing_model3_product_page(self):
        self.driver.close()

    def switching_back_to_inv_page(self):
        self.driver.switch_to.window(self.original_window)
