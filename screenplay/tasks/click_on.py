from screenplay.tasks.task import Task
from screenplay.interactions.click import ClickMultiple, Click
from screenplay.interactions.wait import WaitForOverlayToDisappear
from screenplay.pages.intermediatePages import PlacementPage

class ClickOn(Task):

    def __init__(self, context):
        self.context = context
        self._multiple = None
        self._one_of = None
        self._campaign = None

    def multiple(self, count):
        self.count = count
        self._multiple = True
        return self

    def campaign(self):
        self._campaign = self.context.optimization_locators.assign_rule_chbx
        return self

    def button(self, btn_name):
        if btn_name == "Apply":
            self._element = self.context.optimization_locators.apply_button
        else:
            self._element = self.context.optimization_locators.button.set_parameters(btn_name)
        return self

    def randomly_chosen_icon(self, icon_name):
        self._elements = self.context.optimization_locators.icons.set_parameters(icon_name)
        self._one_of = True
        return self

    def checkboxes(self):
        self.placement_page = PlacementPage(self.context)
        self.elements = self.placement_page.position_checkboxes
        return self

    def and_first_split_switch(self):
        self.split_switch = self.placement_page.split1
        return self

    def perform_as(self, actor):
        actions = ()
        actions += (Click(self.context).element(self._campaign),) if self._campaign else ()
        if self._multiple:
            actions += (
                ClickMultiple(self.context).checkboxes(self.elements, self.count),
                Click(self.context).element(self.split_switch),
                Click(self.context).element(self.context.create_ad_locators.next_btn)
            )
        elif self._one_of:
            actions += (
                Click(self.context).one_of_elements(self._elements),
                WaitForOverlayToDisappear(self.context).element(self.context.optimization_locators.datatable_overlay)
            )
        else:
            actions += (
                Click(self.context).element(self._element),
            )

        return actor.attempts_to("dummy", *actions)