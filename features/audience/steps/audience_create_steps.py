from behave import *

use_step_matcher("re")


@then("I should see Create Audience modal")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.verify_audience_modal_is_displayed()

@step('I click on Create Audience button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.click_create_audience_btn()


@given("Create Audience modal is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps('''
            Given I am on Audience page
        ''')
    context.audiencemodal.click_create_audience_btn()
    context.audiencepage.audience_modal_is_opened()


@when("I fill in and choose (?P<number_of_locations>\d+) locations")
def step_impl(context, number_of_locations):
    """
    :type number_of_locations: str
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_in_and_choose_location(number_of_locations)


@step("I click on (?P<link_number>.+) Exclude link")
def step_impl(context, link_number):
    """
    :type link_number: str
    :type context: behave.runner.Context
    """
    context.audiencemodal.click_on_exclude_link(link_number)