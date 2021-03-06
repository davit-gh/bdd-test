import random
import time
from faker import Faker
from faker.providers import address

from framework.webapp import WebApp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AudienceModalLocators(object):
    LOADING_OVERLAY = (By.CLASS_NAME, "loading-overlay-audience")
    ESTIMATE_LOADING_OVERLAY = (By.CLASS_NAME, "loading-overlay-estimate")
    FIRST_LOADING_OVERLAY_ICON = (By.XPATH, "//div[@class='loading-overlay-icon'][1]")
    MODAL_OVERLAY = (By.XPATH, "//div[@id='createSavedAudience']/div/div")
    CREATE_AUDIENCE_BTN = (By.ID, "createSavedAudienceBtn")
    LOCATION_INPUT = (By.XPATH, "//input[@value='San Francisco...']")
    EXCLUDED_LOCATION_INPUT = (By.XPATH, "//input[@value='Country, City']")
    LANGUAGE_INPUT = (By.XPATH, "//input[@value='Select languages']")
    SUGGESTED_LOCATIONS_UL = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[2]")
    SUGGESTED_LOCATIONS_LI = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[2]/li[last()]")
    SUGGESTED_EXCLUDED_LOCATIONS_LI = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[3]/li[last()]")
    SUGGESTED_LANGUAGES_LI = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[4]/li[last()]")
    AGE_FROM = (By.XPATH, "//label[@class='age-label' and text()='Age:']/../div/div[@class='common-select'][1]")
    SUGGESTED_AGE_FROM_XPATH = "(//form[@id='audience']//ul[@class='chosen-results'])[5]/li[{}]"
    AGE_TO = (By.XPATH, "//label[@class='age-label' and text()='Age:']/../div/div[@class='common-select'][2]")
    SUGGESTED_AGE_TO_XPATH = "(//form[@id='audience']//ul[@class='chosen-results'])[6]/li[{}]"
    EXCLUDE_LINK_XPATH = "(//span[@class='exclude-btn'])[{}]"
    MODAL_BUTTON_XPATH = "//form[@id='{}']//button[text()='{}']"
    LOADING_SEARCH_XPATH = "//label[text()='{}:']/following-sibling::div/div/div[1]"
    CUSTOM_AUDIENCE_INPUT = (By.XPATH, "(//input[@value='Add Custom or Lookalike Audiences'])")
    DETAILED_TARGETING_INPUT = "(//input[@value='Select demographics, interests or behaviours'])[{}]"
    FOLDER_DROPDOWN = (By.XPATH, "//a[@class='chosen-single']/span[text()='All']")
    SUGGESTED_FOLDERS = (By.XPATH, "(//form[@id='audience']//ul[@class='chosen-results'])[16]/li[2]")
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
    # LOCATIONS, LANGUAGES
    LOCATIONS_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']/td[2]/div[2]/p[text()]"
    LOCATIONS_EXCLUDED_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']/td[2]/div[3]/div/p[text()]"
    LANGUAGES_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']//div[@class='lenguages-column']/p"
    AGE_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']/td[5]/p[text()]"
    GENDER_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']/td[6]/p[text()]"
    INTERESTS_INCLUDED_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']/td[7]/div[2]/div/p"
    INTERESTS_EXCLUDED_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']/td[7]/div[3]/div[1]/p"
    INTERESTS_NARROW_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']/td[7]/div[3]/div[2]/p"
    CA_SUGGESTIONS_LI_XPATH = "(//form[@id='audience']//ul[@class='chosen-results'])[{}]/li"
    CA_INCLUDE_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']/td[3]/div[2]/p"
    CA_EXCLUDE_XPATH = "//div[@id='adFlexContent2']//tr[@data-id='{}']/td[3]/div[3]/p"
    FOLDERS_LI = (By.XPATH, "//ul[@class='folders-ul']/li")
    AUDIENCE_ROWS = (By.XPATH, "//div[@id='adFlexContent2']//tbody/tr")
    SHOW_FOLDERS_BTN = (By.ID, "showFoldersBtn2")
    POTENTIAL_REACH = (By.XPATH, "//div[@id='fixedInfoBlock']/span")
    AGE_SPLIT_DROPDOWN = (By.XPATH, "(//form[@id='audience']//a[@class='chosen-single'])[4]")
    AGE_SPLIT_15_YEAR = (By.XPATH, "//li[text()='Every 15 year']")
    AUDIENCE_COUNT = (By.CLASS_NAME, "audience-count")


