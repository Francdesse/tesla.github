from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class PRODUCTPAGE(Page):
    TITLE1 = (By.XPATH, "//div[@class='vehicle-summary-container']//span[contains(text(), 'Model 3')]")
    TITLE = (By.XPATH, "//h1[@class='text-loader--content tds-text--center tds-o-vertical_padding-top vehicleName-main-title tds-text--h1-alt tds-o-no_padding_bottom']")
    IMAGE = (By.CSS_SELECTOR,  'image')
    PRICE = (By.CSS_SELECTOR, '.tds-flex-item.summary-options .finance-type.finance-type--cash ')
    RANGE = (By.CSS_SELECTOR, '[data-id="range"]')
    SPEED = (By.CSS_SELECTOR, '[data-id="top-speed"]')
    VEHICLE_DETAILS = (By.CSS_SELECTOR, '.vehicleSummary-main-title')

    def Navigate_to_product_page(self, link_id):
        self.open_url(link_id)

    def user_sees_all_product_components(self):
        assert self.wait_for_element_appear(*self.TITLE).is_displayed(), "title not found"
        assert self.find_element(*self.IMAGE).is_displayed(), "picture not found"
        assert self.find_element(*self.PRICE).is_displayed(), "price not found"
        assert self.find_element(*self.RANGE).is_displayed(), "range not found"
        assert self.find_element(*self.SPEED).is_displayed(), "speed not found"
        assert self.find_element(*self.VEHICLE_DETAILS).is_displayed(), "vehicle details not found"