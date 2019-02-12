from framework.webapp import WebApp
from ad_creation_screenplay.pages.basePage import BasePage
from ad_creation_screenplay.elements.element import Element
from selenium.webdriver.common.by import By


class AdCreationPage(BasePage):

    def __init__(self, context):
        self.create_ad_btn = Element(By.XPATH, "//button[text()='Create Ad']", context)
        self.loading_overlay = Element(By.CLASS_NAME, "js-get-data-loading-overlay", context)
        self.ad_account_btn = Element(By.XPATH, "(//div[@id='adcreationSteps']//button)[1]", context)
        self.ad_account_option_xpath = Element(By.XPATH, "//div[@id='adcreationSteps']//a/span[text()='{}']", context)
        super().__init__(context)




# class AdCreationPage(WebApp):
#
#     def pick_ad_account(self, ad_account):
#         self.wait_for_element_to_disappear(AdCreationPageLocator.LOADING_OVERLAY)
#         self.wait_for_clickable(AdCreationPageLocator.AD_ACCOUNT_BTN).click()
#         option = (By.XPATH, AdCreationPageLocator.AD_ACCOUNT_OPTION_XPATH.format(ad_account))
#         self.wait_for_clickable(option).click()
