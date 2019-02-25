from features.pages.nav_menu import NavigationMenu
from screenplay.tasks.task import Task
from screenplay.interactions.open import Open
from screenplay.interactions.fill import Fill
from screenplay.interactions.click import Click
from screenplay.interactions.wait import WaitForOverlayToDisappear
from screenplay.pages.loginPage import LoginPageLocator
from screenplay.pages.createAdPage import AdCreationPage
from screenplay.pages.optimizationRulesPage import OptimizationRulesPage
from webdriver import Driver

class OpenWebPage(Task):

    def __init__(self, context):
        self.page_name = None
        self.driver = Driver()
        self.context = context

    def with_name(self, page_name):
        self.context.driver = self.driver
        self.context.login_page_locators = LoginPageLocator(self.context)
        self.context.create_ad_locators = AdCreationPage(self.context)
        return self

    def navigate_to(self, page_name):
        if page_name == "Optimization Rules":
            self.context.optimization_locators = OptimizationRulesPage(self.context)
        self.page_name = page_name
        return self

    def perform_as(self, actor):
        actions = (
            Open(self.context).page(self.page_name),
            Fill(self.context).value(actor.email).into_field(self.context.login_page_locators.username_field),
            Fill(self.context).value(actor.password).into_field(self.context.login_page_locators.password_field),
            Click(self.context).element(self.context.login_page_locators.submit_btn)
        )
        if self.page_name:
            actions += (
                NavigationMenu(self.context.driver, self.page_name),
                WaitForOverlayToDisappear(self.context).element(self.context.optimization_locators.overlay)
            )
        return actor.attempts_to("dummy", *actions)