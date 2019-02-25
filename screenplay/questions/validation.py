from screenplay.questions.question import Question
from screenplay.interactions.get import Get

class Validation(Question):

    def __init__(self, context):
        super().__init__(context)

    def error(self):
        self.error_field =self.context.create_ad_locators.validation_error_field
        return self

    def perform_as(self, actor):

        actions = (
            Get(self.context).text().from_element(self.error_field),
        )
        return actor.attempts_to("dummy", *actions)