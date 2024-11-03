import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
from locators import TestLocators

class TestConstructor:

    def test_sections_sauces_fillings_buns(self, driver):

        driver.get(data.url_stellar_logon)

        driver.find_element(*TestLocators.SEARCH_ENTRANCE_EMAIL).send_keys(data.my_email)
        driver.find_element(*TestLocators.SEARCH_ENTRANCE_PASSWORD).send_keys(data.my_password)
        driver.find_element(*TestLocators.SEARCH_ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.SEARCH_MAIN_TITLE_CONSTRUCTOR)))

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.SEARCH_MAIN_PLACE_ORDER_BUTTON)))


        driver.find_element(*TestLocators.SEARCH_MAIN_SAUCES_TAB).click()
        driver.find_element(*TestLocators.SEARCH_MAIN_CURR_STATUS_SAUCES_TAB)


        driver.find_element(*TestLocators.SEARCH_MAIN_FILLINGS_TAB).click()
        driver.find_element(*TestLocators.SEARCH_MAIN_CURR_STATUS_FILLINGS_TAB)


        driver.find_element(*TestLocators.SEARCH_MAIN_BUNS_TAB).click()
        driver.find_element(*TestLocators.SEARCH_MAIN_CURR_STATUS_BUNS_TAB)


