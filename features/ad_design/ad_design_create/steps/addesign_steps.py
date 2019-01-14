from behave import *
from features.pages.login_page import LoginPage
from features.pages.ad_design import AdDesignPage
from features.pages.nav_menu import NavigationMenu
from features.pages.popup_window import PopUpWindow
from webdriver import Driver
use_step_matcher("re")


@given("Ad Design creation popup is opened")
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
    context.adsdesignpage.click_create_ad_design_button()


@when("I select an Ad Account from adaccount drop-down")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_ad_account()


@step("I select a page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('I click on (?P<button_name>.+) button')
def step_impl(context, button_name):
    """
    :type button_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_btn(button_name)


@then("I should see (?P<adtype_id>.+) creation screen")
def step_impl(context, adtype_id):
    """
    :type adtype_id: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.screen_is_displayed(adtype_id)


@given("I am on (?P<adtype_id>.+) creation screen")
def step_impl(context, adtype_id):
    """
    :type adtype_id: str
    :type context: behave.runner.Context
    """
    driver = Driver()
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.adsdesignpage = AdDesignPage(driver)
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage.verify_on_ad_design_page()
    context.adsdesignpage.click_create_ad_design_button()
    context.adsdesignpage.click_box(adtype_id)
    context.adsdesignpage.click_btn("Next")
    context.adsdesignpage.screen_is_displayed(adtype_id + "Type")
    context.popup_window = PopUpWindow(driver)


@when('I click on (?P<box_name>.+) box')
def step_impl(context, box_name):
    """
    :param box_name:
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_box(box_name)


@step("I upload an image")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I upload an image')


@step("I fill in the required fields")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I fill in the required fields')


@then("I should see the newly created (?P<design_name>.+) design")
def step_impl(context, design_name):
    """
    :type design_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_is_created(design_name)


@step("I upload a single video")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.popup_window.select_single_video_block()
    context.popup_window.upload_file("video")


@step("I upload images")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I upload images')


@step("Published posts exist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.published_posts_exist()


@when("I select a post")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.hover_and_click_on_post()


@when("Published posts does not exist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.published_posts_doesnot_exist()


@then("I should see an error message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I should see an error message')


@step('"Lead form" select box contains at least 1 option')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And "Lead form" select box contains at least 1 option')


@step('I select an option from "Lead form" select box')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I select an option from "Lead form" select box')


@then('I should see a validation error (?P<error_msg>.+)')
def step_impl(context, error_msg):
    """
    :type error_msg: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_error_is_displayed(error_msg)


@step("I click on (?P<button_name>.+) button on (?P<ad_type>.+) popup")
def step_impl(context, button_name, ad_type):
    """
    :type context: behave.runner.Context
    :type button_name: str
    :type ad_type: str
    """
    context.adsdesignpage.click_btn_popup(button_name, ad_type)


@when("I fill in the required post link URL")
def step_impl_fill_in_required_url(context):
    """
    :type context: behave.runner.Context
    """

    context.popup_window.enter_link_url("0")


@step("I upload a single image")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.popup_window.upload_file("image")


@step("I click on plus button next to URL field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.popup_window.add_one_more_post_link_input()


@step("I fill in another URL")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.popup_window.enter_link_url("1")


@step("I fill in a headline text")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.popup_window.enter_headline()


@then("I should see 2 newly created Link Ad designs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_that_ads_were_created()


@step("I upload multiple images as a slideshow")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.popup_window.select_slideshow_block()
    context.popup_window.upload_file("slideshow")
    context.popup_window.upload_file("slideshow")