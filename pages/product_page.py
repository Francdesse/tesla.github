from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class PRODUCTPAGE(Page):
    TITLE = (By.CSS_SELECTOR, 'h1.text-loader--content span')
    IMAGE = (By.CSS_SELECTOR,  '#Model_3_Front_View image')
    PRICE = (By.CSS_SELECTOR, '#footer .finance-type')
    RANGE = (By.CSS_SELECTOR, '.tds-text--h1[data-id="range"]')
    SPEED = (By.CSS_SELECTOR, '[data-id="top-speed"]')
    VEHICLE_DETAILS = (By.CSS_SELECTOR, '.modal-trigger .text-loader--content span')

    def Navigate_to_product_page(self, link_id):
        self.open_url(link_id)
        sleep(2)

    # def user_sees_all_product_components(self):
    #     assert self.wait_for_element_appear(*self.TITLE).is_displayed(), "title not found"
    #     assert self.find_element(*self.IMAGE).is_displayed(), "picture not found"
    #     assert self.find_element(*self.PRICE).is_displayed(), "price not found"
    #     assert self.find_element(*self.RANGE).is_displayed(), "range not found"
    #     assert self.find_element(*self.SPEED).is_displayed(), "speed not found"
    #     assert self.find_element(*self.VEHICLE_DETAILS).is_displayed(), "vehicle details not found"

    def user_sees_all_model3_product_components(self):
        assert self.wait_for_element_appear(*self.TITLE).is_displayed(), "title not found"
        assert self.find_element(*self.IMAGE).is_displayed(), "picture not found"
        assert self.find_element(*self.PRICE).is_displayed(), "price not found"
        assert self.find_element(*self.RANGE).is_displayed(), "range not found"
        assert self.find_element(*self.SPEED).is_displayed(), "speed not found"
        assert self.find_element(*self.VEHICLE_DETAILS).is_displayed(), "vehicle details not found"