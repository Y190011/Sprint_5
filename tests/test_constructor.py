import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import urls
import data
from locators import TestLocators

class TestConstructor:

    def test_sections_sauces_fillings_buns(self, driver):

        driver.get(urls.URL_STELLAR_LOGON)

        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(data.my_email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(data.my_password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.MAIN_TITLE_CONSTRUCTOR)))

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.MAIN_PLACE_ORDER_BUTTON)))


        driver.find_element(*TestLocators.MAIN_SAUCES_TAB).click()
        driver.find_element(*TestLocators.MAIN_CURR_STATUS_SAUCES_TAB)


        driver.find_element(*TestLocators.MAIN_FILLINGS_TAB).click()
        driver.find_element(*TestLocators.MAIN_CURR_STATUS_FILLINGS_TAB)


        driver.find_element(*TestLocators.MAIN_BUNS_TAB).click()
        driver.find_element(*TestLocators.MAIN_CURR_STATUS_BUNS_TAB)


