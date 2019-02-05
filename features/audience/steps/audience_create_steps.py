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


@when("I fill in and choose (?P<number_of_locations>.+) locations")
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


@step("I select age range")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_age()


@step("I select a gender")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.select_gender()


@step("I switch the (?P<buttons>.+) SPLIT buttons to on")
def step_impl(context, buttons):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.click_on_split_button(buttons)


@step("I click on Create button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.click_create_button()


@step("I choose a folder from FOLDERS drop-down")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_folders()


@step("I add (?P<nr_of_tags>.+) tags in TAGS field")
def step_impl(context, nr_of_tags):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I add 2 tags in TAGS field')


@step("I fill in and choose users in Users Connect To field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_users_connect_to_input()


@step("I fill in and choose users in Friends of users connected to field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_friends_of_user_connected_to()


@step("I fill in and choose 2 Demographics, Interests or Behaviours")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_targeting_demographics_or_behaviours_field(field_type="Demographics, Interests or Behaviours")


@step("I fill in and choose an excluded Demographics, Interests or Behaviours")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_targeting_demographics_or_behaviours_field(field_type="Exclude Demographics, Interests or Behaviours")


@step("I fill in and choose an narrow Demographics, Interests or Behaviours")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_targeting_demographics_or_behaviours_field(field_type="Narrow Demographics, Interests or Behaviours")


@step("I fill in and choose (?P<count>.+) languages")
def step_impl(context, count):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_language("Languages", count=2)


@then("I should see new audiences")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.verify_locations_and_languages()


@step("I edit Connections fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.fill_users_connect_to_input()
    context.audiencemodal.fill_friends_of_user_connected_to()


@step("I click on all split switches")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    response = context.audiencemodal.click_on_split_buttons()
    context.potential_reach = response['potential_reach']
    context.audience_count = response['audience_count']


@then("The correct number of new audiences are created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.verify_correct_number_of_audiences_are_created(context)