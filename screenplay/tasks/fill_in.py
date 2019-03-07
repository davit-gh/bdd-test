from screenplay.tasks.task import Task
from screenplay.interactions.fill import Fill

class FillIn(Task):

    def __init__(self, context):
        self.context = context

    def in_the_field(self, name):
        self._element = self.context.optimization_locators.get_element(name)
        return self

    def value(self, value):
        self._value = value
        return self

    def perform_as(self, actor):

        actions = (
            Fill(self.context).into_field(self._element).value(self._value),
        )
        actor.attempts_to("dummy", *actions)