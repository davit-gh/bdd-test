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
    context.audiencemodal.fill_in_and_choose_location(location_number)


@step("I click on (?P<button_name>.+) button on (?P<modal_id>.+) popup")
def step_impl(context, button_name, modal_id):
    """
    :type context: behave.runner.Context
    :type modal_id: str
    :type ad_type: str
    """
    context.audiencemodal.click_btn_popup(button_name, modal_id)


@when("I edit Languages field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_language()


@when("I edit Age and Gender fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I edit Age and Gender fields')


@when("I edit Detailed Targeting fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_targeting_demographics_or_behaviours_field(field_type="demographics")
    context.audiencemodal.fill_targeting_demographics_or_behaviours_field(field_type="exclude demographics")
    context.audiencemodal.fill_targeting_demographics_or_behaviours_field(field_type="narrow demographics")


@when("I edit Custom Audience fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_custom_audience_fields()


@when("I choose a new folder from Folders drop-down")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_folders()


@when("I Edit The Tags")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_tags()