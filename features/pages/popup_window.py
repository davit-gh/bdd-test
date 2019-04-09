import time
import os
from random import randint

from faker import Faker
from faker.providers import internet

from framework.webapp import WebApp
from selenium.webdriver.common.by import By


class PopUpWindowLocators(object):
    POST_LINK_INPUT = "//input[@name='postlink[{}]']"
    HEADLINE_INPUT = (
    By.XPATH, "(//textarea[@name='headline[0]' and @placeholder='Ad a brief headline about your ad'])[1]")
    INPUT_ADD_ICON_XPATH = "//div[@id='{}']//*[@name='{}']/..//span[@class='adz-icon-add_circle']"

    EDIT_UPLOAD_IMAGES = (By.ID, "addImage1")
    UPLOAD_SLIDESHOW_IMAGES = (By.ID, "addSlideshow2")
    SINGLE_VIDEO_BLOCK_XPATH = "//div[@id='{}']//a[contains(@href, 'video')]"
    SLIDESHOW_BLOCK_XPATH = "//div[@id='{}']//a[contains(@href,'#slideshow')]"
    SLIDESHOW_OVERLAY_XPATH = "//div[@id='{}']//div[contains(@class, 'slideshow-upload-loading')]"
    CREATE_SLIDESHOW_BTN_XPATH = "//div[@id='{}']//button[text()='Create Slideshow']"
    UPLOAD_SINGLE_VIDEO_FILE = (By.ID, "addVideo2")
    CREATE_BUTTON = (By.XPATH, "//div[@id='linkAdType']//button[contains(@class, 'create-button')]")
    IMAGE_CONTENT = (By.XPATH, "(//div[@class='image-content'])[1]")
    AD_EDIT_INPUT_XPATH = "//div[@id='{}']//*[@name='{}']"
    LOADING_ICON = (By.XPATH, "//div[@class='loading-overlay-popups']")
    FILE_UPLOAD_COMPLETED = (By.XPATH, "//div[@role='progressbar' and text()='100% Complete']")
    CHOOSE_EXISTING_BTN_XPATH = "//div[@id='{}']//button[text()='Choose Existing']"
    LOADING_OVERLAY = (By.CLASS_NAME, "loading-filter-getBrowseLibrary")
    EXISTING_VIDEOS = (By.XPATH, "//div[@class='select-video-box']")
    CHOOSE_VIDEO_BUTTON = (By.ID, "browse_library_done")
    PUBLISHED_RADIO_BTN = (By.XPATH, "//input[@id='publishedPage']/following-sibling::label[2]")
    LOADING_OVERLAY_XPATH = "//div[@id='{}']/div[1]"
    TAG_FIELD_XPATH = "//div[@id='{}']//input[@name='tags_list']"
    UPLOAD_IMAGE_IDS = {
        'pageLikeAdType': 'addImage1',
        'linkAdType': 'addImage2',
        'leadAdType': 'addImage3',
        'photoAdType': 'addImage4'
    }
    UPLOAD_SLIDESHOW_IDS = {
        'pageLikeAdType': 'addSlideshow1',
        'linkAdType': 'addSlideshow2',
        'leadAdType': 'addSlideshow3',
        'photoAdType': 'addSlideshow4'
    }
