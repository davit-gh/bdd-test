from behave import *
from features.pages.login_page import LoginPage
from features.pages.ad_design import AdDesignPage
from features.pages.nav_menu import NavigationMenu
from webdriver import Driver

use_step_matcher("re")


@given("I am logged in")
def step_impl_validate_logged_in(context):
    """
    :type context: behave.runner.Context
    """
    driver = Driver()
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.adsdesignpage = AdDesignPage(driver)
    context.navmenu = NavigationMenu(driver)


@when('I click on "Ad Designs" tab')
def step_impl_click(context):
    """
    :type context: behave.runner.Context
    """
    context.navmenu.navigate_to_page("Ad Designs")


@then("I should see Ad Design page")
def step_impl_validate_page_is_opened(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_on_ad_design_page()
    context.adsdesignpage.close_website()


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


@when('I click on "Create Ad Design" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_create_ad_design_button()


@then("I should see a popup for Ad Design creation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_popup_is_displayed()
    context.adsdesignpage.close_website()


@when("I select (?P<ad_account>.+) Ad Account from drop-down")
def step_impl(context, ad_account):
    """
    :type ad_account: str
    :type context: behave.runner.Context
    """
    adacc_id = context.adsdesignpage.pick_ad_account(ad_account)
    context.adacc_id = adacc_id

@then("That ad account is the selected option")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I select (?P<page>.+) Page from Pages drop-down")
def step_impl(context, page):
    """
    :type page: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_page(page)


@then("That page is the selected option")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I should see ad designs from (?P<date1>.+) to (?P<date2>.+) date range")
def step_impl(context, date1, date2):
    """
    :type date2: str
    :type date1: str
    :type ad_number: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_designs_within_date_range(date1, date2)


@when("I click on Pages drop-down")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_on_pages()


@then("I enter 3 letters in the page input box")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.fill_in_letters()


@step("I should see matching pages automatically filtered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.filter_pages()


@when("I select an (?P<ad_type>.+) from Ad types drop-down")
def step_impl(context, ad_type):
    """
    :type ad_type: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_ad_type(ad_type)


@then("I should see all the ad designs of (?P<ad_type>.+) ad type")
def step_impl(context, ad_type):
    """
    :type ad_type: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.display_filtered_ad_designs(ad_type)


@when("I enter a date range from (?P<date1>.+) to (?P<date2>.+) in Date picker drop-down")
def step_impl(context, date1, date2):
    """
    :type date2: str
    :type context: behave.runner.Context
    :type date1: str
    """
    context.adsdesignpage.select_date_range(date1, date2)


@when("I enter (?P<tag_name>.+) tag in Tags input field")
def step_impl(context, tag_name):
    """
    :type tag_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.enter_tag(tag_name)


@when("I click on Instagram icon")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_instagram_icon()


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


@step("At least two of any type of ad designs are created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I select Date - Oldest to Newest")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_date_from_dropdown()


@step("I should see ad designs belonging to that account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.adaccount_ad_desings(context.adacc_id)


@step("I should see ad designs with pageid (?P<page_id>.+)")
def step_impl(context, page_id):
    """
    :type page_id: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.page_ad_desings(page_id)


@then("I should see ad designs containing (?P<tag_name>.+) tag")
def step_impl(context, tag_name):
    """
    :type tag_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_contains_tag(tag_name)


@then("I should see Instagram applicable ad designs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_instagram_applicable()


@when("I select sort type (?P<sort_type>.+)")
def step_impl(context, sort_type):
    """
    :type sort_type: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_sorting_by_date(sort_type)


@when("I select (?P<page_name>.+) Page from Ad Design Pages drop-down")
def step_impl(context, page_name):
    """
    :type page_name: str
    :type context: behave.runner.Context
    """

    context.adsdesignpage.select_page_on_ad_design_page(page_name)