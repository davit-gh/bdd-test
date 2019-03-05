from behave import *
from screenplay.tasks.open_web_page import OpenWebPage
from screenplay.tasks.search_for import SearchFor
from screenplay.tasks.click_on import ClickOn
from screenplay.tasks.select_from_dropdown import Select
from screenplay.tasks.create import Create
from screenplay.questions.get_all import GetAll
from screenplay.questions.not_visible import NotDisplayed
from screenplay.questions.is_checked import IsChecked
from screenplay.questions.get_attribute import GetAttribute
from screenplay.stage import Stage

stage = Stage()

@given("{ad_creator} is on Optimization Rules page")
def step_impl(context, ad_creator):
    """
    :type ad_creator: str
    :type context: behave.runner.Context
    """
    # Assign the number of existing rules to the context variable to be used in later steps
    OpenWebPage(context).with_name('LoginPage').navigate_to("Optimization Rules").perform_as(stage.call_to_stage(ad_creator))
    context.rules_number = GetAll(context).rules().length().perform_as(stage.the_actor_in_the_spotlight())


@step("at least 1 optimization rule is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.rules_number >= 1


@step("she searches for an existing rule titled {rule_name}")
def step_impl(context, rule_name):
    """
    :type rule_name: str
    :type context: behave.runner.Context
    """
    SearchFor(context).rule_by_name(rule_name).perform_as(stage.the_actor_in_the_spotlight())


@then("the rules that are named {rule_name} are filtered")
def step_impl(context, rule_name):
    """
    :type rule_name: str
    :type context: behave.runner.Context
    """
    rule_names = GetAll(context).rule_names().perform_as(stage.the_actor_in_the_spotlight())
    rule_names = set(rule_names)
    assert rule_name == rule_names.pop()
    assert len(rule_names) == 0


@step("she clicks on {icon_name} icon on any rule")
def step_impl(context, icon_name):
    """
    :type icon_name: str
    :type context: behave.runner.Context
    """
    random_index = ClickOn(context).randomly_chosen_icon(icon_name).perform_as(stage.the_actor_in_the_spotlight())
    context.random_index = random_index

@step("clicks on {button_name} button")
def step_impl(context, button_name):
    """
    :type button_name: str
    :type context: behave.runner.Context
    """
    ClickOn(context).button(button_name).perform_as(stage.the_actor_in_the_spotlight())


@then("the modal is closed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert NotDisplayed(context).modal(context.random_index).perform_as(stage.the_actor_in_the_spotlight())


@step("she searches for {campaign_name} campaign")
def step_impl(context, campaign_name):
    """
    :type campaign_name: str
    :type context: behave.runner.Context
    """
    SearchFor(context).campaign(campaign_name).perform_as(stage.the_actor_in_the_spotlight())


@step("chooses a campaign and clicks on Apply")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ClickOn(context).campaign().button("apply_button").perform_as(stage.the_actor_in_the_spotlight())
    NotDisplayed(context).rule_modal().perform_as(stage.the_actor_in_the_spotlight())


@then("the rule is assigned to {campaign_name} campaign")
def step_impl(context, campaign_name):
    """
    :type campaign_name: str
    :type context: behave.runner.Context
    """
    ClickOn(context).icon("js-assign-rule", context.random_index).perform_as(stage.the_actor_in_the_spotlight())
    SearchFor(context).campaign(campaign_name).perform_as(stage.the_actor_in_the_spotlight())
    assert IsChecked(context).first_checkbox().perform_as(stage.the_actor_in_the_spotlight())
    ClickOn(context).campaign().button("apply_button").perform_as(stage.the_actor_in_the_spotlight())


@step("she clicks on {icon_name} icon under that dropdown")
def step_impl(context, icon_name):
    """
    :type icon_name: str
    :type context: behave.runner.Context
    """
    ClickOn(context).button(icon_name).perform_as(stage.the_actor_in_the_spotlight())


@then("the rule is duplicated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    rule_names = GetAll(context).rule_names().perform_as(stage.the_actor_in_the_spotlight())
    rules_number = GetAll(context).rules().length().perform_as(stage.the_actor_in_the_spotlight())
    assert context.rules_number == rules_number - 1
    assert "copy of " + rule_names[context.random_index] in rule_names


@then("the rule is deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    rules_number = GetAll(context).rules().length().perform_as(stage.the_actor_in_the_spotlight())
    assert context.rules_number == rules_number + 1


@step("makes changes on the modal and clicks on {save_btn} button")
def step_impl_make_changes(context, save_btn):
    """
    :type save_btn: str
    :type context: behave.runner.Context
    """
    values = ["Start", "CTR", "Last 3 days"]
    ClickOn(context).button("adset_radio_btn").perform_as(stage.the_actor_in_the_spotlight())
    Select(context).from_dropdown('action').option(values[0]).perform_as(stage.the_actor_in_the_spotlight())
    Select(context).from_dropdown('cpc_cpm').option(values[1]).perform_as(stage.the_actor_in_the_spotlight())
    Select(context).from_dropdown('period').option(values[2]).perform_as(stage.the_actor_in_the_spotlight())
    ClickOn(context).button(save_btn).perform_as(stage.the_actor_in_the_spotlight())
    context.values_to_be_checked = values

@then("the changes are saved")
def step_impl_changes_are_saved(context):
    """
    :type context: behave.runner.Context
    """
    ClickOn(context).icon("rule_arrow js-edit-optim-rule", 1).perform_as(stage.the_actor_in_the_spotlight())
    attr1 = GetAttribute(context).element("action_ddown").attribute("title").perform_as(stage.the_actor_in_the_spotlight())
    attr2 = GetAttribute(context).element("cpc_cpm_ddown").attribute("title").perform_as(stage.the_actor_in_the_spotlight())
    attr3 = GetAttribute(context).element("period_ddown").attribute("title").perform_as(stage.the_actor_in_the_spotlight())
    assert IsChecked(context).radio_btn("adset_radio_input").perform_as(stage.the_actor_in_the_spotlight())
    assert context.values_to_be_checked == [attr1, attr2, attr3]


@step("gives the rule name, adds conditions, chooses a schedule")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    Create(context).rule().by_random_name().perform_as(stage.the_actor_in_the_spotlight())
    step_impl_make_changes(context, "create_save_btn")


@then("the rule is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    rules_number = GetAll(context).rules().length().perform_as(stage.the_actor_in_the_spotlight())
    assert context.rules_number == rules_number - 1
    step_impl_changes_are_saved(context)