class PopUpWindow(WebApp):
    text = ''

    def enter_link_url(self, link_id: str):
        element = self.wait_for_element((By.XPATH, PopUpWindowLocators.POST_LINK_INPUT.format(link_id)))
        element.send_keys('http://example.com')

    def enter_headline(self):
        element = self.wait_for_element(PopUpWindowLocators.HEADLINE_INPUT)
        element.send_keys('example headline')

    def select_single_video_block(self, ad_type):
        overlay_selector = (By.XPATH, PopUpWindowLocators.LOADING_OVERLAY_XPATH.format(ad_type))
        time.sleep(1)
        self.wait_for_element_to_disappear(overlay_selector)
        selector = (By.XPATH, PopUpWindowLocators.SINGLE_VIDEO_BLOCK_XPATH.format(ad_type))
        element = self.wait_for_clickable(selector)
        element.click()

    def select_slideshow_block(self, ad_type):
        time.sleep(2)
        selector = (By.XPATH, PopUpWindowLocators.SLIDESHOW_BLOCK_XPATH.format(ad_type))
        self.wait_for_clickable(selector).click()
        time.sleep(1)

    def upload_file(self, file_type: str, ad_type: str, choose_or_upload=None):
        path_images = "/files/images"
        path_videos = "/files/videos"
        if file_type == "image":
            image = os.getcwd() + "{}/image1.jpg".format(path_images)
            image_field_id = PopUpWindowLocators.UPLOAD_IMAGE_IDS[ad_type]
            selector = (By.ID, image_field_id)
            self.driver.instance.find_element(*selector).send_keys(image)
        elif file_type == "video":
            if choose_or_upload == 'upload':
                video = os.getcwd() + "{}\\SampleVideo.mp4".format(path_videos)
                self.driver.instance.find_element(*PopUpWindowLocators.UPLOAD_SINGLE_VIDEO_FILE).send_keys(video)
                self.wait_for_element(PopUpWindowLocators.FILE_UPLOAD_COMPLETED, time=40)
            else:
                btn_selector = (By.XPATH, PopUpWindowLocators.CHOOSE_EXISTING_BTN_XPATH.format(ad_type))
                choose_existing_btn = self.wait_for_clickable(btn_selector)
                choose_existing_btn.click()
                self.wait_for_element_to_disappear(PopUpWindowLocators.LOADING_OVERLAY)
                videos = self.wait_for_elements(PopUpWindowLocators.EXISTING_VIDEOS)
                videos[randint(0, len(videos) - 1)].click()
                choose_video_btn = self.wait_for_clickable(PopUpWindowLocators.CHOOSE_VIDEO_BUTTON)
                choose_video_btn.click()
        elif file_type == "slideshow":
            img = os.getcwd() + "{}/image1.jpg".format(path_images)
            img1 = os.getcwd() + "{}/image2.jpg".format(path_images)
            img2 = os.getcwd() + "{}/image3.jpg".format(path_images)
            selector = (By.ID, PopUpWindowLocators.UPLOAD_SLIDESHOW_IDS[ad_type])
            element = self.find_element(*selector)
            element.send_keys(img)
            element.send_keys(img1)
            element.send_keys(img2)
            create_btn_selector = PopUpWindowLocators.CREATE_SLIDESHOW_BTN_XPATH.format(ad_type)
            overlay_selector = PopUpWindowLocators.SLIDESHOW_OVERLAY_XPATH.format(ad_type)
            create_btn = (By.XPATH, create_btn_selector)
            overlay = (By.XPATH, overlay_selector)
            self.find_element(*create_btn).click()
            self.wait_for_element_to_disappear(overlay, 200)
        elif file_type == "image_edit":
            image = os.getcwd() + "{}/image{}.jpg".format(path_images, randint(1, 3))
            self.driver.instance.find_element(*PopUpWindowLocators.EDIT_UPLOAD_IMAGES).send_keys(image)
        else:
            raise FileNotFoundError("File with type '{}' does not exist".format(file_type))

    def add_one_more_input(self, field_type, ad_type):
        selector = (By.XPATH, PopUpWindowLocators.INPUT_ADD_ICON_XPATH.format(ad_type, field_type))
        self.wait_for_element(selector).click()

    def edit_text_input_value(self, field_type, ad_type):
        faker = Faker()
        faker.add_provider(internet)
        time.sleep(2)
        selector = (By.XPATH, PopUpWindowLocators.AD_EDIT_INPUT_XPATH.format(ad_type, field_type))
        element = self.wait_for_element(selector)
        self.text = faker.name() if 'link' not in field_type else faker.url()
        element.clear()
        element.send_keys(self.text)

    def verify_edit_window_text_input_is_correct(self, field_type, ad_type):
        time.sleep(1)
        self.wait_for_element_to_disappear(PopUpWindowLocators.LOADING_ICON)
        selector = (By.XPATH, PopUpWindowLocators.AD_EDIT_INPUT_XPATH.format(ad_type, field_type))
        element = self.wait_for_element(selector)
        element_text = element.get_attribute("data-value")
        assert element_text == self.text

    def click_on_published_radio(self, ad_type):
        overlay_selector = (By.XPATH, PopUpWindowLocators.LOADING_OVERLAY_XPATH.format(ad_type))
        self.wait_for_element_to_disappear(overlay_selector)
        self.wait_for_clickable(PopUpWindowLocators.PUBLISHED_RADIO_BTN).click()

    def edit_tag_field(self, ad_type, tag_name):
        tag_field_selector = (By.XPATH, PopUpWindowLocators.TAG_FIELD_XPATH.format(ad_type))
        self.wait_for_element(tag_field_selector).send_keys(tag_name)
        pass