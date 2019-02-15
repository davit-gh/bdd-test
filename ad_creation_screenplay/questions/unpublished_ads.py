from ad_creation_screenplay.questions.question import Question
from features.pages.nav_menu import NavigationMenu
from ad_creation_screenplay.interactions.get import Get
from ad_creation_screenplay.interactions.wait import WaitForOverlayToDisappear
from ad_creation_screenplay.pages.unpublishedAds import UnpublishedAdsPage

class UnpublishedAds(Question):

    def __init__(self, context):
        super().__init__(context)

    def navigate_to(self):
        nav_menu = NavigationMenu(self.context.driver)
        nav_menu.navigate_to_page("Unpublished Ads")

        return self

    def get_titles(self):
        unpublishedAdsPage = UnpublishedAdsPage(self.context)
        self.campaign_titles = unpublishedAdsPage.campaign_titles
        return self

    def perform_as(self, actor):

        actions = (
            WaitForOverlayToDisappear(self.context).element(self.context.create_ad_locators.loading_overlay),
            Get(self.context).campaign_titles(self.campaign_titles)
        )
        return actor.attempts_to("dummy", *actions)