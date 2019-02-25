from screenplay.tasks.task import Task
from screenplay.interactions.click import Click
from screenplay.interactions.wait import WaitForOverlayToDisappear

class OpenCampaignDetailsPage(Task):

    def __init__(self, context):
        self.context = context

    def performs_as(self, actor):
        actions = (
            Click(self.context).element(self.context.create_ad_locators.create_ad_btn),
            WaitForOverlayToDisappear(self.context).element(self.context.create_ad_locators.loading_overlay)
        )
        actor.attempts_to("dummy", *actions)