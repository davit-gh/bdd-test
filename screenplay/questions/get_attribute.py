from screenplay.questions.question import Question
from screenplay.interactions.get import Get

class GetAttribute(Question):

    def __init__(self, context):
        super().__init__(context)

    def element(self, name):
        self._element = self.context.optimization_locators.get_element(name)
        return self

    def attribute(self, attr_name):
        self._attr_name = attr_name
        return self

    def perform_as(self, actor):

        actions = (
            Get(self.context).from_element(self._element).attribute(self._attr_name),
        )

        return actor.attempts_to("dummy", *actions)