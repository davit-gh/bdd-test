import random
from faker import Faker
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException

from framework.webapp import WebApp

class AudiencesPageLocator(object):
    # OVERLAYS
    LOADING_OVERLAY = (By.CLASS_NAME, "loading-overlay-audience")
    LOADING_OVERLAY_ICON_XPATH = "//div[@id='adFlexContent2']//tbody/tr[{}]/td/div[1]"
    MOVE_TO_MODAL_OVERLAY = (By.XPATH, "//div[@id='moveToModal']/div/div")
    AUDIENCE_MODAL_OVERLAY = (By.XPATH, "//div[@id='createSavedAudience']/div/div")
    AUDIENCE_ESTIMATE_OVERLAY = (By.CLASS_NAME, "audience-estimate")
    # AUDIENCE
    CREATE_AUDIENCE_BTN = (By.XPATH, "//ul[@class='create-add-title']/li/button")
    AUDIENCE_ROWS = (By.XPATH, "//div[@id='adFlexContent2']//tbody/tr")
    ACTION_ICONS_XPATH = "(//div[@id='adFlexContent2']//tbody/tr)[{}]//div[@class='buttons-row']/button"
    SELECT_BTN = "(//div[@id='adFlexContent2']//tbody/tr)[{}]//div[@class='buttons-content']/button"
    AUDIENCE_LOCATION_SELECT = (By.NAME, "location_include[]")
    # MOVE TO MODAL
    POPUP_MOVE_BUTTON = (By.XPATH, "//div[@id='moveToModal']//button[2]")
    POPUP_DELETE_BUTTON = (By.XPATH, "//div[@id='deleteSelectedModal']//button[2]")
    SUCCESS_POPOVER = (By.ID, "successMessage")
    MOVE_TO_MODAL = (By.ID, "moveToModal")
    # PAGINATION
    PAGINATION_NEXT = (By.CLASS_NAME, "pagination-next")
    PAGINATION_PER_PAGE_XPATH = "//li[text()='Show: {} Per']"
    PAGINATION_DEFAULT = (By.XPATH, "//span[text()='Show: 12 Per']")
    # DATES
    DATE_SORT = (By.XPATH, "//div[contains(@class,'sort-by-select-content')]")
    DATE_SORT_OPTION_XPATH = "//li[text()='{}']"
    AUDIENCE_MODIFIED_DATES = (By.XPATH, "//div[@id='adFlexContent2']//tbody/tr/td/p[2]")
    # FOLDERS
    FOLDERS_LI = (By.XPATH, "//ul[@class='folders-ul']/li")
    FIRST_MOVE_TO_FOLDER = (By.XPATH, "//ul[@id='moveToFolderList']/li[1]")
    ADD_FOLDER_BUTTON = (By.CLASS_NAME, "add-folder")
    HAMBURGER_ICON = (By.ID, "showFoldersBtn2")
    FOLDERS_PANEL = (By.CSS_SELECTOR, "div#adFlexContent2.active")
    NEW_FOLDER_NAME = (By.XPATH, "//div[@id='adFlexContent2']//div[2]/a")
    SAVE_ICON = (By.XPATH, "//span[contains(@class, 'save-folder-action')]")
    # AD ACCOUNT
    AD_ACCOUNT_BTN = (By.XPATH, "//div[@id='savedAudienceTab']//div[@class='filters-content--item']//button")
    AD_ACCOUNT_SPAN_XPATH = "//div[@id='savedAudienceTab']//div[@class='filters-content--item']" \
                              "//span[@class='text' and text()='{}']"
    AD_ACCOUNT_OPTION_XPATH = "//select[@name='audience_adaccount_id']/option[text()='{}']"
    # DATEPICKER
    DATEPICKER_START = (By.XPATH, '//input[@name="daterangepicker_start"]')
    DATEPICKER_END = (By.XPATH, '//input[@name="daterangepicker_end"]')
    # TAGS
    TAGS_FIELD = (By.XPATH, '//input[@value="Tags..."]')
    TAGS_OPTION = (By.XPATH, "//li[@data-option-array-index='0']")
    AUDIENCES_TAGS = (By.XPATH, "//div[@id='savedAudienceTab']//div[@class='tag-item']/span")

