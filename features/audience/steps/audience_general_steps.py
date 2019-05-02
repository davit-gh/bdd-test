from behave import *
from features.pages.login_page import LoginPage
from features.pages.audiences import AudiencePage
from features.pages.nav_menu import NavigationMenu
from webdriver import Driver

use_step_matcher("re")


@given("Audience page is paginated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    is_headless = context.config.userdata.get("headless", None)
    driver = Driver(is_headless)
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.audiencepage = AudiencePage(driver)
    context.navmenu.navigate_to_page("Audience")
    context.audiencepage.verify_on_audiences_page()
    context.audiencepage.verify_audiences_page_is_paginated()

@step("I select (?P<pagination_number>.+) Audiences Per Page from the pagination drop-down")
def step_impl(context, pagination_number):
    """
    :type pagination_number: str
    :type context: behave.runner.Context
    """
    context.audiencepage.select_per_page_pagination(pagination_number)

@when("I click on Next pagination link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.click_on_pagination_next()

@then("Less than or equal to (?P<pagination_number>\d+) audiences are displayed")
def step_impl(context, pagination_number):
    """
    :type pagination_number: str
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_number_of_displayed_audiences(pagination_number)

@when("I select sort type (?P<sort_type>.+)")
def step_impl(context, sort_type):
    """
    :type sort_type: str
    :type context: behave.runner.Context
    """
    context.audiencepage.select_sorting_by_date(sort_type)

@then("The audiences are sorted by (?P<sort_type>.+) order of date")
def step_impl(context, sort_type):
    """
    :type sort_type: str
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_audience_ordering(sort_type)

@when("I click on Add Folder and fill in a name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.create_new_folder()

@step("I click Save icon")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.click_folder_creation_save_icon()

@then("I see the folder listed under All")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_that_folder_exists()

@when("I select (?P<ad_account>.+) Ad Account from drop-down")
def step_impl(context, ad_account):
    """
    :type ad_account: str
    :type context: behave.runner.Context
    """
    context.audiencepage.pick_ad_account(ad_account)

@step("I should see ad designs belonging to (?P<ad_account>.+) account")
def step_impl(context, ad_account):
    """
    :type ad_account: str
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_audiences_belong_to_ad_account(ad_account)

@when("I enter a date range from (?P<date1>.+) to (?P<date2>.+) in Date picker drop-down")
def step_impl(context, date1, date2):
    """
    :type date2: str
    :type context: behave.runner.Context
    :type date1: str
    """
    context.audiencepage.select_date_range(date1, date2)

@step("I should see ad designs from (?P<date1>.+) to (?P<date2>.+) date range")
def step_impl(context, date1, date2):
    """
    :type date2: str
    :type date1: str
    :type ad_number: str
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_ad_designs_within_date_range(date1, date2)

@when("I enter (?P<tag_name>.+) tag in Tags input field")
def step_impl(context, tag_name):
    """
    :type tag_name: str
    :type context: behave.runner.Context
    """
    context.audiencepage.enter_tag(tag_name)

@then("I should see audiences containing (?P<tag_name>.+) tag")
def step_impl(context, tag_name):
    """
    :type tag_name: str
    :type context: behave.runner.Context
    """
    context.audiencepage.verify_audience_contains_tag(tag_name)