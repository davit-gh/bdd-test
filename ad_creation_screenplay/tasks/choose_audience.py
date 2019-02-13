import random
from ad_creation_screenplay.tasks.task import Task
from ad_creation_screenplay.interactions.click import Click
from ad_creation_screenplay.elements.element import Element

class Choose(Task):

    def __init__(self, context):
        self.context = context

    def existing_audience(self):
        hovered_audience_data_id = self.context.create_ad_locators.audiences.hover_one_of_elements()
        self.hovered_audience_data_id = hovered_audience_data_id

        return self

    def perform_as(self, actor):
        actions = (
            Click(self.context).element(self.audience),
            Click(self.context).element(self.context.create_ad_locators.next_btn)
        )
        actor.attempts_to("dummy", *actions)