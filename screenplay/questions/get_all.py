from screenplay.questions.question import Question
from screenplay.interactions.get import Get
from screenplay.interactions.wait import WaitForOverlayToDisappear

class GetAll(Question):

    def __init__(self, context):
        super().__init__(context)
        self._length = None

    def adsets(self):
        self.elements = self.context.create_ad_locators.adsets_ready_to_publish
        return self

    def rule_names(self):
        self.elements = self.context.optimization_locators.existing_rule_names
        return self

    def rules(self):
        self.elements = self.context.optimization_locators.existing_rules
        return self

    def length(self):
        self._length = True
        return self

    def perform_as(self, actor):
        actions = ()
        if self._length:
            actions += (Get(self.context).length_of().elements(self.elements),)
        else:
            actions += (
                WaitForOverlayToDisappear(self.context).element(self.context.optimization_locators.success_message),
                Get(self.context).elements(self.elements).texts()
            )

        return actor.attempts_to("dummy", *actions)