from behave import *

use_step_matcher("re")


@given("Edit Audience modal is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps('''
                Given I am on Audience page
                And At least one audience is created
                When I hover over the audience
                And I click on Edit action button
                Then Edit/Create audience modal is opened
            ''')


@when("I edit Locations field and add (?P<location_number>.+) locations")
def step_impl(context, location_number):
    """
    :type location_number: str
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'Not implemented')


@step("I click on (?P<button_name>.+) button on (?P<modal_id>.+) popup")
def step_impl(context, button_name, modal_id):
    """
    :type context: behave.runner.Context
    :type modal_id: str
    :type ad_type: str
    """
    context.audiencemodal.click_btn_popup(button_name, modal_id)
