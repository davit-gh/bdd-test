from screenplay.questions.question import Question
from screenplay.interactions.get import Get

class IsChecked(Question):

    def __init__(self, context):
        super().__init__(context)

    def first_checkbox(self):
        self._element = self.context.optimization_locators.assign_rule_chbx_input
        return self

    def perform_as(self, actor):

        actions = (
            Get(self.context).is_selected(self._element),
        )

        return actor.attempts_to("dummy", *actions)