import random
from ad_creation_screenplay.tasks.task import Task
from ad_creation_screenplay.interactions.click import Click, HoverAndClick

class Choose(Task):

    def __init__(self, context):
        self.context = context

    def existing_audience(self):
        hovered_audience_data_id = self.context.create_ad_locators.audiences.hover_one_of_elements()
        self.select_btn = self.context.create_ad_locators.audience_select_btn.set_parameters(hovered_audience_data_id)
        return self

    def existing_design(self):
        hovered_ad_design_data_id = self.context.create_ad_locators.ad_designs.hover_one_of_elements()
        self.select_btn = self.context.create_ad_locators.ad_design_select_btn.set_parameters(hovered_ad_design_data_id)
        return self

    def perform_as(self, actor):

        actions = (
            Click(self.context).element(self.select_btn),
            Click(self.context).element(self.context.create_ad_locators.next_btn)
        )
        actor.attempts_to("dummy", *actions)


class ChooseMultiple(Task):

    def __init__(self, context):
        self.context = context

    def existing_designs(self, count):
        self.select_btns = self.context.create_ad_locators.ad_design_select_btns
        self.count = count
        return self

    def existing_audiences(self, count):
        self.select_btns = self.context.create_ad_locators.audience_select_btns
        self.count = count
        return self

    def perform_as(self, actor):

        actions = (
            HoverAndClick(self.context).elements(self.select_btns, self.count),
            Click(self.context).element(self.context.create_ad_locators.next_btn)
        )
        actor.attempts_to("dummy", *actions)
