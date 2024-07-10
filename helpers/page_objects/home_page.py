from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from helpers.page_objects.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.demoblaze.com/"

    FIRST_PRODUCT = (By.CSS_SELECTOR, '.card-block a')
    LOG_IN = (By.ID, 'login2')
    LOG_USER = (By.ID, 'loginusername')
    LOG_PASS = (By.ID, 'loginpassword')
    CART_PAGE = (By.ID, 'cartur')
    HOME = (By.ID, "nava")
    BUTTON_LOG = (By.CSS_SELECTOR, '#logInModal > div > div > div.modal-footer > button.btn.btn-primary')

    def open(self):
        self.driver.get(self.URL)

    def log_in(self, user, password):
        log_in = self.driver.find_element(*self.LOG_IN)
        log_in.click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOG_USER)
        )
        log_user = self.driver.find_element(*self.LOG_USER)
        log_user.send_keys(user)
        log_pass = self.driver.find_element(*self.LOG_PASS)
        log_pass.send_keys(password)
        button_log = self.driver.find_element(*self.BUTTON_LOG)
        button_log.click()

    def home(self):
        sleep(2)
        home = self.driver.find_element(*self.HOME)
        home.click()

    def click_first_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        )
        element = self.driver.find_element(*self.FIRST_PRODUCT)
        element.click()

    def click_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_PAGE)
        )
        cart = self.driver.find_element(*self.CART_PAGE)
        cart.click()
