import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import data
from urls import urls


class TestPersAccConstrExit:

    def test_to_personal_account_and_exit(self, driver):

        driver.get(urls.URL_STELLAR_LOGON)

        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(data.my_email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(data.my_password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.MAIN_TITLE_CONSTRUCTOR)))

        driver.find_element(*TestLocators.MAIN_ACCOUNT_URL).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.PERS_ACC_PROFILE_BUTTON)))

        driver.find_element(*TestLocators.PERS_ACC_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.ENTRANCE_TITLE)))


    def test_to_personal_account_to_constructor_via_logotype(self, driver):

        driver.get(urls.URL_STELLAR_LOGON)

        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(data.my_email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(data.my_password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.MAIN_TITLE_CONSTRUCTOR)))

        driver.find_element(*TestLocators.MAIN_ACCOUNT_URL).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.PERS_ACC_PROFILE_BUTTON)))

        driver.find_element(*TestLocators.PERS_ACC_LOGOTYPE_URL).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.MAIN_PLACE_ORDER_BUTTON)))

    def test_to_personal_account_to_constructor_via_constructor_url(self, driver):

        driver.get(urls.URL_STELLAR_LOGON)

        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(data.my_email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(data.my_password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.MAIN_TITLE_CONSTRUCTOR)))

        driver.find_element(*TestLocators.MAIN_ACCOUNT_URL).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.PERS_ACC_PROFILE_BUTTON)))

        driver.find_element(*TestLocators.PERS_ACC_CONSTRUCTOR_URL).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.MAIN_PLACE_ORDER_BUTTON)))



