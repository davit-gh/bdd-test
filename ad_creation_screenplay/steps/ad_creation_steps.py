from behave import *
from ad_creation_screenplay.tasks.open_web_page import OpenWebPage
from ad_creation_screenplay.tasks.create_a_campaign import CreateCampaign
from ad_creation_screenplay.tasks.select_from_dropdown import Select
from ad_creation_screenplay.tasks.choose_audience import Choose
from ad_creation_screenplay.tasks.open_campaign_details_page import OpenCampaignDetailsPage
from ad_creation_screenplay.stage import Stage


stage = Stage()

@given("I am logged in")
def step_impl_validate_logged_in(context):
    context.execute_steps('''
            Given I am logged in
        ''')


@given("{ad_creator} is logged in")
def step_impl(context, ad_creator):
    """
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