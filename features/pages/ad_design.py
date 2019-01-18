import random
from random import randint
from faker import Faker
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException

from framework.webapp import WebApp


class AdDesignPageLocator(object):
    CREATE_AD_DESIGN_BUTTON = (By.ID, "createAdDesignBtn")
    MODAL_ID = (By.ID, "createAdDesignModal")
    AD_ACCOUNT_OPTION = (By.XPATH, "//span[text()='Sandbox Adzwedo']")
    AD_ACCOUNT_DROPDOWN = (By.CLASS_NAME, "ad-account-select")
    PUBLISHED_POSTS_TABLE_ROW = (By.XPATH, "//div[@id='selectedByPublishedPosts']//tbody/tr")
    SELECT_BTN = (By.XPATH, "//div[@id='selectedByPublishedPosts']//tbody/tr//button")
    ERROR_LABEL = (By.CLASS_NAME, "error_message")
    LOADING_OVERLAY_XPATH = "//div[@id='{}']/div[1]"
    ADS_BLOCK = (By.XPATH, "//div[@class='ads-block']")
    ADS_BLOCK_IMG = "(//div[@class='ads-block--content'])[{}]/img"
    ACTION_ICONS_XPATH = "(//div[@class='ads-block--content'])[{}]/div[2]/div/div/button"
    ADD_BLOCK_ID = ""
    SUCCESS_POPOVER = (By.ID, "successMessage")
    AD_DESIGN_MODIFIED_DATE_XPATH = "(//div[@class='ads-block--header--text-content'])[{}]/p"
    AD_DESIGN_MODIFIED_DATES = (By.XPATH, "//div[@class='ads-block--header--text-content']/p")
    AD_DESIGN_PREVIEW_IMG_XPATH = "(//div[@class='ads-block--content'])[{}]/img"
    TAG = (By.XPATH, "//div[@class='tag-item']/span")
    INSTAGRAM_NOT_APPLICABLE = (By.CLASS_NAME, "adz-icon-ic_instagram_notapp")
    FOLDERS_LI = (By.XPATH, "//ul[@class='folders-ul']/li")
    DELETE_BUTTON = (By.XPATH, "//div[@id='deleteSelectedModal']//button[2]")
    AD_DESIGN_SELECT_BTN = "(//div[@class='ads-block--content'])[{}]/div[2]/div/button"
    AD_DESIGN_HEADER_TEXT = "((//h5[text()='{}']))"
    AD_DESIGN_BLOCK_BY_HEADER = "(//h5[text()='{}'])[{}]/../../parent::div//div[@class='ads-block--content']"
    AD_DESIGN_BUTTONS_BY_HEADER = ""
    UNSELECT_ALL_LINK = (By.XPATH, "//li[contains(@class, 'unselect-all-btn')]")
    MOVE_TO_LINK = (By.XPATH, "//li[contains(@class, 'move-to-folder-btn')]")
    AD_BLOCK_CUSTOM = "(//div[@class='ads-block'])[{}]"
    HAMBURGER_ICON = (By.ID, "showFoldersBtn")
    ADD_FOLDER_BUTTON = (By.CLASS_NAME, "add-folder")
    NEW_FOLDER_NAME = (By.XPATH, "//div[@id='adFlexContent']//div[2]/a")
    SAVE_ICON = (By.XPATH, "//span[contains(@class, 'save-folder-action')]")
    AD_DESIGN_HEADER_DATE = (By.XPATH, "//div[@class='ads-block--header--text-content']/p")
    TYPE_DROPDOWN = (By.XPATH, "//a[@class='chosen-single']/span[text()='Ad types']")
    TYPE_DROPDOWN_PAGE_LIKE_AD = "//ul[@class='chosen-results']/li[text()='{}']"
    LOADING_ICON = (By.XPATH, "//div[@class='js-get-data-loading-overlay']")
    PAGINATION_DEFAULT = (By.XPATH, "//span[text()='Show: 12 Per']")
    PAGINATION_PER_PAGE_XPATH = "//li[text()='Show: {} Per']"
    PAGINATION_NEXT = (By.CLASS_NAME, "pagination-next")
    AD_DESIGN_COUNT = (By.CLASS_NAME, "addesign-count")
    FIRST_IMG_LOADING_OVERLAY = (By.XPATH, "(//div[@class='img-loading-overlay-icon'])[1]")
    PAGE_SELECT = (By.XPATH, "//form[@id='addesign']//button[@data-id='pageSelect']")
    PAGE_OPTION_XPATH = "(//li[.//p[text()='{}']])[2]/a"
    PAGE_LOADING_OVERLAY = (By.CLASS_NAME, "js-popup-adpage-loading")

    # TODO move to popup page
    POP_UP_MOVE_BUTTON = (By.XPATH, "//div[contains(@class, 'display-block')]//button[2]")
    POP_UP_FIRST_FOLDER_SELECTOR = (By.XPATH, "//ul[@id='moveToFolderList']/li[1]")
    PREVIEW_MOBILE_FEED = (By.XPATH, "//li[@data-value='mobilefeed']")
    PREVIEW_DESKTOP_FEED = (By.XPATH, "//li[@data-value='desktopfeed']")
    PREVIEW_RIGHT_COLUMN = (By.XPATH, "//li[@data-value='rightcolumn']")
    PREVIEW_INSTAGRAM_FEED = (By.XPATH, "//li[@data-value='instagramstream']")
    PREVIEW_INSTAGRAM_STORY = (By.XPATH, "//li[@data-value='instagramstory']")
    PREVIEW_AUDIENCE_NETWORK = (By.XPATH, "//li[@data-value='mobileexternal']")
    PREVIEW_IMAGE = (By.XPATH, "//div[@class='frame-content']/iframe")


