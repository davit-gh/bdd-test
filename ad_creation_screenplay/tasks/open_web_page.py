from ad_creation_screenplay.tasks.task import Task
from ad_creation_screenplay.interactions.open import Open
from ad_creation_screenplay.interactions.fill import Fill
from ad_creation_screenplay.interactions.click import Click
from ad_creation_screenplay.pages.loginPage import LoginPageLocator
from ad_creation_screenplay.pages.createAdPage import AdCreationPage
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

    def perform_as(self, actor):
        actions = (
            Open(self.context).page(self.page_name),
            Fill(self.context).value(actor.email).into_field(self.context.login_page_locators.username_field),
            Fill(self.context).value(actor.password).into_field(self.context.login_page_locators.password_field),
            Click(self.context).element(self.context.login_page_locators.submit_btn)
        )
        return actor.attempts_to("dummy", *actions)