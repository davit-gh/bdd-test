from framework.webapp import WebApp
import random
from faker import Faker
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By


class AdCreationPageLocator(object):
    LOADING_OVERLAY = (By.CLASS_NAME, "js-get-data-loading-overlay")
    AD_ACCOUNT_BTN = (By.XPATH, "(//div[@id='adcreationSteps']//button)[1]")
    AD_ACCOUNT_OPTION_XPATH = (By.XPATH, "//div[@id='adcreationSteps']//a/span[text()='{}']")


class AdCreationPage(WebApp):

    def pick_ad_account(self, ad_account):
        self.wait_for_element_to_disappear(AdCreationPageLocator.LOADING_OVERLAY)
        self.wait_for_clickable(AdCreationPageLocator.AD_ACCOUNT_BTN).click()
        option = (By.XPATH, AdCreationPageLocator.AD_ACCOUNT_OPTION_XPATH.format(ad_account))
        self.wait_for_clickable(option).click()
