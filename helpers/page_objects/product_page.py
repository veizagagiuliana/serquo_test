from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.page_objects.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-success')

    def click_add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        add_to_cart_button.click()
