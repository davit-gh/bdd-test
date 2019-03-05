from screenplay.tasks.task import Task
from screenplay.interactions.fill import Fill
from screenplay.interactions.click import Click
from faker import Faker

class Create(Task):

    def __init__(self, context):
        self.context = context
        self.elements_to_click = []

    def campaign(self, campaign_type):
        self.elements_to_click = [
            self.context.create_ad_locators.get_element("campaign_type", campaign_type),
            self.context.create_ad_locators.next_btn
        ]
        self._element = self.context.create_ad_locators.get_element("campaign_title_field")
        return self

    def rule(self):
        self._element = self.context.optimization_locators.get_element("rule_name_field")
        return self

    def by_random_name(self):
        faker = Faker()
        self.context.name = faker.first_name()
        return self

    def perform_as(self, actor):
        actions = [
            Fill(self.context).value(self.context.name).into_field(self._element),
        ]
        actions += [Click(self.context).element(element) for element in self.elements_to_click if self.elements_to_click]
        return actor.attempts_to("dummy", *actions)