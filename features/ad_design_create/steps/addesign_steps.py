from behave import *
from features.pages.login_page import LoginPage
from features.pages.ad_design import AdDesignPage
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
    context.adsdesignpage = AdDesignPage(driver)
    context.adsdesignpage.click_menu()
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
    context.adsdesignpage = AdDesignPage(driver)
    context.adsdesignpage.click_menu()
    context.adsdesignpage.verify_on_ad_design_page()
    context.adsdesignpage.click_create_ad_design_button()
    context.adsdesignpage.click_box(adtype_id)
    context.adsdesignpage.click_btn("Next")
    context.adsdesignpage.screen_is_displayed(adtype_id + "Type")


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


@step("I click on (?P<button_name>.+) button on (?P<ad_type>.+) popup")
def step_impl(context, button_name, ad_type):
    """
    :type context: behave.runner.Context
    :type button_name: str
    :type ad_type: str
    """
    context.adsdesignpage.click_btn_popup(button_name, ad_type)


