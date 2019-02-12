from ad_creation_screenplay.tasks.task import Task
from ad_creation_screenplay.interactions.click import Click

class Select(Task):

    def __init__(self, context):
        self.context = context
        self.ad_account = None

    def from_dropdown(self, ad_account):
        self.ad_account = ad_account

        return self

    def perform_as(self, actor):
        if self.ad_account:
            Click(self.context).element(self.context.dropdown)
            Click(self.context).element(self.context.option)