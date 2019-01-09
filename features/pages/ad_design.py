import random
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from framework.webapp import WebApp


class AdDesignPageLocator(object):

    CREATE_AD_DESIGN_BUTTON = (By.ID, "createAdDesignBtn")
    MODAL_ID = (By.ID, "createAdDesignModal")
    AD_ACCOUNT_OPTION = (By.XPATH, "//span[text()='Sandbox Adzwedo']")
    AD_ACCOUNT_DROPDOWN = (By.CLASS_NAME, "ad-account-select")
    PUBLISHED_POSTS_TABLE_ROW = (By.XPATH, "//div[@id='selectedByPublishedPosts']//tbody/tr")
    SELECT_BTN = (By.XPATH, "//div[@id='selectedByPublishedPosts']//tbody/tr//button")
    ERROR_LABEL = (By.CLASS_NAME, "error_message")
    LOADING_OVERLAY = (By.CLASS_NAME, "loading-overlay-popups")
    ADS_BLOCK = (By.XPATH, "//div[@class='ads-block']")
    ACTION_ICONS_XPATH = "(//div[@class='ads-block--content'])[{}]/div[2]/div/div/button"
    ADD_BLOCK_ID = ""
    SUCCESS_POPOVER = (By.ID, "successMessage")
    AD_DESIGN_MODIFIED_DATE_XPATH = "(//div[@class='ads-block--header--text-content'])[{}]/p"
    AD_DESIGN_PREVIEW_IMG_XPATH = "(//div[@class='ads-block--content'])[{}]/img"
    TAG = (By.XPATH, "//div[@class='tag-item']/span")
    INSTAGRAM_NOT_APPLICABLE = (By.CLASS_NAME, "adz-icon-ic_instagram_notapp")
    FOLDERS_LI = (By.XPATH, "//ul[@class='folders-ul']/li")
    DELETE_BUTTON = (By.XPATH, "//div[@id='deleteSelectedModal']//button[2]")

class AdDesignPage(WebApp):

    ad_design_id = ''

    def verify_on_ad_design_page(self):
        element = self.wait_for_element(AdDesignPageLocator.CREATE_AD_DESIGN_BUTTON)
        assert element.is_displayed()

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
        self.wait_for_loading(AdDesignPageLocator.LOADING_OVERLAY)
        btn = self.wait_for_clickable(btn_locator)
        btn.click()

    def screen_is_displayed(self, adtype_id):
        screen = (By.XPATH, "//div[@id='{}']".format(adtype_id))
        element = self.wait_for_element(screen)
        assert element.is_displayed()

    def published_posts_exist(self):
        exist = self.element_exists(AdDesignPageLocator.PUBLISHED_POSTS_TABLE_ROW)
        assert exist

    def hover_and_click_on_post(self):
        action = ActionChains(self.driver.instance)
        row = self.wait_for_element(AdDesignPageLocator.PUBLISHED_POSTS_TABLE_ROW)
        action.move_to_element(row).perform()
        btn = self.wait_for_element(AdDesignPageLocator.SELECT_BTN)
        btn.click()

    def verify_ad_is_created(self, design_name):
        element_locator = (By.XPATH, "//h5[text()='{}']".format(design_name))
        element = self.element_exists(element_locator)
        assert element

    def verify_error_is_displayed(self, error_text):
        element = self.wait_for_element(AdDesignPageLocator.ERROR_LABEL)
        assert error_text == element.text

    def select_page(self, page):
        selector = (By.XPATH, "//button[@data-id='pageSelect']")
        page_dropdown = self.wait_for_clickable(selector)
        self.driver.instance.execute_script("arguments[0].click();", page_dropdown)
        option_selector = (By.XPATH, '//p[text()="{}"]'.format(page))
        option = self.wait_for_clickable(option_selector)
        self.driver.instance.execute_script("arguments[0].click();", option)

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
        selector = (By.XPATH, "//div[@class='ads-block-content flex-content ad-items-flex-content addesign-list']//div[@class='ads-block--content']/img")
        self.select_date_range("Year To Date")
        time.sleep(3)
        ad_images = self.wait_for_elements(selector)
        assert len(ad_images) == 6

    def select_date_from_dropdown(self):
        selector = (By.XPATH, "//div[@class='filters-content--item pull-right']")
        element = self.wait_for_element(selector)
        time.sleep(3)
        element.click()
        time.sleep(3)
        selector = (By.XPATH, "//div[@class='filters-content--item pull-right']//li[text()='Date - Newest to Oldest']")
        element = self.wait_for_element(selector)
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
        assert len(elements) > 0

    def hover_over_ad_design_block(self):
        ad_designs = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        ad_design = random.choice(ad_designs)
        self.ad_design_id = ad_design.find_element_by_xpath('..').get_attribute('data-id')
        action = ActionChains(self.driver.instance)
        action.move_to_element(ad_design).perform()
        # in UI index is plus 1
        AdDesignPageLocator.ADD_BLOCK_ID = (ad_designs.index(ad_design)) + 1

    def verify_action_icons_visible(self):
        icon = (By.XPATH, AdDesignPageLocator.ACTION_ICONS_XPATH.format(AdDesignPageLocator.ADD_BLOCK_ID))
        action_icons = self.wait_for_elements(icon)
        if len(action_icons) != 5:
            raise AssertionError("Found {} actions icons, expected to find 5".format(len(action_icons)))

    def click_on_icon(self, icon_name):
        icon = (By.XPATH, AdDesignPageLocator.ACTION_ICONS_XPATH.format(AdDesignPageLocator.ADD_BLOCK_ID))
        action_icons = self.wait_for_elements(icon)
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
        assert not btn.get_attribute("style")

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
        first_folder_selector = (By.XPATH, "//ul[@id='moveToFolderList']/li[1]")
        first_folder = self.wait_for_element(first_folder_selector)
        first_folder.click()
        move_btn_selector = (By.XPATH, "//div[contains(@class, 'display-block')]//button[2]")
        move_btn = self.wait_for_clickable(move_btn_selector)
        time.sleep(7)
        move_btn.click()

    def verify_ad_is_moved(self):
        folders = self.wait_for_elements(AdDesignPageLocator.FOLDERS_LI)
        folders[1].click()
        time.sleep(3)
        ad_designs = self.wait_for_elements(AdDesignPageLocator.ADS_BLOCK)
        data_ids = []
        for ad_design in ad_designs:
            data_id = ad_design.find_element_by_xpath('..').get_attribute('data-id')
            data_ids.append(data_id)
        assert self.ad_design_id in data_ids

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

    def select_sorting_by_date(self):
        selector = (By.XPATH, "//div[contains(@class, 'chosen-with-drop')]/a")
        element = self.wait_for_element(selector)
        element.click()
        sort_by = element.find_element_by_xpath('.//li[text(), "Date - Oldest to Newest"]')
        sort_by.click()
