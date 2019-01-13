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
    driver = Driver()
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.adsdesignpage = AdDesignPage(driver)
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage.verify_on_ad_design_page()


@step("The page contains ad designs of all 6 objectives")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I can see thumbnail images for all the ad designs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_images_displayed()


@given("Ad Design page contains at least 13 ad designs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = Driver()
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.adsdesignpage = AdDesignPage(driver)
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage.verify_on_ad_design_page()


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