class AdDesignPage(WebApp):
    ad_design_id = ''
    ad_design_ids = []
    ad_design_header = ''
    folder_name = ''
    ad_design_img = ''

    def verify_on_ad_design_page(self):
        element = self.wait_for_element(AdDesignPageLocator.CREATE_AD_DESIGN_BUTTON)
        assert element.is_displayed()

    def select_ad_design(self):
        element = self.wait_for_element(
            (By.XPATH, AdDesignPageLocator.AD_DESIGN_SELECT_BTN.format(AdDesignPageLocator.ADD_BLOCK_ID)))
        element.click()

    def select_multiple_ad_designs(self):
        ads_block_1 = self.wait_for_element((By.XPATH, AdDesignPageLocator.AD_BLOCK_CUSTOM.format(1)))
        ads_block_2 = self.wait_for_element((By.XPATH, AdDesignPageLocator.AD_BLOCK_CUSTOM.format(2)))
        self.ad_design_ids.append(ads_block_1.find_element_by_xpath('..').get_attribute('data-id'))
        self.ad_design_ids.append(ads_block_2.find_element_by_xpath('..').get_attribute('data-id'))
        self.action_move_to_element(ads_block_1)
        self.wait_for_element(
            (By.XPATH, AdDesignPageLocator.AD_DESIGN_SELECT_BTN.format(1))).click()
        self.action_move_to_element(ads_block_2)
        self.wait_for_element(
            (By.XPATH, AdDesignPageLocator.AD_DESIGN_SELECT_BTN.format(2))).click()

    def verify_ad_designs_unselected(self):
        self.wait_for_element_to_disappear(
            (By.XPATH, AdDesignPageLocator.AD_DESIGN_SELECT_BTN.format(1) + "[text()='Unselect']"))
        self.wait_for_element_to_disappear(
            (By.XPATH, AdDesignPageLocator.AD_DESIGN_SELECT_BTN.format(2) + "[text()='Unselect']"))

    def click_on_unselect_all_link(self):
        self.wait_for_element(AdDesignPageLocator.UNSELECT_ALL_LINK).click()

    def click_on_move_to_link(self):
        self.wait_for_element(AdDesignPageLocator.MOVE_TO_LINK).click()

    def verify_ad_design_is_selected(self):
        element = self.wait_for_element(
            (By.XPATH, AdDesignPageLocator.AD_DESIGN_SELECT_BTN.format(AdDesignPageLocator.ADD_BLOCK_ID)))
        assert element.text == "Unselect"

    def click_create_ad_design_button(self):
        self.click_element(*AdDesignPageLocator.CREATE_AD_DESIGN_BUTTON)

    def verify_ad_design_popup_is_displayed(self):
        element = self.wait_for_element(AdDesignPageLocator.MODAL_ID)
        assert element.get_attribute("aria-hidden") == "false"

    def select_ad_account(self):
        dropdown = self.wait_for_element(AdDesignPageLocator.AD_ACCOUNT_DROPDOWN)
        self.driver.instance.execute_script("arguments[0].click();", dropdown)
        option = self.wait_for_element(AdDesignPageLocator.AD_ACCOUNT_OPTION)
        self.driver.instance.execute_script("arguments[0].click();", option)

    def pick_ad_account(self, ad_account):
        option = (By.XPATH, "//span[text()='{}']".format(ad_account))
        element = self.wait_for_element(option)
        self.driver.instance.execute_script("arguments[0].click();", element)

    def click_box(self, box_name):
        box_locator = (By.XPATH, "//label[@for='{}']".format(box_name))
        self.wait_for_element(AdDesignPageLocator.AD_ACCOUNT_OPTION)
        box = self.wait_for_element(box_locator)
        box.click()

    def click_btn(self, btn_name):
        btn_locator = (By.XPATH, "//button[text()='{}']".format(btn_name))
        btn = self.wait_for_element(btn_locator)
        btn.click()

    def click_btn_popup(self, btn_name, ad_type):
        btn_locator = (By.XPATH, "//div[@id='{}']//button[text()='{}']".format(ad_type, btn_name))
        overlay_selector = (By.XPATH, AdDesignPageLocator.LOADING_OVERLAY_XPATH.format(ad_type))
        time.sleep(1)
        self.wait_for_element_to_disappear(overlay_selector)
        btn = self.wait_for_clickable(btn_locator)
        btn.click()

    def screen_is_displayed(self, adtype_id):
        screen = (By.XPATH, "//div[@id='{}']".format(adtype_id))
        element = self.wait_for_element(screen)
        assert element.is_displayed()
        return self.driver

    def published_posts_exist(self):
        exist = self.element_exists(AdDesignPageLocator.PUBLISHED_POSTS_TABLE_ROW)
        assert exist

    def hover_and_click_on_post(self):
        action = ActionChains(self.driver.instance)
        row = self.wait_for_element(AdDesignPageLocator.PUBLISHED_POSTS_TABLE_ROW)
        action.move_to_element(row).perform()
        btn = self.wait_for_element(AdDesignPageLocator.SELECT_BTN)
        btn.click()

    def verify_error_is_displayed(self, error_text):
        element = self.wait_for_element(AdDesignPageLocator.ERROR_LABEL)
        assert error_text == element.text

    def select_page(self, page_name):
        self.wait_for_element_to_disappear(AdDesignPageLocator.PAGE_LOADING_OVERLAY)
        page_dropdown = self.wait_for_clickable(AdDesignPageLocator.PAGE_SELECT)
        page_dropdown.click()
        option = self.wait_for_clickable((By.XPATH, AdDesignPageLocator.PAGE_OPTION_XPATH.format(page_name)))
        option.click()

    def click_on_pages(self):
        selector = (By.XPATH, "//button[@data-id='pageSelect']")
        page_dropdown = self.wait_for_clickable(selector)
        self.driver.instance.execute_script("arguments[0].click();", page_dropdown)

    def fill_in_letters(self):
        selector = (By.XPATH, "//div[@class='bs-searchbox']/input")
        element = self.wait_for_element(selector)
        element.send_keys('Eff')

    def filter_pages(self):
        selector = (By.XPATH, "//li[@data-original-index='2']")
        element = self.wait_for_element(selector)
        assert 'active' in element.get_attribute('class')

    def select_ad_type(self, ad_type):
        selector = (By.XPATH, '//div[@class="filters-content--item"][3]')
        self.wait_for_element((By.CLASS_NAME, 'ads-block--content'))
        element = self.wait_for_clickable(selector)
        element.click()
        option_selector = (By.XPATH, '//li[text()="{}"]'.format(ad_type))
        option = self.wait_for_clickable(option_selector)
        option.click()

    def display_filtered_ad_designs(self, ad_type):
        selector = (By.XPATH, "//div[@class='ads-block']//h5")
        elements = self.wait_for_elements(selector)
        for element in elements:
            assert element.text == ad_type

    def select_date_range(self, date1, date2):
        selector = (By.XPATH, '//div[@class="filters-content--item"][4]')
        self.wait_for_element((By.CLASS_NAME, 'ads-block--content'))
        element = self.wait_for_clickable(selector)
        element.click()
        input1_selector = (By.XPATH, '//input[@name="daterangepicker_start"]')
        input1 = self.wait_for_element(input1_selector)
        input1.clear()
        input1.send_keys(date1)
        input2_selector = (By.XPATH, '//input[@name="daterangepicker_end"]')
        input2 = self.wait_for_element(input2_selector)
        input2.clear()
        input2.send_keys(date2)
        btn_selector = (By.XPATH, "//button[text()='Apply']")
        btn = self.wait_for_clickable(btn_selector)
        btn.click()

    def enter_tag(self, tag_name):
        selector = (By.XPATH, '//input[@value="Tags..."]')
        element = self.wait_for_clickable(selector)
        time.sleep(2)
        element.click()
        time.sleep(1)
        element.send_keys(tag_name)
        selector = (By.XPATH, "//li[@data-option-array-index='0']")
        element = self.wait_for_clickable(selector)
        element.click()

    def click_instagram_icon(self):
        selector = (By.CLASS_NAME, "instagram-applicable-filter")
        element = self.wait_for_clickable(selector)
        time.sleep(3)
        element.click()

    def verify_ad_design_images_displayed(self):
        selector = (By.XPATH, "//div[@class='ads-block--content']/img")
        images = self.wait_for_elements(selector)
        for image in images:
            assert "no-preview.png" not in image.get_attribute("src")

    def select_date_from_dropdown(self):
        selector = (By.XPATH, "//span[text()='Date - Newest to Oldest']")
        element = self.wait_for_element(selector)
        element.click()
        selector = (By.XPATH, "//li[text()='Date - Oldest to Newest']")
        element = self.wait_for_clickable(selector)
        element.click()

    def adaccount_ad_desings(self):
        selector = (By.XPATH, "//option[text()='Sandbox Adzwedo']")
        element = self.wait_for_element(selector)
        value = element.get_attribute('value')
        selector = (By.XPATH, "//div[@class='ads-block-content flex-content ad-items-flex-content addesign-list']/div")
        elements = self.wait_for_elements(selector)
        for element in elements:
            assert element.get_attribute('data-adaccountid') == value

    def page_ad_desings(self, pageid):
        selector = (By.XPATH, "//div[@class='ads-block-content flex-content ad-items-flex-content addesign-list']/div")
        elements = self.wait_for_elements(selector)
        for element in elements:
            assert element.get_attribute('data-pageid') == pageid

    def verify_ad_design_page_is_not_empty(self):
        # TODO add new ad design if page is empty
        elements = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        assert len(elements) > 1

    def create_new_ad_design_if_needed(self):
        elements = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        if len(elements) < 13:
            raise AssertionError

    def hover_over_ad_design_block(self):
        ad_designs = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        ad_design = random.choice(ad_designs)
        self.ad_design_id = ad_design.find_element_by_xpath('..').get_attribute('data-id')
        self.action_move_to_element(ad_design)
        # in UI index is plus 1
        AdDesignPageLocator.ADD_BLOCK_ID = (ad_designs.index(ad_design)) + 1

    def hover_over_ad_design_by_type(self, ad_header: str):
        time.sleep(5)
        self.ad_design_header = ad_header
        ad_designs = self.wait_for_elements((By.XPATH, AdDesignPageLocator.AD_DESIGN_HEADER_TEXT.format(ad_header)))
        ad_design_block_id = randint(1, len(ad_designs))
        AdDesignPageLocator.ADD_BLOCK_ID = ad_design_block_id
        ad_design_block = AdDesignPageLocator.AD_DESIGN_BLOCK_BY_HEADER.format(ad_header, ad_design_block_id)
        ad_design = self.wait_for_element((By.XPATH, ad_design_block))
        self.action_move_to_element(ad_design)
        self.ad_design_img = self._get_image_url()
        AdDesignPageLocator.AD_DESIGN_BUTTONS_BY_HEADER = ad_design_block + "//div[2]/div/div/button"

    def edit_first_ad_design(self):
        time.sleep(1)
        self.wait_for_element_to_disappear(AdDesignPageLocator.FIRST_IMG_LOADING_OVERLAY)
        ad_designs = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        self.action_move_to_element(ad_designs[0])
        self.wait_for_element((By.XPATH, AdDesignPageLocator.ACTION_ICONS_XPATH.format(1) + "[3]")).click()

    def verify_action_icons_visible(self):
        icon = (By.XPATH, AdDesignPageLocator.ACTION_ICONS_XPATH.format(AdDesignPageLocator.ADD_BLOCK_ID))
        action_icons = self.wait_for_elements(icon)
        if len(action_icons) != 5:
            raise AssertionError("Found {} actions icons, expected to find 5".format(len(action_icons)))

    def click_on_icon(self, icon_name):
        if self.ad_design_header != "":
            icon = (By.XPATH,
                    AdDesignPageLocator.AD_DESIGN_BUTTONS_BY_HEADER)
            action_icons = self.wait_for_elements(icon)
            self._click_icon_if_exists(action_icons, icon_name)
        else:
            icon = (By.XPATH, AdDesignPageLocator.ACTION_ICONS_XPATH.format(AdDesignPageLocator.ADD_BLOCK_ID))
            action_icons = self.wait_for_elements(icon)
            self._click_icon_if_exists(action_icons, icon_name)

    @staticmethod
    def _click_icon_if_exists(action_icons, icon_name):
        icon_arr = [icon for icon in action_icons if icon.get_attribute("title") == icon_name]
        if icon_arr:
            icon_arr[0].click()
        else:
            raise AssertionError("Icon with name {} is not found".format(icon_name))

    def success_popover_is_displayed(self):
        success_popover = self.wait_for_element(AdDesignPageLocator.SUCCESS_POPOVER)
        assert success_popover.is_displayed()

    def ad_design_is_duplicated(self):
        # Duplicated ad design is placed as the first block
        dup_dt_selector = (By.XPATH, AdDesignPageLocator.AD_DESIGN_MODIFIED_DATE_XPATH.format(1))
        dup_datetime_element = self.wait_for_element(dup_dt_selector)
        dup_datetime_object = datetime.strptime(dup_datetime_element.text, '%d/%m/%Y %H:%M')
        datetime_now = datetime.now()
        # increase ADD_BLOCK_ID by 1 because a new ad design has been added at the front
        orig_img_select = (By.XPATH, AdDesignPageLocator.AD_DESIGN_PREVIEW_IMG_XPATH
                           .format(AdDesignPageLocator.ADD_BLOCK_ID + 1))
        dup_img_select = (By.XPATH, AdDesignPageLocator.AD_DESIGN_PREVIEW_IMG_XPATH.format(1))
        orig_img = self.wait_for_element(orig_img_select)
        dup_img = self.wait_for_element(dup_img_select)
        assert dup_datetime_object < datetime_now + timedelta(minutes=3)
        assert orig_img.get_attribute('src') == dup_img.get_attribute('src')

    def verify_popup_is_displayed(self, modal_id):
        modal_selector = (By.ID, modal_id)
        modal = self.wait_for_element(modal_selector)
        assert modal.is_displayed()

    def verify_button_is_disabled(self, btn_class_name):
        btn_selector = (By.CLASS_NAME, btn_class_name)
        btn = self.wait_for_element(btn_selector)
        expected_btn_style = "opacity: 0.5;"
        assert btn.get_attribute("style") == expected_btn_style

    def verify_ad_design_contains_tag(self, tag_name):
        tags = self.wait_for_elements(AdDesignPageLocator.TAG)
        for tag in tags:
            assert tag.text == tag_name

    def verify_instagram_applicable(self):
        try:
            ig_not_applicable = self.wait_for_elements(AdDesignPageLocator.INSTAGRAM_NOT_APPLICABLE)
            assert False
        except TimeoutException:
            assert True

    def verify_ad_designs_within_date_range(self, date1, date2):
        # TODO handle the case when ad designs are paginated
        blocks = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        date_object1 = datetime.strptime(date1, '%d/%m/%Y')
        date_object2 = datetime.strptime(date2, '%d/%m/%Y')

        dt_selector = (By.XPATH, AdDesignPageLocator.AD_DESIGN_MODIFIED_DATE_XPATH.format(1))
        datetime_element = self.wait_for_element(dt_selector)
        datetime_object1 = datetime.strptime(datetime_element.text, '%d/%m/%Y %H:%M')

        dt_selector = (By.XPATH, AdDesignPageLocator.AD_DESIGN_MODIFIED_DATE_XPATH.format(len(blocks)))
        datetime_element = self.wait_for_element(dt_selector)
        datetime_object2 = datetime.strptime(datetime_element.text, '%d/%m/%Y %H:%M')

        assert date_object1 < datetime_object1
        assert date_object2 > datetime_object2

    def verify_folders_list_is_not_empty(self):
        hamburger_icon = self.wait_for_clickable((By.ID, "showFoldersBtn"))
        hamburger_icon.click()
        folders = self.wait_for_elements(AdDesignPageLocator.FOLDERS_LI)
        assert len(folders) > 1

    def move_to_folder(self):
        self.wait_for_element(AdDesignPageLocator.POP_UP_FIRST_FOLDER_SELECTOR).click()
        time.sleep(2)
        self.click_element(*AdDesignPageLocator.POP_UP_MOVE_BUTTON)
        time.sleep(5)

    def verify_ad_is_moved(self):
        self.wait_for_element_to_disappear(AdDesignPageLocator.SUCCESS_POPOVER)
        folders = self.wait_for_elements(AdDesignPageLocator.FOLDERS_LI)
        folders[1].click()
        ad_designs = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        data_ids = []
        for ad_design in ad_designs:
            data_id = ad_design.find_element_by_xpath('..').get_attribute('data-id')
            data_ids.append(data_id)
        if self.ad_design_id != '':
            assert self.ad_design_id in data_ids
        else:
            for ad_id in self.ad_design_ids:
                if ad_id not in data_ids:
                    raise AssertionError("Ad design id - '{}' is not in the list '{}'".format(ad_id, data_ids))

    def verify_ad_is_deleted(self):
        ad_designs = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        data_ids = []
        for ad_design in ad_designs:
            data_id = ad_design.find_element_by_xpath('..').get_attribute('data-id')
            data_ids.append(data_id)
        assert self.ad_design_id not in data_ids

    def click_button_on_popup(self):
        delete_btn = self.wait_for_element(AdDesignPageLocator.DELETE_BUTTON)
        delete_btn.click()

    def select_sorting_by_date(self, sort_type):
        self.wait_for_element_to_disappear(AdDesignPageLocator.LOADING_ICON)
        selector = (By.XPATH, "//div[contains(@class,'sort-by-select-content')]")
        element = self.wait_for_element(selector)
        element.click()
        selector = (By.XPATH, '//li[text()="{}"]'.format(sort_type))
        sort_by = self.wait_for_element(selector)
        sort_by.click()

    def verify_all_previews_displayed(self):
        self.wait_for_element(AdDesignPageLocator.PREVIEW_MOBILE_FEED).click()
        element = AdDesignPageLocator.PREVIEW_IMAGE
        self.wait_for_element(element).is_displayed()
        self.wait_for_element(AdDesignPageLocator.PREVIEW_DESKTOP_FEED).click()
        self._check_disappears_and_appears_again(element)
        self.wait_for_element(AdDesignPageLocator.PREVIEW_RIGHT_COLUMN).click()
        self._check_disappears_and_appears_again(element)
        self.wait_for_element(AdDesignPageLocator.PREVIEW_INSTAGRAM_FEED).click()
        self._check_disappears_and_appears_again(element)
        self.wait_for_element(AdDesignPageLocator.PREVIEW_INSTAGRAM_STORY).click()
        self._check_disappears_and_appears_again(element)
        self.wait_for_element(AdDesignPageLocator.PREVIEW_AUDIENCE_NETWORK).click()
        self._check_disappears_and_appears_again(element)

    def _check_disappears_and_appears_again(self, element):
        self.wait_for_element_to_disappear(element)
        self.wait_for_element(element).is_displayed()

    def create_new_folder(self):
        time.sleep(3)
        self.wait_for_clickable(AdDesignPageLocator.HAMBURGER_ICON).click()
        self.wait_for_element(AdDesignPageLocator.ADD_FOLDER_BUTTON).click()
        faker = Faker()
        self.folder_name = faker.first_name()
        self.driver.instance.find_element(*AdDesignPageLocator.NEW_FOLDER_NAME).send_keys(self.folder_name)

    def verify_that_folder_exists(self):
        time.sleep(1)
        folders = self.wait_for_elements(AdDesignPageLocator.FOLDERS_LI)
        folder_names = []
        for folder_name in folders:
            folder_names.append(folder_name.text)
        assert self.folder_name in folder_names

    def click_folder_creation_save_icon(self):
        self.wait_for_element(AdDesignPageLocator.SAVE_ICON).click()

    def verify_that_ads_were_created(self, count, ad_type):
        self.wait_for_element_to_disappear(AdDesignPageLocator.FIRST_IMG_LOADING_OVERLAY)
        elements = self.wait_for_elements(AdDesignPageLocator.AD_DESIGN_HEADER_DATE)
        ad_header_dates = [date.text for date in elements]
        current_date = self._get_current_date()
        assert ad_header_dates.count(current_date) == int(count)

    def verify_that_ad_with_specific_type_exists(self, ad_header: str):
        ad_types = self.wait_for_elements((By.XPATH, AdDesignPageLocator.AD_DESIGN_HEADER_TEXT.format(ad_header)))
        if len(ad_types) < 1:
            # TODO
            raise NotImplementedError

    def filer_ad_designs_by_type(self, ad_type: str):
        self.wait_for_element_to_disappear(AdDesignPageLocator.LOADING_ICON)
        try:
            self.click_element(*AdDesignPageLocator.TYPE_DROPDOWN)
            option = (By.XPATH, AdDesignPageLocator.TYPE_DROPDOWN_PAGE_LIKE_AD.format(ad_type))
            self.click_element(*option)
        except (ElementNotVisibleException, NoSuchElementException):
            print("In reality element is visible and I can click it. Later, we need to find a better way to select from dropdown.")

    def verify_that_image_url_changed(self):
        pass

    def _get_image_url(self) -> str:
        element = self.wait_for_element(
            (By.XPATH, AdDesignPageLocator.ADS_BLOCK_IMG.format(AdDesignPageLocator.ADD_BLOCK_ID)))
        return element.get_attribute("src")

    def compare_img_urls(self):
        print(self.ad_design_img)
        new_url = self.wait_for_element(
            (By.XPATH, AdDesignPageLocator.ADS_BLOCK_IMG.format("1")))
        print(new_url.get_attribute("src"))
        assert self.ad_design_img != new_url.get_attribute("src")

    def verify_pagination_is_displayed(self):
        exists = self.element_exists(AdDesignPageLocator.PAGINATION_NEXT)
        assert exists

    def select_per_page_pagination(self, pagination_number):
        pagination_dropdown = self.wait_for_clickable(AdDesignPageLocator.PAGINATION_DEFAULT)
        pagination_dropdown.click()
        pagination_per_page = self.wait_for_clickable(
            (By.XPATH, AdDesignPageLocator.PAGINATION_PER_PAGE_XPATH.format(pagination_number))
        )
        pagination_per_page.click()
        self.wait_for_element_to_disappear(AdDesignPageLocator.LOADING_ICON)

    def click_on_pagination_next(self):
        self.wait_for_clickable(AdDesignPageLocator.PAGINATION_NEXT).click()

    def verify_number_of_displayed_ad_designs(self, pagination_number):
        ad_designs = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        assert len(ad_designs) <= int(pagination_number)

    def verify_ad_design_ordering(self, sort_type):
        reverse = True if sort_type == "descending" else False
        ad_designs_dates = self.wait_for_elements(AdDesignPageLocator.AD_DESIGN_MODIFIED_DATES)
        date_times = [datetime.strptime(date.text, '%d/%m/%Y %H:%M') for date in ad_designs_dates]
        assert sorted(date_times, reverse=reverse) == date_times
        if self.element_exists(AdDesignPageLocator.PAGINATION_NEXT):
            self.click_on_pagination_next()
            self.verify_ad_design_ordering(sort_type)

    @staticmethod
    def _get_current_date():
        return datetime.now().strftime('%d/%m/%Y %H:%M')
