from screenplay.questions.question import Question
from screenplay.interactions.is_displayed import NotVisible

class NotDisplayed(Question):

    def __init__(self, context):
        super().__init__(context)
        self._length = None

    def modal(self, random_index):
        #random_index = self.context.random_index if hasattr(self.context, 'random_index') else None
        self._modal = self.context.optimization_locators.rule_creation_modal.set_parameters(random_index)
        return self

    def perform_as(self, actor):
        actions = (
            NotVisible(self.context).element(self._modal),
        )

        return actor.attempts_to("dummy", *actions)