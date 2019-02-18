from ad_creation_screenplay.questions.question import Question
from ad_creation_screenplay.interactions.get import Get

class GetAll(Question):

    def __init__(self, context):
        super().__init__(context)

    def adsets(self):
        adsets = self.context.create_ad_locators.adsets_ready_to_publish
        self._adsets = adsets
        return self

    def perform_as(self, actor):
        actions = (
            Get(self.context).length_of().elements(self._adsets),
        )

        return actor.attempts_to("dummy", *actions)