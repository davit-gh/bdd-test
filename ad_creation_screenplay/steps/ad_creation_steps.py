from behave import *
from ad_creation_screenplay.tasks.open_web_page import OpenWebPage
from ad_creation_screenplay.tasks.select_from_dropdown import Select
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
    Select(context).from_dropdown(ad_account).perform_as(stage.the_actor_in_the_spotlight())


@when("she clicks on Create Ad button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    OpenCampaignDetailsPage(context).performs_as(stage.the_actor_in_the_spotlight())