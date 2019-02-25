from screenplay.pages.basePage import BasePage
from screenplay.elements.element import Element
from selenium.webdriver.common.by import By


class OptimizationRulesPage(BasePage):

    def __init__(self, context):
        self.overlay = Element(By.CLASS_NAME, "optimization-rules-loading-overlay", context)
        self.existing_rules = Element(By.XPATH, "//div[@id='rule_container']/div", context)
        self.existing_rule_names = Element(By.CLASS_NAME, "rule-name", context)
        self.rule_search_field = Element(By.XPATH, "//input[@name='search_rule']", context)
        self.search_icon = Element(By.XPATH, "//input[@class='ad-input']/following-sibling::span", context)
        super().__init__(context)
