from screenplay.tasks.task import Task
from screenplay.interactions.click import ClickMultiple, Click
from screenplay.pages.intermediatePages import PlacementPage

class ClickOn(Task):

    def __init__(self, context):
        self.context = context

    def several(self, count):
        self.count = count
        return self

    def checkboxes(self):
        self.placement_page = PlacementPage(self.context)
        self.elements = self.placement_page.position_checkboxes
        return self

    def and_first_split_switch(self):
        self.split_switch = self.placement_page.split1
        return self

    def perform_as(self, actor):
        actions = (
            ClickMultiple(self.context).checkboxes(self.elements, self.count),
            Click(self.context).element(self.split_switch),
            Click(self.context).element(self.context.create_ad_locators.next_btn)
        )
        return actor.attempts_to("dummy", *actions)