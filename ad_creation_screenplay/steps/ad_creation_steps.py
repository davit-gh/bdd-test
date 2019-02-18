from behave import *
from ad_creation_screenplay.tasks.open_web_page import OpenWebPage
from ad_creation_screenplay.tasks.create_a_campaign import CreateCampaign
from ad_creation_screenplay.tasks.select_from_dropdown import Select
from ad_creation_screenplay.tasks.choose import Choose, ChooseMultiple
from ad_creation_screenplay.tasks.open_campaign_details_page import OpenCampaignDetailsPage
from ad_creation_screenplay.interactions.click import Click
from ad_creation_screenplay.interactions.wait import WaitForOverlayToDisappear
from ad_creation_screenplay.questions.unpublished_ads import UnpublishedAds
from ad_creation_screenplay.questions.validation import Validation
from ad_creation_screenplay.questions.get_all import GetAll
from ad_creation_screenplay.stage import Stage

stage = Stage()


@given("{ad_creator} is logged in")
def step_impl(context, ad_creator):
    """
    :type ad_creator: str
    :type context: behave.runner.Context
    """
    OpenWebPage(context).with_name('LoginPage').perform_as(stage.call_to_stage(ad_creator))


@step("she chooses {ad_account} ad account")
def step_impl(context, ad_account):
    """
    :type context: behave.runner.Context
    """
    Select(context).from_dropdown("adaccount").option(ad_account).perform_as(stage.the_actor_in_the_spotlight())


@when("she clicks on Create Ad button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    OpenCampaignDetailsPage(context).performs_as(stage.the_actor_in_the_spotlight())


@step("she chooses {page_name} page")
def step_impl(context, page_name):
    """
    :type page_name: str
    :type context: behave.runner.Context
    """
    Select(context).from_dropdown("page").option(page_name).perform_as(stage.the_actor_in_the_spotlight())


@step("she creates a new {campaign_type} campaign")
def step_impl(context, campaign_type):
    """
    :type campaign_type: str
    :type context: behave.runner.Context
    """
    CreateCampaign(context)\
        .by_filling_in("campaign_name").choose(campaign_type).perform_as(stage.the_actor_in_the_spotlight())


@step("she chooses an existing audience")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Choose(context).existing_audience().perform_as(stage.the_actor_in_the_spotlight())

@step("she chooses {count} existing audiences")
def step_impl(context, count):
    """
    :type count: str
    :type context: behave.runner.Context
    """
    ChooseMultiple(context).existing_audiences(count).perform_as(stage.the_actor_in_the_spotlight())

@step("she chooses an {ad_design_type} ad design")
def step_impl(context, ad_design_type):
    """
    :type context: behave.runner.Context
    :type ad_design_type: str
    """
    Select(context).from_dropdown('ad_type').option(ad_design_type).perform_as(stage.the_actor_in_the_spotlight())
    Choose(context).existing_design().perform_as(stage.the_actor_in_the_spotlight())

@step("she chooses {count} {ad_design_type} ad designs")
def step_impl(context, count, ad_design_type):
    """
    :type count: str
    :type ad_design_type: str
    :type context: behave.runner.Context
    """
    Select(context).from_dropdown('ad_type').option(ad_design_type).perform_as(stage.the_actor_in_the_spotlight())
    ChooseMultiple(context).existing_designs(count).perform_as(stage.the_actor_in_the_spotlight())

@step('she clicks on {button_name} button')
def step_impl(context, button_name):
    """
    :type button_name: str
    :type context: behave.runner.Context
    """
    Click(context).element(context.create_ad_locators.next_btn).execute()

@then("The campaign is moved to Unpublished Ads")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    campaign_titles = UnpublishedAds(context).navigate_to().get_titles().perform_as(stage.the_actor_in_the_spotlight())
    assert context.campaign_title in campaign_titles

@step("she clicks on Publish Later link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    WaitForOverlayToDisappear(context).element(context.create_ad_locators.profile_overlay).execute()
    Click(context).element(context.create_ad_locators.publish_later_link).execute()

@then("she sees {validation_error} error notification")
def step_impl_validate_error_notification(context, validation_error):
    """
    :type validation_error: str
    :type context: behave.runner.Context
    """
    error = Validation(context).error().perform_as(stage.the_actor_in_the_spotlight())
    assert error == validation_error


@step("she chooses to create adset per ad design")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Click(context).element(context.create_ad_locators.adset_per_ad).execute()


@then("{count} adsets should be available for publishing")
def step_impl(context, count):
    """
    :type count: str
    :type context: behave.runner.Context
    """
    number_of_adsets = GetAll(context).adsets().perform_as(stage.the_actor_in_the_spotlight())
    assert number_of_adsets == int(count)


