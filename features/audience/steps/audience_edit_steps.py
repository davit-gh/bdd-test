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
    audiences = context.audiencemodal.click_btn_popup(button_name, modal_id)
    context.audience_id = audiences[0].get_attribute("data-id")


@when("I edit (?P<field_name>.+) field")
def step_impl(context, field_name):
    """
    :type field_name: str
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_language(field_name)


@when("I edit Age and Gender fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_age()
    context.audiencemodal.select_gender()


@when("I edit Detailed Targeting fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_targeting_demographics_or_behaviours_field(field_type="Demographics, Interests or Behaviours")
    context.audiencemodal.fill_targeting_demographics_or_behaviours_field(field_type="Exclude Demographics, Interests or Behaviours")
    context.audiencemodal.fill_targeting_demographics_or_behaviours_field(field_type="Narrow Demographics, Interests or Behaviours")


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


@then("The location is changed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.verify_locations_is_changed(context.audience_id)


@then("The language is changed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.verify_languages_is_changed(context.audience_id)


@then("The age and gender is changed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.verify_age_gender_are_changed(context.audience_id)


@then("The interest are changed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.verify_interests_are_changed(context.audience_id)


@then("The custom audience change is saved")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.verify_custom_audience_is_changed(context.audience_id)


@then("The audience is moved to that folder")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.verify_moved_to_folder(context.audience_id)
