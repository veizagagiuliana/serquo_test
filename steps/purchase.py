from behave import *
from selenium import webdriver

from helpers.page_objects.cart_page import CartPage
from helpers.page_objects.home_page import HomePage
from helpers.page_objects.product_page import ProductPage

card_data = {
    "name": "test",
    "country": "test",
    "city": "test",
    "card": "2321123223211232",
    "month": "09",
    "year": "2026"
}


@given('I open the website')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.home_page = HomePage(context.browser)
    context.home_page.open()


@given('I am on the sign-up page')
def step_impl(context):
    context.home_page.log_in("testtest", "testtest")


@given('I am at home')
def step_impl(context):
    context.home_page.home()


@when('I select the first product')
def step_impl(context):
    context.home_page.click_first_product()


@when('I add it to the cart')
def step_impl(context):
    context.product_page = ProductPage(context.browser)
    context.product_page.click_add_to_cart()


@when('I go to the cart and pay')
def step_impl(context):
    context.home_page.click_cart()
    context.cart_page = CartPage(context.browser)
    context.cart_page.click_place_order()
    context.cart_page.fill_place_order(name=card_data.get('name'),
                                       country=card_data.get('country'),
                                       city=card_data.get('city'),
                                       card=card_data.get('card'),
                                       month=card_data.get('month'),
                                       year=card_data.get('year'))
    context.cart_page.click_purchase()


@then('a message successful is displayed')
def step_impl(context):
    assert context.cart_page.success_is_visible() is True, 'The purchase.feature could not be completed.'