class AudiencePage(WebApp):

    audience_id = ""
    audience_index = ""
    folder_name = ""

    def verify_on_audiences_page(self):
        self.wait_for_element_to_disappear(AudiencesPageLocator.LOADING_OVERLAY)
        element = self.wait_for_element(AudiencesPageLocator.CREATE_AUDIENCE_BTN)
        assert element.is_displayed()

    def verify_ad_audience_is_not_empty(self):
        # TODO add new ad design if page is empty
        elements = self.wait_for_elements(AudiencesPageLocator.AUDIENCE_ROWS)
        assert len(elements) > 1

    def hover_over_audience_block(self):
        audiences = self.wait_for_elements(AudiencesPageLocator.AUDIENCE_ROWS)
        audience = random.choice(audiences)
        self.audience_id = audience.get_attribute('data-id')
        self.action_move_to_element(audience)
        # in UI index is plus 1
        self.audience_index = (audiences.index(audience)) + 1

    def verify_action_icons_visible(self):
        icon = (By.XPATH, AudiencesPageLocator.ACTION_ICONS_XPATH.format(self.audience_id))
        select_btn_selector = (By.XPATH, AudiencesPageLocator.SELECT_BTN.format(self.audience_id))
        assert self.element_exists(select_btn_selector)
        action_icons = self.wait_for_elements(icon)
        if len(action_icons) != 3:
            raise AssertionError("Found {} actions icons, expected to find 3".format(len(action_icons)))

    def click_action_btn(self, button_name):
        select_btn_selector = (By.XPATH, AudiencesPageLocator.SELECT_BTN.format(self.audience_index))
        if button_name == 'Select':
            self.wait_for_clickable(select_btn_selector).click()
        else:
            icon_selector = (By.XPATH, AudiencesPageLocator.ACTION_ICONS_XPATH.format(self.audience_index))
            icons = self.wait_for_elements(icon_selector)
            icon_to_click = [icon for icon in icons if icon.get_attribute('title') == button_name]
            icon_to_click[0].click()

    def verify_audience_is_selected(self):
        select_btn_selector = (By.XPATH, AudiencesPageLocator.SELECT_BTN.format(self.audience_index))
        element = self.wait_for_element(select_btn_selector)
        assert element.text == "Unselect"

    def audience_modal_is_opened(self):
        self.wait_for_element_to_disappear(AudiencesPageLocator.AUDIENCE_MODAL_OVERLAY)
        self.wait_for_element_to_disappear(AudiencesPageLocator.AUDIENCE_ESTIMATE_OVERLAY)
        assert self.element_exists(AudiencesPageLocator.AUDIENCE_LOCATION_SELECT)

    def verify_folders_list_is_not_empty(self):
        self.wait_for_clickable(AudiencesPageLocator.HAMBURGER_ICON).click()
        folders = self.wait_for_elements(AudiencesPageLocator.FOLDERS_LI)
        assert len(folders) >= 1

    def move_to_folder(self):
        self.wait_for_element_to_disappear(AudiencesPageLocator.MOVE_TO_MODAL_OVERLAY)
        self.wait_for_clickable(AudiencesPageLocator.FIRST_MOVE_TO_FOLDER).click()
        time.sleep(1)
        self.wait_for_clickable(AudiencesPageLocator.POPUP_MOVE_BUTTON).click()
        self.wait_for_element_to_disappear(AudiencesPageLocator.LOADING_OVERLAY)
        overlay_icon_selector = (By.XPATH, AudiencesPageLocator.LOADING_OVERLAY_ICON_XPATH.format(self.audience_index))
        self.wait_for_element_to_disappear(AudiencesPageLocator.LOADING_OVERLAY)
        self.wait_for_element_to_disappear(overlay_icon_selector)


    def verify_audience_is_moved(self):
        time.sleep(1)
        self.wait_for_element_to_disappear(AudiencesPageLocator.SUCCESS_POPOVER)
        folders = self.wait_for_elements(AudiencesPageLocator.FOLDERS_LI)
        folders[1].click()
        audiences = self.wait_for_elements(AudiencesPageLocator.AUDIENCE_ROWS)
        audience_ids = [audience.get_attribute('data-id') for audience in audiences]
        if self.audience_id != '':
            assert self.audience_id in audience_ids
        else:
            raise AssertionError("Error occurred when moving to a folder")

    def click_button_on_popup(self):
        self.wait_for_clickable(AudiencesPageLocator.POPUP_DELETE_BUTTON).click()

    def verify_audience_is_deleted(self):
        time.sleep(0.5)
        self.wait_for_element_to_disappear(AudiencesPageLocator.SUCCESS_POPOVER)
        audiences = self.wait_for_elements(AudiencesPageLocator.AUDIENCE_ROWS)
        audience_ids = [audience.get_attribute('data-id') for audience in audiences]
        assert self.audience_id not in audience_ids

    def verify_audiences_page_is_paginated(self):
        audiences = self.wait_for_elements(AudiencesPageLocator.AUDIENCE_ROWS)
        assert len(audiences) <= 12
        assert self.element_exists(AudiencesPageLocator.PAGINATION_NEXT)

    def select_per_page_pagination(self, pagination_number):
        self.wait_for_clickable(AudiencesPageLocator.PAGINATION_DEFAULT).click()
        per_page_selector = (By.XPATH, AudiencesPageLocator.PAGINATION_PER_PAGE_XPATH.format(pagination_number))
        self.find_element(*per_page_selector).click()
        self.wait_for_element_to_disappear(AudiencesPageLocator.LOADING_OVERLAY)

    def click_on_pagination_next(self):
        self.wait_for_clickable(AudiencesPageLocator.PAGINATION_NEXT).click()

    def verify_number_of_displayed_audiences(self, pagination_number):
        audiences = self.wait_for_elements(AudiencesPageLocator.AUDIENCE_ROWS)
        assert len(audiences) <= int(pagination_number)

    def select_sorting_by_date(self, sort_type):
        self.wait_for_element_to_disappear(AudiencesPageLocator.LOADING_OVERLAY)
        self.wait_for_clickable(AudiencesPageLocator.DATE_SORT).click()
        self.wait_for_clickable((By.XPATH, AudiencesPageLocator.DATE_SORT_OPTION_XPATH.format(sort_type))).click()

    def verify_audience_ordering(self, sort_type):
        reverse = True if sort_type == "descending" else False
        audience_dates = self.wait_for_elements(AudiencesPageLocator.AUDIENCE_MODIFIED_DATES)
        date_times = [datetime.strptime(date.text, '%d/%m/%Y %H:%M') for date in audience_dates]
        assert sorted(date_times, reverse=reverse) == date_times
        if self.element_exists(AudiencesPageLocator.PAGINATION_NEXT):
            self.click_on_pagination_next()
            self.verify_audience_ordering(sort_type)

    def create_new_folder(self):
        time.sleep(3)
        self.wait_for_clickable(AudiencesPageLocator.HAMBURGER_ICON).click()
        self.wait_for_element(AudiencesPageLocator.ADD_FOLDER_BUTTON).click()
        faker = Faker()
        self.folder_name = faker.first_name()
        self.driver.instance.find_element(*AudiencesPageLocator.NEW_FOLDER_NAME).send_keys(self.folder_name)

    def click_folder_creation_save_icon(self):
        self.wait_for_clickable(AudiencesPageLocator.SAVE_ICON).click()

    def verify_that_folder_exists(self):
        time.sleep(1)
        folders = self.wait_for_elements(AudiencesPageLocator.FOLDERS_LI)
        folder_names = [folder_name.text for folder_name in folders]
        assert self.folder_name in folder_names

    def pick_ad_account(self, ad_account):
        self.wait_for_element_to_disappear(AudiencesPageLocator.LOADING_OVERLAY)
        self.wait_for_clickable(AudiencesPageLocator.AD_ACCOUNT_BTN).click()
        option = (By.XPATH, AudiencesPageLocator.AD_ACCOUNT_OPTION_XPATH.format(ad_account))
        self.wait_for_clickable(option).click()

    def verify_audiences_belong_to_ad_account(self, ad_account):
        option_selector = (By.XPATH, AudiencesPageLocator.AD_ACCOUNT_OPTION_XPATH.format(ad_account))
        option = self.find_element(*option_selector)
        ad_account_id = option.get_attribute("value")
        audiences = self.wait_for_elements(AudiencesPageLocator.AUDIENCE_ROWS)
        audience_adaccount_ids = [audience.get_attribute("data-adaccountid") for audience in audiences]
        audience_adaccount_ids = set(audience_adaccount_ids)
        assert len(audience_adaccount_ids) == 1
        assert audience_adaccount_ids.pop() == ad_account_id

    def select_date_range(self, date1, date2):
        self.wait_for_element_to_disappear(AudiencesPageLocator.LOADING_OVERLAY)
        selector = (By.XPATH, '//div[@class="filters-content--item"][2]')
        self.wait_for_clickable(selector).click()
        datepicker_start = self.wait_for_element(AudiencesPageLocator.DATEPICKER_START)
        datepicker_start.clear()
        datepicker_start.send_keys(date1)
        datepicker_end = self.wait_for_element(AudiencesPageLocator.DATEPICKER_END)
        datepicker_end.clear()
        datepicker_end.send_keys(date2)
        btn_selector = (By.XPATH, "//button[text()='Apply']")
        self.wait_for_clickable(btn_selector).click()

    def verify_ad_designs_within_date_range(self, date1, date2):
        # TODO handle the case when ad designs are paginated
        audiences = self.wait_for_elements(AudiencesPageLocator.AUDIENCE_MODIFIED_DATES)
        date_object1 = datetime.strptime(date1 + ' 23:59', '%d/%m/%Y %H:%M')
        date_object2 = datetime.strptime(date2 + ' 23:59', '%d/%m/%Y %H:%M')

        datetime_object1 = datetime.strptime(audiences[1].text, '%d/%m/%Y %H:%M')
        datetime_object2 = datetime.strptime(audiences[len(audiences) - 1].text, '%d/%m/%Y %H:%M')

        assert date_object1 > datetime_object2
        assert date_object2 > datetime_object1

    def enter_tag(self, tag_name):
        self.wait_for_element_to_disappear(AudiencesPageLocator.LOADING_OVERLAY)
        element = self.wait_for_clickable(AudiencesPageLocator.TAGS_FIELD)
        element.click()
        time.sleep(1)
        element.send_keys(tag_name)
        self.wait_for_clickable(AudiencesPageLocator.TAGS_OPTION).click()

    def verify_audience_contains_tag(self, tag_name):
        try:
            tags = self.wait_for_elements(AudiencesPageLocator.AUDIENCES_TAGS)
        except TimeoutException:
            raise AssertionError("No audiences containing the tag")
        tag_text = [tag.text for tag in tags]
        assert set(tag_text).pop() == tag_name
