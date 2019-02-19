from ad_creation_screenplay.pages.basePage import BasePage
from ad_creation_screenplay.elements.element import Element
from selenium.webdriver.common.by import By


class PlacementPage(BasePage):

    def __init__(self, context):
        self.position_checkboxes = Element(By.XPATH, "(//div[@class='left-col'])[1]//label[not(@class)]", context)
        self.split1 = Element(By.XPATH, "(//label[@class='switch-split'])[1]", context)
        self.split2 = Element(By.XPATH, "(//label[@class='switch-split'])[2]", context)
        super().__init__(context)

