import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import data
from urls import urls


class TestLogon:

    def test_logon_via_registration_form(self, driver):

        driver.get(urls.URL_STELLAR_LOGON)

        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(data.my_email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(data.my_password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (TestLocators.MAIN_TITLE_CONSTRUCTOR)))



    def test_logon_via_personal_account_button(self, driver):

        driver.get(urls.URL_STELLAR_MAIN)

        driver.find_element(*TestLocators.MAIN_ACCOUNT_URL).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.ENTRANCE_TITLE)))

        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(data.my_email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(data.my_password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.MAIN_TITLE_CONSTRUCTOR)))


    def test_logon_via_login_to_account_button_on_main_page(self, driver):

        driver.get(urls.URL_STELLAR_MAIN)

        driver.find_element(*TestLocators.MAIN_LOGON_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.ENTRANCE_TITLE)))

        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(data.my_email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(data.my_password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.MAIN_TITLE_CONSTRUCTOR)))


    def test_logon_via_button_on_password_restore_form(self, driver):

        driver.get(urls.URL_STELLAR_LOGON)

        driver.find_element(*TestLocators.ENTRANCE_FORGOT_PASSWORD_URL).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
                (TestLocators.PASSWORD_RECOVERY_TITLE)))

        driver.find_element(*TestLocators.PASSWORD_RECOVERY_REMEMBER_URL).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.ENTRANCE_TITLE)))

        driver.find_element(*TestLocators.ENTRANCE_EMAIL).send_keys(data.my_email)
        driver.find_element(*TestLocators.ENTRANCE_PASSWORD).send_keys(data.my_password)
        driver.find_element(*TestLocators.ENTRANCE_BUTTON).click()

        WebDriverWait(driver, 3).until(
               expected_conditions.visibility_of_element_located((TestLocators.MAIN_TITLE_CONSTRUCTOR)))