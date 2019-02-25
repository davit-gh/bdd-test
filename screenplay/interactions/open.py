from screenplay.interactions.interaction import Interaction
from config import settings

class Open(Interaction):

    def __init__(self, context):
        self.context = context
        self.url = None
        super().__init__(context)

    def custom_url(self, page_url):
        self.url = page_url

        return self

    def page(self, page_name):
        self.url = settings.login_page_url
        return self

    def execute(self):
        self.context.driver.navigate(self.url)