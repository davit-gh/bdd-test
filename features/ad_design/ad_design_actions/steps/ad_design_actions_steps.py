from behave import *
from features.pages.login_page import LoginPage
from features.pages.ad_design import AdDesignPage
from features.pages.nav_menu import NavigationMenu
from features.pages.popup_window import PopUpWindow
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
    context.popup_window = PopUpWindow(driver)


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
def step_impl(context, icon_name: str):
    """
    :param icon_name: wanted icon
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
def step_impl(context, modal_id: str):
    """
    :param modal_id: id of wanted modal
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_popup_is_displayed(modal_id)


@then("The button with class (?P<btn_class>.+) is disabled")
def step_impl(context, btn_class: str):
    """
    :param btn_class: class of wanted button
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_button_is_disabled(btn_class)


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


@step("At least one folder is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_page_is_not_empty()
    context.adsdesignpage.verify_folders_list_is_not_empty()


@step("I click on Delete button on popup")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_button_on_popup()


@step("The ad is deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_is_deleted()


@step("Click on Select button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_ad_design()


@then("The ad designs are selected")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_is_selected()


@when("I hover over the ad design of type (?P<type>.+)")
def step_impl_hover_over_by_type(context, type: str):
    """
    :param type: type of wanted ad design
    :type context: behave.runner.Context
    """
    context.adsdesignpage.filer_ad_designs_by_type(type)
    context.adsdesignpage.hover_over_ad_design_by_type(type)


@step("All the previews display properly")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_all_previews_displayed()


@step("At least two ad designs are selected")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_multiple_ad_designs()


@when("I click on Unselect all link")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_on_unselect_all_link()


@then("The ad designs are unselected")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_designs_unselected()


@step("At least two ad designs are created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_page_is_not_empty()


@when("I click on Move to")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_on_move_to_link()


@then("The ad designs are moved to that folder")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_is_moved()