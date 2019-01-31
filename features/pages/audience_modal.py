from random import randint
import time
from faker import Faker
from faker.providers import address

from framework.webapp import WebApp
from selenium.webdriver.common.by import By


class AudienceModalLocators(object):
    MODAL_OVERLAY = (By.XPATH, "//div[@id='createSavedAudience']/div/div")
    CREATE_AUDIENCE_BTN = (By.ID, "createSavedAudienceBtn")
    LOCATION_INPUT = (By.XPATH, "//input[@value='San Francisco...']")
    LANGUAGE_INPUT = (By.XPATH, "//input[@value='Select languages']")
    SUGGESTED_LOCATIONS_UL = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[2]")
    SUGGESTED_LOCATIONS_LI = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[2]/li[last()]")
    SUGGESTED_LANGUAGES = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[4]/li")
    AGE_FROM = (By.XPATH, "//label[@class='age-label' and text()='Age:']/../div/div[@class='common-select'][1]")
    SUGGESTED_AGE_FROM = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[5]/li")
    AGE_TO = (By.XPATH, "//label[@class='age-label' and text()='Age:']/../div/div[@class='common-select'][2]")
    SUGGESTED_AGE_TO = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[6]/li")
    EXCLUDE_LINK_ID = "(//span[@class='exclude-btn'])[{}]"
    MODAL_BUTTON_XPATH = "//form[@id='{}']//button[text()='{}']"
    LOADING_SEARCH = (By.XPATH, "//label[text()='Locations:']/following-sibling::div/div/div[1]")
    CUSTOM_AUDIENCE_INPUT = (By.XPATH, "(//input[@value='Add Custom or Lookalike Audiences'])")
    DETAILED_TARGETING_INPUT = "(//input[@value='Select demographics, interests or behaviours'])[{}]"
    FOLDER_DROPDOWN = (By.XPATH, "//a[@class='chosen-single']/span[text()='All']")
    SUGGESTED_FOLDERS = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[16]/li")
    TAGS_INPUT = (By.XPATH, "//h4[text()='Tags']/../../div/div/input[@name='tags_list']")
    FEMALE_GENDER = (By.XPATH, "//input[@id='femaleGender']/../label[1]")
    MALE_GENDER = (By.XPATH, "//input[@id='maleGender']/../label[1]")
    SPLIT_BUTTONS = (By.XPATH, "(//span[@class='slider-split round'])")
    CREATE_BUTTON = (By.XPATH, "(//button[text()='Create'])[1]")
    CONNECT_TO_INPUT = "(//input[@value='Select pages, events or groups'])[{}]"
    SUGGESTED_USERS = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[11]/li")
    SUGGESTED_FRIENDS = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[12]/li")
    SUGGESTED_DEMOGRAPHICS = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[8]/li")
    SUGGESTED_EXCLUDE_DEMOGRAPHICS = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[9]/li")
    SUGGESTED_NARROW_DEMOGRAPHICS = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[10]/li")


