import time
import os
from faker import Faker

from framework.webapp import WebApp
from selenium.webdriver.common.by import By


class PopUpWindowLocators(object):
    POST_LINK_INPUT = "//input[@name='postlink[{}]']"
    HEADLINE_INPUT = (
    By.XPATH, "(//textarea[@name='headline[0]' and @placeholder='Ad a brief headline about your ad'])[1]")
    POST_LINK_INPUT_ADD_ICON = (By.XPATH, "//input[@name='postlink[0]']/..//span[@class='adz-icon-add_circle']")
    UPLOAD_IMAGES = (By.ID, "addImage2")
    UPLOAD_SLIDESHOW_IMAGES = (By.ID, "addSlideshow2")
    SINGLE_VIDEO_BLOCK = (By.XPATH, "//a[@href='#videoTypeLinkAD']")
    SLIDESHOW_BLOCK = (By.XPATH, "//a[@href='#slideshowTypeLinkAD']")
    UPLOAD_SINGLE_VIDEO_FILE = (By.ID, "addVideo2")
    CREATE_BUTTON = (By.XPATH, "//div[@id='linkAdType']//button[contains(@class, 'create-button')]")
    IMAGE_CONTENT = (By.XPATH, "(//div[@class='image-content'])[1]")
    AD_EDIT_TEXT_INPUT = (By.XPATH, "(//textarea[@name='text[0]'])[1]")
    LOADING_ICON = (By.XPATH, "//div[@class='loading-overlay-popups']")
    FILE_UPLOAD_COMPLETED = (By.XPATH, "//div[@role='progressbar' and text()='100% Complete']")


class PopUpWindow(WebApp):
    text = ''

    def enter_link_url(self, link_id: str):
        element = self.wait_for_element((By.XPATH, PopUpWindowLocators.POST_LINK_INPUT.format(link_id)))
        element.send_keys('http://example.com')

    def enter_headline(self):
        element = self.wait_for_element(PopUpWindowLocators.HEADLINE_INPUT)
        element.send_keys('example headline')

    def select_single_video_block(self):
        self.wait_for_element(PopUpWindowLocators.SINGLE_VIDEO_BLOCK).click()

    def select_slideshow_block(self):
        self.wait_for_element(PopUpWindowLocators.SLIDESHOW_BLOCK).click()

    def upload_file(self, file_type: str, file="image.jpg"):
        path_images = "\\files\\images"
        path_videos = "\\files\\videos"
        if file_type == "image":
            image = os.getcwd() + "{}\\{}".format(path_images, file)
            self.driver.instance.find_element(*PopUpWindowLocators.UPLOAD_IMAGES).send_keys(image)
        elif file_type == "video":
            video = os.getcwd() + "{}\\SampleVideo.mp4".format(path_videos)
            self.driver.instance.find_element(*PopUpWindowLocators.UPLOAD_SINGLE_VIDEO_FILE).send_keys(video)
            self.wait_for_element(PopUpWindowLocators.FILE_UPLOAD_COMPLETED, time=20)
        elif file_type == "slideshow":
            img = os.getcwd() + "{}\\image.jpg".format(path_images)
            img1 = os.getcwd() + "{}\\image1.jpg".format(path_images)
            img2 = os.getcwd() + "{}\\image2.jpg".format(path_images)
            self.driver.instance.find_element(*PopUpWindowLocators.UPLOAD_SLIDESHOW_IMAGES).send_keys(img)
            self.driver.instance.find_element(*PopUpWindowLocators.UPLOAD_SLIDESHOW_IMAGES).send_keys(img1)
            self.driver.instance.find_element(*PopUpWindowLocators.UPLOAD_SLIDESHOW_IMAGES).send_keys(img2)
        else:
            raise FileNotFoundError("File with type '{}' does not exist".format(file_type))

    def add_one_more_post_link_input(self):
        self.wait_for_element(PopUpWindowLocators.POST_LINK_INPUT_ADD_ICON).click()

    def edit_text_input_value(self):
        faker = Faker()
        time.sleep(2)
        element = self.wait_for_element(PopUpWindowLocators.AD_EDIT_TEXT_INPUT)
        self.text = faker.name()
        element.clear()
        element.send_keys(self.text)

    def verify_edit_window_text_input_is_correct(self):
        time.sleep(1)
        self.wait_for_element_to_disappear(PopUpWindowLocators.LOADING_ICON)
        element = self.wait_for_element(PopUpWindowLocators.AD_EDIT_TEXT_INPUT)
        element_text = element.get_attribute("data-value")
        assert element_text == self.text
