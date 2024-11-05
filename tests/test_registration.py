import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from urls import urls
from locators import TestLocators
import helper


class TestRegistration:

    def test_registration_and_check(self, driver):

        driver.get(urls.URL_STELLAR_LOGON)

        driver.find_element(*TestLocators.REGISTRATION_URL).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                    (TestLocators.REGISTRATION_TITLE)))

        password = helper.gen_random_password()
        email    = helper.gen_random_email()

        driver.find_element(*TestLocators.REGISTRATION_NAME).send_keys(helper.gen_random_name())
        driver.find_element(*TestLocators.REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.ENTRANCE_TITLE)))

        incorrect_password = password + "1"
        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(incorrect_password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.ENTRANCE_TITLE)))

        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.MAIN_TITLE_CONSTRUCTOR)))


