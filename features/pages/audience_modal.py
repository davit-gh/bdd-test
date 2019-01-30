from random import randint

from faker import Faker
from faker.providers import address

from framework.webapp import WebApp
from selenium.webdriver.common.by import By


class AudienceModalLocators(object):
    LOADING_OVERLAY = (By.CLASS_NAME, "loading-overlay-audience")
    CREATE_AUDIENCE_BTN = (By.ID, "createSavedAudienceBtn")
    LOCATION_INPUT = (By.XPATH, "//input[@value='San Francisco...']")
    LANGUAGE_INPUT = (By.XPATH, "//input[@value='Select languages']")
    SUGGESTED_LOCATIONS = (By.XPATH, "//form[@id='audience']//ul[@class='chosen-results']/li")
    SUGGESTED_LANGUAGES = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[4]/li")
    AGE_FROM = (By.XPATH, "//label[@class='age-label' and text()='Age:']/../div/div[@class='common-select'][1]")
    SUGGESTED_AGE_FROM = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[5]/li")
    AGE_TO = (By.XPATH, "//label[@class='age-label' and text()='Age:']/../div/div[@class='common-select'][2]")
    SUGGESTED_AGE_TO = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[6]/li")
    EXCLUDE_LINK_ID = "(//span[@class='exclude-btn'])[{}]"
    MODAL_BUTTON_XPATH = "//form[@id='{}']//button[text()='{}']"
    LOADING_SEARCH = (By.ID, "audience-search-loading")
    CUSTOM_AUDIENCE_INPUT = (By.XPATH, "(//input[@value='Add Custom or Lookalike Audiences'])")
    DETAILED_TARGETING_INPUT = (By.XPATH, "(//input[@value='Select demographics, interests or behaviours'])")


class AudienceModal(WebApp):

    def click_create_audience_btn(self):
        self.wait_for_clickable(AudienceModalLocators.CREATE_AUDIENCE_BTN).click()

    def fill_in_and_choose_location(self, number_of_locations):
        faker = Faker()
        faker.add_provider(address)
        location_input = self.find_element(*AudienceModalLocators.LOCATION_INPUT)
        i = int(number_of_locations)
        while i > 0:
            location_input.send_keys(faker.random_letter())
            self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_SEARCH)
            locations = self.wait_for_presence_of_elements(AudienceModalLocators.SUGGESTED_LOCATIONS)
            locations[randint(0, len(locations) - 1)].click()
            i = i - 1

    def fill_language(self):
        faker = Faker()
        language_input = self.find_element(*AudienceModalLocators.LANGUAGE_INPUT)
        language_input.send_keys(faker.random_letter())
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_SEARCH)
        languages = self.wait_for_elements(AudienceModalLocators.SUGGESTED_LANGUAGES)
        languages[randint(0, len(languages))].click()

    def fill_age(self):
        self.find_element(*AudienceModalLocators.AGE_FROM).click()
        age_from = self.wait_for_presence_of_elements(AudienceModalLocators.SUGGESTED_AGE_FROM)
        age_from[randint(0, len(age_from))].click()
        self.find_element(*AudienceModalLocators.AGE_TO).click()
        age_to = self.wait_for_presence_of_elements(AudienceModalLocators.SUGGESTED_AGE_TO)
        age_to[randint(0, len(age_to))].click()

    def fill_gender(self):
        # TODO
        pass

    def fill_detailed_targeting_fields(self, fields_number=3):
        faker = Faker()
        targeting_input = self.wait_for_elements(AudienceModalLocators.DETAILED_TARGETING_INPUT)
        i = fields_number
        while i > 0:
            for field in range(fields_number):
                targeting_input[field].send_keys(faker.random_letter())
                self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_SEARCH)
                locations = self.wait_for_presence_of_elements(AudienceModalLocators.SUGGESTED_LOCATIONS)
                locations[randint(0, len(locations))].click()
                i = i - 1

    def fill_custom_audience_fields(self, fields_number=2):
        faker = Faker()
        audience_input = self.wait_for_elements(AudienceModalLocators.CUSTOM_AUDIENCE_INPUT)
        i = fields_number
        while i > 0:
            for field in range(fields_number):
                audience_input[field].send_keys(faker.random_letter())
                self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_SEARCH)
                locations = self.wait_for_presence_of_elements(AudienceModalLocators.SUGGESTED_LOCATIONS)
                locations[randint(0, len(locations))].click()
                i = i - 1

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
