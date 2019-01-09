from behave import *
from features.pages.login_page import LoginPage
from features.pages.ad_design import AdDesignPage
from features.pages.nav_menu import NavigationMenu
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
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage = AdDesignPage(driver)
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


@then("I should see (?P<screen_name>.+) creation screen")
def step_impl(context, screen_name):
    """
    :type screen_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.screen_is_displayed(screen_name)


@given("I am on (?P<screen_name>.+) creation screen")
def step_impl(context, screen_name):
    """
    :type screen_name: str
    :type context: behave.runner.Context
    """
    driver = Driver()
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.adsdesignpage = AdDesignPage(driver)
    context.navmenu = NavigationMenu(driver)
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage.verify_on_ad_design_page()
    context.adsdesignpage.click_create_ad_design_button()
    context.adsdesignpage.click_box("pagePostAd")
    context.adsdesignpage.click_btn("Next")
    context.adsdesignpage.screen_is_displayed(screen_name)


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


@step("I upload a video")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I upload a video')


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


@step("I fill in the required (?P<field_type>.+) field")
def step_impl(context, field_type):
    """
    :type field_type: str
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I fill in the required field Text field')


@step("I click on (?P<button_name>.+) button on (?P<ad_type>.+) popup")
def step_impl(context, button_name, ad_type):
    """
    :type context: behave.runner.Context
    :type button_name: str
    :type ad_type: str
    """
    context.adsdesignpage.published_posts_exist()
    context.adsdesignpage.click_btn_popup(button_name, ad_type)


@given("I am on Ad Design page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = Driver()
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.navmenu = NavigationMenu(driver)
    context.navmenu.navigate_to_page("Ad Designs")
    context.adsdesignpage = AdDesignPage(driver)
    context.adsdesignpage.verify_on_ad_design_page()

@step("At least one ad design is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_page_is_not_empty()


@when("I hover over the ad design")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.hover_over_ad_design_block()


@then("I should see 5 action icons")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_action_icons_visible()


@step("I click on (?P<icon_name>.+) icon")
def step_impl(context, icon_name):
    """
    :type icon_name: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_on_icon(icon_name)


@then("Success notification is displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.success_popover_is_displayed()


@step("The ad design is duplicated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.ad_design_is_duplicated()


@step("A new popup is displayed with id (?P<modal_id>.+)")
def step_impl(context, modal_id):
    """
    :type modal_id: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_popup_is_displayed(modal_id)


@then("The button with class (?P<btn_class>.+) is disabled")
def step_impl(context, btn_class):
    """
    :type btn_class: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_button_is_disabled(btn_class)


@step("At least one folder is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_folders_list_is_not_empty()


@step("I select a folder and click on Move")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.move_to_folder()


@then("The ad is moved into the folder")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_is_moved()


@step("The ad is deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_is_deleted()