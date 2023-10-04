from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    DEMO_DRIVE_BTN= (By.XPATH, '//a[@title="Demo Drive" and @href="/drive"]')
    DEMO_PAGE_TITLE= (By.CSS_SELECTOR, '#root .car-containershow .header-container h1')
    EXPLORE_INV= (By.CSS_SELECTOR, '#block-tesla-frontend-content .tcl-homepage-hero__buttons [href="/inventory/new/m3"]')
    Model3_DEMO_DRIVE= (By.XPATH, "//span[text()='Demo Drive']")
    ORDR_NOW_BTN= (By.CSS_SELECTOR, '.tcl-button-group [title="Order Now"]')

    def user_nav_to_homepage(self):
        self.open_url('https://www.tesla.com')

    def user_clicks_on_order_now(self):
        ordernow_options= self.find_elements(*self.ORDR_NOW_BTN)
        ordernow_options[0].click()

    def user_clicks_on_demo_drive(self):
        all_options= self.find_elements(*self.DEMO_DRIVE_BTN)
        all_options[0].click()

    def user_taken_to_demo_drive_page(self):
        self.verify_element_text('Schedule a Demo Drive', *self.DEMO_PAGE_TITLE)

    def user_scroll_down(self):
        model3_explore_inv= self.find_element(*self.EXPLORE_INV)
        self.driver.execute_script("arguments[0].scrollIntoView();", model3_explore_inv)
        sleep(5)

    def user_clicks_on_inventory(self):
        model3_inv = self.find_elements(*self.EXPLORE_INV)
        model3_inv[0].click()

    def user_clicks_on_Model3_Demo_page(self):
        model3_demo_button = self.find_elements(*self.Model3_DEMO_DRIVE)
        model3_demo_button[0].click()
