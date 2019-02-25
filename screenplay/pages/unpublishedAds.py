from screenplay.pages.basePage import BasePage
from screenplay.elements.element import Element
from selenium.webdriver.common.by import By


class UnpublishedAdsPage(BasePage):

    def __init__(self, context):
        self.campaign_titles = Element(By.XPATH, "//div[@class='campaign-row--header--tittle']//h2[text()]", context)
        super().__init__(context)

