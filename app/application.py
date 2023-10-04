#from pages.header_page import Header
from pages.main_page import MainPage
from pages.model3_inv_page import MODEL3INVENTORYPAGE
from pages.product_page import PRODUCTPAGE
from pages.model3_demo_page import MODEL3DEMOPAGE
# from pages.sign_in_page import SignInPage



class Application:

    def __init__(self, driver):
        self.driver = driver

        #self.header_page =  Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.model3_inv_page = MODEL3INVENTORYPAGE(self.driver)
        self.product_page = PRODUCTPAGE(self.driver)
        self.model3_demo_page = MODEL3DEMOPAGE(self.driver)
        # self.sign_in_page = SignInPage(self.driver)
