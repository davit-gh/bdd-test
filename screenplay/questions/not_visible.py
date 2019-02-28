from screenplay.questions.question import Question
from screenplay.interactions.is_displayed import NotVisible

class NotDisplayed(Question):

    def __init__(self, context):
        super().__init__(context)
        self._length = None

    def modal(self, random_index):
        #random_index = self.context.random_index if hasattr(self.context, 'random_index') else None
        self._element = self.context.optimization_locators.rule_creation_modal.set_parameters(random_index)
        return self

    def rule_modal(self):
        self._element = self.context.optimization_locators.assign_rule_modal
        return self

    def checkbox(self):
        self._element = self.context.optimization_locators.assign_rule_chbx
        return self

    def perform_as(self, actor):
        actions = (
            NotVisible(self.context).element(self._element),
        )
        return actor.attempts_to("dummy", *actions)