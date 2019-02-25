from screenplay.tasks.task import Task
from screenplay.interactions.fill import Fill
from screenplay.interactions.click import Click


class CreateCampaign(Task):

    def __init__(self, context):
        self.context = context

    def by_filling_in(self, campaing_title):
        self.context.campaign_title = campaing_title
        return self

    def choose(self, campaign_type):
        self.campaign_type = campaign_type
        return self

    def perform_as(self, actor):
        actions = (
            Fill(self.context).value(self.context.campaign_title).into_field(self.context.create_ad_locators.campaign_title_field),
            Click(self.context).element(self.context.create_ad_locators.campaign_type.set_parameters(self.campaign_type)),
            Click(self.context).element(self.context.create_ad_locators.next_btn)
        )
        return actor.attempts_to("dummy", *actions)