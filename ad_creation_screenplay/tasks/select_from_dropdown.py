from ad_creation_screenplay.tasks.task import Task
from ad_creation_screenplay.interactions.click import Click

class Select(Task):

    def __init__(self, context):
        self.context = context

    def from_dropdown(self, ddown_name):
        if ddown_name == 'adaccount':
            self.ddown_selector = self.context.create_ad_locators.ad_account_ddown
        elif ddown_name == 'page':
            self.ddown_selector = self.context.create_ad_locators.page_ddown
        elif ddown_name == 'ad_type':
            self.ddown_selector = self.context.create_ad_locators.ad_type_ddown
        self.ddown_name = ddown_name
        return self

    def option(self, option_name):
        if self.ddown_name == 'adaccount':
            self.option_selector = self.context.create_ad_locators.ad_account_option.set_parameters(option_name)
        elif self.ddown_name == 'page':
            self.option_selector = self.context.create_ad_locators.page_option.set_parameters(option_name)
        elif self.ddown_name == 'ad_type':
            self.option_selector = self.context.create_ad_locators.ad_type_option.set_parameters(option_name)
        return self

    def perform_as(self, actor):
        actions = (
            Click(self.context).element(self.ddown_selector),
            Click(self.context).element(self.option_selector)
        )
        actor.attempts_to("dummy", *actions)