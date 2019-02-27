from screenplay.tasks.task import Task
from screenplay.interactions.fill import Fill
from screenplay.interactions.click import Click
from screenplay.interactions.wait import WaitForOverlayToDisappear

class SearchFor(Task):

    def __init__(self, context):
        self.context = context

    def rule_by_name(self, rule_name):
        self._value = rule_name
        self._element = self.context.optimization_locators.rule_search_field
        self._search_icon = self.context.optimization_locators.search_icon.set_parameters("Search...")
        return self

    def campaign(self, campaign_name):
        self._value = campaign_name
        self._element = self.context.optimization_locators.campaign_search_field
        self._search_icon = self.context.optimization_locators.search_icon.set_parameters("Search by name...")
        return self

    def perform_as(self, actor):
        actions = (
            Click(self.context).element(self._element),
            Fill(self.context).value(self._value).into_field(self._element),
            Click(self.context).element(self._search_icon),
            WaitForOverlayToDisappear(self.context).element(self.context.optimization_locators.overlay)
        )
        return actor.attempts_to("dummy", *actions)