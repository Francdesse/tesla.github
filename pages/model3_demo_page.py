from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MODEL3DEMOPAGE(Page):

    PAGE_TILE= (By.XPATH, "//h1[text()='Schedule a Demo Drive']")

    sleep(3)

    def user_verify_demo_page(self):
        assert self.find_element(*self.PAGE_TILE).is_displayed(), "Title is missing"