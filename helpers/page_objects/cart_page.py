from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers.page_objects.base_page import BasePage


class CartPage(BasePage):
    SUCCESS = (By.CLASS_NAME, 'sa-success')
    MODAL = (By.CLASS_NAME, 'modal-footer')
    PLACE_ORDER = (By.CLASS_NAME, 'btn-success')
    PURCHASE = (By.CSS_SELECTOR, '#orderModal > div > div > div.modal-footer > button.btn.btn-primary')
    FILL_NAME = (By.ID, 'name')
    FILL_COUNTRY = (By.ID, 'country')
    FILL_CITY = (By.ID, 'city')
    FILL_CARD = (By.ID, 'card')
    FILL_MONTH = (By.ID, 'month')
    FILL_YEAR = (By.ID, 'year')

    def click_place_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PLACE_ORDER)
        )
        place_order = self.driver.find_element(*self.PLACE_ORDER)
        place_order.click()

    def fill_place_order(self, name, country, city, card, month, year):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FILL_NAME)
        )
        self.driver.find_element(*self.FILL_NAME).send_keys(name)
        self.driver.find_element(*self.FILL_COUNTRY).send_keys(country)
        self.driver.find_element(*self.FILL_CITY).send_keys(city)
        self.driver.find_element(*self.FILL_CARD).send_keys(card)
        self.driver.find_element(*self.FILL_MONTH).send_keys(month)
        self.driver.find_element(*self.FILL_YEAR).send_keys(year)

    def click_purchase(self):
        purchase_button = self.driver.find_element(*self.PURCHASE)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", purchase_button)
        purchase_button.click()

    def success_is_visible(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS)
        )
        success = self.driver.find_element(*self.SUCCESS)
        return success.is_displayed()