class AudienceModal(WebApp):

    locations = []
    languages = []
    age_to = ''
    age_from = ''
    gender = ''
    interests = []
    custom_audiences = []

    def click_create_audience_btn(self):
        self.wait_for_clickable(AudienceModalLocators.CREATE_AUDIENCE_BTN).click()

    def fill_in_and_choose_location(self, number_of_locations):
        faker = Faker()
        faker.add_provider(address)
        self.wait_for_element_to_disappear(AudienceModalLocators.MODAL_OVERLAY)
        location_input = self.wait_for_element(AudienceModalLocators.LOCATION_INPUT)
        excluded_location_input = self.wait_for_element(AudienceModalLocators.EXCLUDED_LOCATION_INPUT)
        i = int(number_of_locations)
        while i > 0:
            location_input.click()
            location_input.send_keys(faker.random_letter())
            self.wait_for_element_to_disappear((By.XPATH, AudienceModalLocators.LOADING_SEARCH_XPATH.format("Locations")))
            self.wait_for_element(AudienceModalLocators.SUGGESTED_LOCATIONS_UL)
            self.locations.append(self.find_element(*AudienceModalLocators.SUGGESTED_LOCATIONS_LI).text)
            self.wait_for_clickable(AudienceModalLocators.SUGGESTED_LOCATIONS_LI).click()

            excluded_location_input.click()
            excluded_location_input.send_keys(faker.random_letter())
            exclude_loc = self.wait_for_clickable(AudienceModalLocators.SUGGESTED_EXCLUDED_LOCATIONS_LI)
            self.locations.append(exclude_loc.text)
            exclude_loc.click()
            i = i - 1

    def fill_language(self, field_name, count=1):
        # TODO does not work with 2 languages, for some reason it does not use same suggested list
        language_input = self.wait_for_clickable(AudienceModalLocators.LANGUAGE_INPUT)
        i = count
        while i > 0:
            overlay = (By.XPATH, AudienceModalLocators.LOADING_SEARCH_XPATH.format(field_name))
            language_input.click()
            language_input.send_keys(random.choice('abcdefspgkuri'))
            time.sleep(2)
            self.wait_for_element_to_disappear(overlay)
            self.languages.append(self.find_element(*AudienceModalLocators.SUGGESTED_LANGUAGES_LI).text)
            self.wait_for_clickable(AudienceModalLocators.SUGGESTED_LANGUAGES_LI).click()
            i = i - 1

    def fill_age(self):
        time.sleep(2)
        self.wait_for_clickable(AudienceModalLocators.AGE_FROM).click()
        age_from_selector = (By.XPATH, AudienceModalLocators.SUGGESTED_AGE_FROM_XPATH.format(random.randint(1, 25)))
        age_from = self.wait_for_clickable(age_from_selector)
        self.age_from = age_from.text
        time.sleep(2)
        age_from.click()
        self.wait_for_clickable(AudienceModalLocators.AGE_TO).click()
        age_to_selector = (By.XPATH, AudienceModalLocators.SUGGESTED_AGE_TO_XPATH.format(random.randint(26, 50)))
        age_to = self.wait_for_clickable(age_to_selector)
        self.age_to = age_to.text
        age_to.click()

    def select_gender(self, gender="male"):
        time.sleep(2)
        if gender == "male":
            self.find_element(*AudienceModalLocators.MALE_GENDER).click()
            self.gender = "female"
        elif gender == "female":
            self.find_element(*AudienceModalLocators.FEMALE_GENDER).click()
            self.gender = "male"
        else:
            raise TypeError("Unknown gender")

    def fill_folders(self):
        self.wait_for_clickable(AudienceModalLocators.FOLDER_DROPDOWN).click()
        folders = self.wait_for_presence_of_elements(AudienceModalLocators.SUGGESTED_FOLDERS)
        time.sleep(1)
        folders[0].click()

    def fill_tags(self):
        # TODO, doesn't work at the moment
        faker = Faker()
        tag = faker.word()
        self.find_element(*AudienceModalLocators.TAGS_INPUT).send_keys(tag)

    def _get_potential_reach_and_audience_count(self):
        reach_span = self.find_element(*AudienceModalLocators.POTENTIAL_REACH)
        potential_reach = reach_span.text.split()[0]
        audience_count = self.find_element(*AudienceModalLocators.AUDIENCE_COUNT).text
        response = {
            'potential_reach': potential_reach,
            'audience_count': audience_count
        }
        return response

    def click_on_split_buttons(self):
        btns = self.wait_for_presence_of_elements(AudienceModalLocators.SPLIT_BUTTONS)
        for i in range(len(btns) - 1):
            btns[i].click()
        self.wait_for_clickable(AudienceModalLocators.AGE_SPLIT_DROPDOWN).click()
        self.wait_for_clickable(AudienceModalLocators.AGE_SPLIT_15_YEAR).click()
        self.wait_for_element_to_disappear(AudienceModalLocators.ESTIMATE_LOADING_OVERLAY)

    def click_create_button(self):
        self.find_element(*AudienceModalLocators.CREATE_BUTTON).click()

    def fill_targeting_demographics_or_behaviours_field(self, field_type, count=1):
        time.sleep(1)
        faker = Faker()
        if field_type == "Demographics, Interests or Behaviours":
            locator = (By.XPATH, AudienceModalLocators.DETAILED_TARGETING_INPUT.format(1))
            options_locator = AudienceModalLocators.SUGGESTED_DEMOGRAPHICS
        elif field_type == "Exclude Demographics, Interests or Behaviours":
            locator = (By.XPATH, AudienceModalLocators.DETAILED_TARGETING_INPUT.format(2))
            options_locator = AudienceModalLocators.SUGGESTED_EXCLUDE_DEMOGRAPHICS
        elif field_type == "Narrow Demographics, Interests or Behaviours":
            locator = (By.XPATH, AudienceModalLocators.DETAILED_TARGETING_INPUT.format(3))
            options_locator = AudienceModalLocators.SUGGESTED_NARROW_DEMOGRAPHICS
        i = count
        while i > 0:
            self.find_element(*locator).send_keys(faker.random_letter(), faker.random_letter())
            time.sleep(4)
            overlay_selector = (By.XPATH, AudienceModalLocators.LOADING_SEARCH_XPATH.format(field_type))
            self.wait_for_element_to_disappear(overlay_selector)
            options = self.wait_for_presence_of_elements(options_locator)
            option = options[random.randint(0, len(options) - 1)]
            self.interests.append(option.text)
            option.click()
            i = i - 1

    def fill_custom_audience_fields(self, fields_number=2):
        faker = Faker()
        audience_input = self.wait_for_elements(AudienceModalLocators.CUSTOM_AUDIENCE_INPUT)
        i = fields_number
        while i > 0:
            for j, field in enumerate(range(fields_number)):
                audience_input[field].send_keys(faker.random_letter())
                overlay_selector = (By.XPATH, AudienceModalLocators.LOADING_SEARCH_XPATH.format("Custom Audience"))
                time.sleep(2)
                self.wait_for_element_to_disappear(overlay_selector)
                suggestions_selector = (By.XPATH, AudienceModalLocators.CA_SUGGESTIONS_LI_XPATH.format(14 + j))
                custom_audiences = self.wait_for_presence_of_elements(suggestions_selector)
                custom_audience = custom_audiences[random.randint(0, len(custom_audiences) - 1)]
                self.custom_audiences.append(custom_audience.text)
                custom_audience.click()
                i = i - 1

    def fill_users_connect_to_input(self):
        time.sleep(2)
        locator = (By.XPATH, AudienceModalLocators.CONNECT_TO_INPUT.format(1))
        self.find_element(*locator).click()
        self.find_element(*locator).send_keys("a")
        users = self.wait_for_elements(AudienceModalLocators.SUGGESTED_USERS)
        users[random.randint(0, len(users)-1)].click()

    def fill_friends_of_user_connected_to(self):
        time.sleep(2)
        locator = (By.XPATH, AudienceModalLocators.CONNECT_TO_INPUT.format(2))
        self.find_element(*locator).click()
        self.find_element(*locator).send_keys("a")
        friends = self.wait_for_elements(AudienceModalLocators.SUGGESTED_FRIENDS)
        friends[random.randint(0, len(friends)-1)].click()

    def clear_location_input_field(self):
        self.find_element(*AudienceModalLocators.LOCATION_INPUT).clear()

    def click_on_exclude_link(self, link_number):
        exclude_link_locator = (By.XPATH, AudienceModalLocators.EXCLUDE_LINK_XPATH.format(link_number[0]))
        self.wait_for_clickable(exclude_link_locator).click()

    def click_btn_popup(self, button_name, modal_id):
        btn_locator = (By.XPATH, AudienceModalLocators.MODAL_BUTTON_XPATH.format(modal_id, button_name))
        reach_and_count = self._get_potential_reach_and_audience_count()
        self.wait_for_clickable(btn_locator).click()
        self.wait_for_element_to_disappear(AudienceModalLocators.MODAL_OVERLAY)
        reach_and_count['audiences'] = self.wait_for_elements(AudienceModalLocators.AUDIENCE_ROWS)
        return reach_and_count

    def verify_locations_is_changed(self, audience_id):
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_OVERLAY)
        self.wait_for_element_to_disappear(AudienceModalLocators.FIRST_LOADING_OVERLAY_ICON)
        locations_selector = AudienceModalLocators.LOCATIONS_XPATH.format(audience_id)
        locations_excluded_selector = AudienceModalLocators.LOCATIONS_EXCLUDED_XPATH.format(audience_id)
        locations = self.wait_for_presence_of_elements((By.XPATH, locations_selector))
        locations_excluded = self.wait_for_presence_of_elements((By.XPATH, locations_excluded_selector))
        location_texts = [location.text for location in locations]
        location_excluded_texts = [location.text for location in locations_excluded]
        assert set(self.locations).issubset(location_texts + location_excluded_texts)
        assert len(self.locations) < len(location_texts + location_excluded_texts)

    def verify_languages_is_changed(self, audience_id):
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_OVERLAY)
        languages_selector = AudienceModalLocators.LANGUAGES_XPATH.format(audience_id)
        languages = self.find_elements(*(By.XPATH, languages_selector))
        final_language_texts = [language.text for language in languages]
        assert set(self.languages).issubset(final_language_texts)
        assert len(self.languages) < len(final_language_texts)

    def verify_age_gender_are_changed(self, audience_id):
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_OVERLAY)
        age_selector = AudienceModalLocators.AGE_XPATH.format(audience_id)
        gender_selector = AudienceModalLocators.GENDER_XPATH.format(audience_id)
        ages = self.find_element(*(By.XPATH, age_selector))
        gender = self.find_element(*(By.XPATH, gender_selector))
        assert ages.text == "{}-{}".format(self.age_from, self.age_to)
        assert gender.text.lower() == self.gender

    def verify_interests_are_changed(self, audience_id):
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_OVERLAY)
        interests_include_selector = (By.XPATH, AudienceModalLocators.INTERESTS_INCLUDED_XPATH.format(audience_id))
        interests_exclude_selector = (By.XPATH, AudienceModalLocators.INTERESTS_EXCLUDED_XPATH.format(audience_id))
        interests_narrow_selector = (By.XPATH, AudienceModalLocators.INTERESTS_NARROW_XPATH.format(audience_id))
        interests_include = [interest.text for interest in self.find_elements(*interests_include_selector)]
        interests_exclude = [interest.text for interest in self.find_elements(*interests_exclude_selector)]
        interests_narrow = [interest.text for interest in self.find_elements(*interests_narrow_selector)]
        interests = interests_include + interests_exclude + interests_narrow
        assert set(self.interests).issubset(interests)

    def verify_custom_audience_is_changed(self, audience_id):
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_OVERLAY)
        ca_include_selector = (By.XPATH, AudienceModalLocators.CA_INCLUDE_XPATH.format(audience_id))
        ca_exclude_selector = (By.XPATH, AudienceModalLocators.CA_EXCLUDE_XPATH.format(audience_id))
        ca_include = [ca.text for ca in self.find_elements(*ca_include_selector)]
        ca_exclude = [ca.text for ca in self.find_elements(*ca_exclude_selector)]
        assert set(self.custom_audiences).issubset(ca_include + ca_exclude)

    def verify_moved_to_folder(self, audience_id):
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_OVERLAY)
        self.wait_for_clickable(AudienceModalLocators.SHOW_FOLDERS_BTN).click()
        folders = self.wait_for_elements(AudienceModalLocators.FOLDERS_LI)
        folders[1].click()
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_OVERLAY)
        audiences = self.wait_for_elements(AudienceModalLocators.AUDIENCE_ROWS)
        audience_ids = [audience.get_attribute('data-id') for audience in audiences]
        assert audience_id in audience_ids

    def verify_correct_number_of_audiences_are_created(self, context):
        self.wait_for_element_to_disappear(AudienceModalLocators.LOADING_OVERLAY)
        new_audience_count = self.find_element(*AudienceModalLocators.AUDIENCE_COUNT).text
        assert int(new_audience_count) == int(context.potential_reach) + int(context.audience_count)
        print(new_audience_count, context.potential_reach, context.audience_count)