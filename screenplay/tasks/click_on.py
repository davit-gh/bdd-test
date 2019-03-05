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
        self._wait = self.context.optimization_locators.datatable_overlay2
        return self

    def icon(self, name, index):
        index = "[{}]".format(index)
        self._element = self.context.optimization_locators.icons.set_parameters(name, index)
        return self

    def button(self, btn_name):
        self._element = self.context.optimization_locators.get_element(btn_name)
        r_ind = self.context.random_index if hasattr(self.context, "random_index") else ""
        if btn_name == "Duplicate" or btn_name == "Delete":
            self._element = self.context.optimization_locators.ddown_opt.set_parameters(r_ind, btn_name)
        return self

    def randomly_chosen_icon(self, icon_class):
        self._elements = self.context.optimization_locators.icons.set_parameters(icon_class, '')
        self._wait = self.context.optimization_locators.datatable_overlay1
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
        if self._campaign:
            actions += (
                WaitForOverlayToDisappear(self.context).element(self._wait),
                Click(self.context).element(self._campaign),
                Click(self.context).element(self._element)
            )
        elif self._multiple:
            actions += (
                ClickMultiple(self.context).checkboxes(self.elements, self.count),
                Click(self.context).element(self.split_switch),
                Click(self.context).element(self.context.create_ad_locators.next_btn)
            )
        elif self._one_of:
            actions += (
                #WaitForOverlayToDisappear(self.context).element(self.context),
                Click(self.context).one_of_elements(self._elements),
            )
        else:
            actions += (
                WaitForOverlayToDisappear(self.context).element(self.context.optimization_locators.datatable_overlay1),
                WaitForOverlayToDisappear(self.context).element(self.context.optimization_locators.datatable_overlay2),
                WaitForOverlayToDisappear(self.context).element(self.context.optimization_locators.success_message),
                Click(self.context).element(self._element),
            )

        return actor.attempts_to("dummy", *actions)