class AudienceModal(WebApp):

    def click_create_audience_btn(self):
        self.wait_for_clickable(AudienceModalLocators.CREATE_AUDIENCE_BTN).click()

    def fill_in_and_choose_location(self, number_of_locations):
        faker = Faker()
        faker.add_provider(address)
        self.wait_for_element_to_disappear(AudienceModalLocators.MODAL_OVERLAY)
        location_input = self.find_element(*AudienceModalLocators.LOCATION_INPUT)
        i = int(number_of_locations)
        while i > 0:
            location_input.send_keys(faker.random_letter(), faker.random_letter())
            time.sleep(1)
            self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_SEARCH)
            self.wait_for_element(AudienceModalLocators.SUGGESTED_LOCATIONS_UL)
            self.wait_for_clickable(AudienceModalLocators.SUGGESTED_LOCATIONS_LI).click()
            i = i - 1

    def fill_language(self, count=1):
        # TODO does not work with 2 languages, for some reason it does not use same suggested list
        faker = Faker()
        language_input = self.find_element(*AudienceModalLocators.LANGUAGE_INPUT)
        i = count
        while i > 0:
            language_input.send_keys(faker.random_letter())
            time.sleep(3)
            self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_SEARCH)
            languages = self.wait_for_elements(AudienceModalLocators.SUGGESTED_LANGUAGES)
            languages[randint(0, len(languages))].click()
            i = i - 1

    def fill_age(self):
        time.sleep(1)
        self.find_element(*AudienceModalLocators.AGE_FROM).click()
        age_from = self.wait_for_presence_of_elements(AudienceModalLocators.SUGGESTED_AGE_FROM)
        age_from[randint(0, len(age_from))].click()
        self.find_element(*AudienceModalLocators.AGE_TO).click()
        age_to = self.wait_for_presence_of_elements(AudienceModalLocators.SUGGESTED_AGE_TO)
        age_to[randint(0, len(age_to))].click()

    def select_gender(self, gender="male"):
        time.sleep(2)
        if gender == "male":
            self.find_element(*AudienceModalLocators.MALE_GENDER).click()
        elif gender == "female":
            self.find_element(*AudienceModalLocators.FEMALE_GENDER).click()
        else:
            raise TypeError("Unknown gender")

    def fill_folders(self):
        self.find_element(*AudienceModalLocators.FOLDER_DROPDOWN).click()
        folders = self.wait_for_presence_of_elements(AudienceModalLocators.SUGGESTED_FOLDERS)
        folders[randint(0, len(folders))].click()

    def fill_tags(self):
        # TODO, doesn't work at the moment
        faker = Faker()
        tag = faker.word()
        self.find_element(*AudienceModalLocators.TAGS_INPUT).send_keys(tag)

    def click_on_split_button(self, buttons=1):
        btns = self.wait_for_presence_of_elements(AudienceModalLocators.SPLIT_BUTTONS)
        i = int(buttons)
        while i > 0:
            btn = randint(0, len(btns))
            print(btn)
            btns[btn].click()
            i = i - 1
            time.sleep(2)

    def click_create_button(self):
        self.find_element(*AudienceModalLocators.CREATE_BUTTON).click()

    def fill_targeting_demographics_or_behaviours_field(self, field_type, count=1):
        time.sleep(1)
        faker = Faker()
        if field_type == "demographics":
            locator = (By.XPATH, AudienceModalLocators.DETAILED_TARGETING_INPUT.format(1))
            options_locator = AudienceModalLocators.SUGGESTED_DEMOGRAPHICS
        elif field_type == "exclude demographics":
            locator = (By.XPATH, AudienceModalLocators.DETAILED_TARGETING_INPUT.format(2))
            options_locator = AudienceModalLocators.SUGGESTED_EXCLUDE_DEMOGRAPHICS
        elif field_type == "narrow demographics":
            locator = (By.XPATH, AudienceModalLocators.DETAILED_TARGETING_INPUT.format(3))
            options_locator = AudienceModalLocators.SUGGESTED_NARROW_DEMOGRAPHICS
        i = count
        while i > 0:
            self.find_element(*locator).send_keys(faker.random_letter(), faker.random_letter())
            time.sleep(4)
            self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_SEARCH)
            options = self.wait_for_presence_of_elements(options_locator)
            options[randint(0, len(options))].click()
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

    def fill_users_connect_to_input(self):
        time.sleep(2)
        locator = (By.XPATH, AudienceModalLocators.CONNECT_TO_INPUT.format(1))
        self.find_element(*locator).click()
        self.find_element(*locator).send_keys("a")
        users = self.wait_for_elements(AudienceModalLocators.SUGGESTED_USERS)
        users[randint(0, len(users))].click()

    def fill_friends_of_user_connected_to(self):
        time.sleep(2)
        locator = (By.XPATH, AudienceModalLocators.CONNECT_TO_INPUT.format(2))
        self.find_element(*locator).click()
        self.find_element(*locator).send_keys("a")
        friends = self.wait_for_elements(AudienceModalLocators.SUGGESTED_FRIENDS)
        friends[randint(0, len(friends))].click()

    def clear_location_input_field(self):
        self.find_element(*AudienceModalLocators.LOCATION_INPUT).clear()

    def click_on_exclude_link(self, link_number):
        exclude_link_locator = (By.ID, AudienceModalLocators.EXCLUDE_LINK_ID.format(link_number[0]))
        self.find_element(*exclude_link_locator).click()

    def click_btn_popup(self, button_name, modal_id):
        btn_locator = (By.XPATH, AudienceModalLocators.MODAL_BUTTON_XPATH.format(modal_id, button_name))
        self.wait_for_clickable(btn_locator).click()
        self.wait_for_element_to_disappear(AudienceModalLocators.MODAL_OVERLAY)
        pass
