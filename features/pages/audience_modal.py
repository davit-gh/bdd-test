import time
import os
from random import randint

from faker import Faker
from faker.providers import address

from framework.webapp import WebApp
from selenium.webdriver.common.by import By


class AudienceModalLocators(object):
    LOADING_OVERLAY = (By.CLASS_NAME, "loading-overlay-audience")
    CREATE_AUDIENCE_BTN = (By.ID, "createSavedAudienceBtn")
    LOCATION_INPUT = (By.XPATH, "//input[@value='San Francisco...']")
    SUGGESTED_LOCATIONS = (By.XPATH, "//form[@id='audience']//div[@class='common-select']/div/div/ul/li")
    EXCLUDE_LINK_ID = "(//span[@class='exclude-btn'])[{}]"
    MODAL_BUTTON_XPATH = "//form[@id='{}']//button[text()='{}']"

class AudienceModal(WebApp):

    def click_create_audience_btn(self):
        self.wait_for_clickable(AudienceModalLocators.CREATE_AUDIENCE_BTN).click()

    def fill_in_and_choose_location(self, number_of_locations):
        faker = Faker()
        faker.add_provider(address)
        location_input = self.find_element(*AudienceModalLocators.LOCATION_INPUT)
        for i in number_of_locations:
                location_input.send_keys(faker.random_letter())
                locations = self.wait_for_elements(AudienceModalLocators.SUGGESTED_LOCATIONS)
                locations[randint(0, len(locations)-1)].click()

    def clear_location_input_field(self):
        self.find_element(*AudienceModalLocators.LOCATION_INPUT).clear()

    def click_on_exclude_link(self, link_number):
        exclude_link_locator = (By.ID, AudienceModalLocators.EXCLUDE_LINK_ID.format(link_number[0]))
        self.find_element(*exclude_link_locator).click()

    def click_btn_popup(self, button_name, modal_id):
        btn_locator = (By.XPATH, AudienceModalLocators.MODAL_BUTTON_XPATH.format(modal_id, button_name))
        self.wait_for_clickable(btn_locator).click()
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_OVERLAY)
        pass