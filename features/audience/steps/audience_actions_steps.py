from behave import *
from features.pages.login_page import LoginPage
from features.pages.audiences import AudiencePage
from features.pages.audience_modal import AudienceModal
from features.pages.nav_menu import NavigationMenu
from webdriver import Driver

use_step_matcher("re")

@given("I am on Audience page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = Driver()
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.audiencepage = AudiencePage(driver)
    context.audiencemodal = AudienceModal(driver)
    context.navmenu.navigate_to_page("Audience")
    context.audiencepage.verify_on_audiences_page()


@step("At least one audience is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_ad_audience_is_not_empty()


@when("I hover over the audience")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    audience_id = context.audiencepage.hover_over_audience_block()
    context.audience_id = audience_id

@then("I should see 4 action icons")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_action_icons_visible()

@step('I click on (?P<button_name>.+) action button')
def step_impl(context, button_name):
    """
    :type button_name: str
    :type context: behave.runner.Context
    """
    context.audiencepage.click_action_btn(button_name)


@then("The audience is selected")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_audience_is_selected()


@then("Edit/Create audience modal is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.audience_modal_is_opened()

@step("At least one folder is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_folders_list_is_not_empty()

@step("I select a folder and click on Move")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.move_to_folder()

@then("The audience is moved into the folder")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_audience_is_moved()

@step("I click on Delete button on popup")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.click_button_on_popup()


@then("The audience is deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_audience_is_deleted()