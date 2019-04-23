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
    is_headless = context.config.userdata.get("headless", None)
    driver = Driver(is_headless)
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.adsdesignpage = AdDesignPage(driver)
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage.verify_on_ad_design_page()
    context.adsdesignpage.click_create_ad_design_button()


@when("I select (?P<adaccount_name>.+) from adaccount drop-down")
def step_impl(context, adaccount_name):
    """
    :type adaccount_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.pick_ad_account_on_modal(adaccount_name)


@step("I select (?P<page_name>.+) page")
def step_impl(context, page_name):
    """
    :type page_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_page(page_name)


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
    is_headless = context.config.userdata.get("headless", None)
    driver = Driver(is_headless)
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.adsdesignpage = AdDesignPage(driver)
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage.verify_on_ad_design_page()
    context.adsdesignpage.click_create_ad_design_button()
    if adtype_id == 'leadAd':
        context.adsdesignpage.select_page('Test page')
    context.adsdesignpage.click_box(adtype_id)
    context.adsdesignpage.click_btn("Next")
    context.ad_type = adtype_id + "Type"
    context.adsdesignpage.screen_is_displayed(context.ad_type)
    context.popup_window = PopUpWindow(driver)
    context.design_count = context.adsdesignpage._get_design_count()


@when('I click on (?P<box_name>.+) box')
def step_impl(context, box_name):
    """
    :param box_name:
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_box(box_name)


@step("I (?P<choose_or_upload>.+) a single video")
def step_impl(context, choose_or_upload):
    """
    :type choose_or_upload: str
    :type context: behave.runner.Context
    """
    context.popup_window.select_single_video_block(context.ad_type)
    context.popup_window.upload_file("video", context.ad_type, choose_or_upload)


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


@step('I select an option from "Lead form" select box')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


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


@step("I upload a single image for (?P<ad_type>.+)")
def step_impl(context, ad_type):
    """
    :type ad_type: str
    :type context: behave.runner.Context
    """
    context.popup_window.upload_file("image", ad_type)


@step("I click on plus button next to (?P<field_type>.+) field")
def step_impl(context, field_type):
    """
    :type field_type: str
    :type context: behave.runner.Context
    """
    context.popup_window.add_one_more_input(field_type, context.ad_type)


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


@then("I should see (?P<count>.+) newly created (?P<ad_type>.+) designs")
def step_impl(context, count, ad_type):
    """
    :type ad_type: str
    :type count: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_that_ads_were_created(count, ad_type, context)


@step("I (?P<choose_or_upload>.+) multiple images as a slideshow")
def step_impl(context, choose_or_upload):
    """
    :type choose_or_upload: str
    :type context: behave.runner.Context
    """
    context.popup_window.select_slideshow_block(context.ad_type)
    context.popup_window.upload_file("slideshow", context.ad_type, choose_or_upload)
    #context.popup_window.upload_file("slideshow", context.ad_type, choose_or_upload)


@when("I upload a video file")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.popup_window.upload_file("video")


@step("I edit the (?P<field_type>.+) field")
def step_impl(context, field_type):
    """
    :type field_type: str
    :type context: behave.runner.Context
    """
    context.popup_window.edit_text_input_value(field_type, context.ad_type)


@when("I choose 1 image on each on of 3 cards")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for i in range(3):
        pass
