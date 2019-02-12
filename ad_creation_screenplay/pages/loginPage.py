from ad_creation_screenplay.pages.basePage import BasePage
from ad_creation_screenplay.elements.element import Element
from selenium.webdriver.common.by import By

class LoginPageLocator(BasePage):

    def __init__(self, context):
        self.username_field = Element(By.NAME, "email", context)
        self.password_field = Element(By.NAME, "password", context)
        self.submit_btn = Element(By.XPATH, "//input[@value='Login']", context)
        self.profile_name = Element(By.CLASS_NAME, "user_name", context)
        self.error_div = Element(By.CLASS_NAME, "alert-danger", context)
        super().__init__(context)
