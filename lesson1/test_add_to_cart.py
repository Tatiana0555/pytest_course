from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_item_in_the_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # text_before = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name ']").text
    # второй вариант через XPATH:
    text_before = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]').text

    button = driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button.click()
    # time.sleep(3)

    cart = driver.find_element(By.CSS_SELECTOR, "a[class ='shopping_cart_link']")
    cart.click()

    # text_after = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name ']").text

    # text_after = driver.find_element(By.CSS_SELECTOR, '//div[contains(text(), "Sauce Labs Backpack")]').text
    text_after = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]').text

    # time.sleep(3)

    assert text_before == text_after
    # time.sleep(3)