from screenplay.tasks.task import Task
from screenplay.interactions.click import Click
from screenplay.interactions.wait import WaitForOverlayToDisappear

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
        elif ddown_name == 'action':
            self.ddown_selector = self.context.optimization_locators.action_ddown
        elif ddown_name == 'cpc_cpm':
            self.ddown_selector = self.context.optimization_locators.cpc_cpm_ddown
        elif ddown_name == 'period':
            self.ddown_selector = self.context.optimization_locators.period_ddown
        self.ddown_name = ddown_name
        return self

    def option(self, option_name):
        if self.ddown_name == 'adaccount':
            self.option_selector = self.context.create_ad_locators.ad_account_option.set_parameters(option_name)
        elif self.ddown_name == 'page':
            self.option_selector = self.context.create_ad_locators.page_option.set_parameters(option_name)
        elif self.ddown_name == 'ad_type':
            self.option_selector = self.context.create_ad_locators.ad_type_option.set_parameters(option_name)
        elif self.ddown_name == 'action' or self.ddown_name == 'cpc_cpm' or self.ddown_name == 'period':
            self.option_selector = self.context.optimization_locators._option.set_parameters(option_name)
        return self

    def perform_as(self, actor):
        actions = (
            Click(self.context).element(self.ddown_selector),
            Click(self.context).element(self.option_selector)
        )
        if self.context.page_name != "Optimization Rules":
            actions += (WaitForOverlayToDisappear(self.context).elements(self.context.create_ad_locators.cc_overlays),)
        actor.attempts_to("dummy", *actions)