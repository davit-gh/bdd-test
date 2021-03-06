from behave import *
from features.pages.login_page import LoginPage
from features.pages.ad_design import AdDesignPage
from features.pages.nav_menu import NavigationMenu
from webdriver import Driver

use_step_matcher("re")


@given("I am on Ad Design page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    is_headless = context.config.userdata.get("headless", None)
    driver = Driver(is_headless)
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.adsdesignpage = AdDesignPage(driver)
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage.verify_on_ad_design_page()


@then("I can see thumbnail images for all the ad designs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_images_displayed()


@given("Ad Design page is paginated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    is_headless = context.config.userdata.get("headless", None)
    driver = Driver(is_headless)
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.adsdesignpage = AdDesignPage(driver)
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage.verify_on_ad_design_page()
    context.adsdesignpage.verify_pagination_is_displayed()

@when("I click on Add Folder and fill in a name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.create_new_folder()


@then("I see the folder listed under All")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_that_folder_exists()


@step("I click Save icon")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_folder_creation_save_icon()


@step("I select (?P<pagination_number>.+) Ads Per Page from the pagination drop-down")
def step_impl(context, pagination_number):
    """
    :type pagination_number: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_per_page_pagination(pagination_number)


@when("I click on Next pagination link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_on_pagination_next()


@then("Less than or equal to (?P<pagination_number>\d+) ad designs are displayed")
def step_impl(context, pagination_number):
    """
    :type pagination_number: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_number_of_displayed_ad_designs(pagination_number)


@then("The ad designs are sorted by (?P<sort_type>.+) order of date")
def step_impl(context, sort_type):
    """
    :type sort_type: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_ordering(sort_type)

@step("At least one ad design is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_page_is_not_empty()

@when("I select sort type (?P<sort_type>.+)")
def step_impl(context, sort_type):
    """
    :type sort_type: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_sorting_by_date(sort_type)


@when("I filter ad designs of type (?P<type>.+)")
def step_impl(context, type):
    """
    :type context: behave.runner.Context
    :type type: str
    """
    context.adsdesignpage.filer_ad_designs_by_type(type)


@when("I open ad creation modal")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_create_ad_design_button()


@step("I change the selected page to (?P<page_name>.+)")
def step_impl(context, page_name):
    """
    :type page_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_page(page_name)


@then("The page on Ad Design page also changes to (?P<page_name>.+)")
def step_impl(context, page_name):
    """
    :type page_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_page_syincing(page_name)