from ad_creation_screenplay.tasks.task import Task
from ad_creation_screenplay.interactions.fill import Fill
from ad_creation_screenplay.interactions.click import Click


class CreateCampaign(Task):

    def __init__(self, context):
        self.context = context

    def by_filling_in(self, campaing_name):
        self.campaign_name = campaing_name
        return self

    def choose(self, campaign_type):
        self.campaign_type = campaign_type
        return self

    def perform_as(self, actor):
        actions = (
            Fill(self.context).value(self.campaign_name).into_field(self.context.create_ad_locators.campaign_name_field),
            Click(self.context).element(self.context.create_ad_locators.campaign_type.set_parameters(self.campaign_type)),
            Click(self.context).element(self.context.create_ad_locators.next_btn)
        )
        return actor.attempts_to("dummy", *actions)