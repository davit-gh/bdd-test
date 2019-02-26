from behave import *
from screenplay.tasks.open_web_page import OpenWebPage
from screenplay.tasks.search_for import SearchFor
from screenplay.tasks.click_on import ClickOn
from screenplay.questions.get_all import GetAll
from screenplay.questions.not_visible import NotDisplayed
from screenplay.stage import Stage

stage = Stage()

@given("{ad_creator} is on Optimization Rules page")
def step_impl(context, ad_creator):
    """
    :type ad_creator: str
    :type context: behave.runner.Context
    """
    OpenWebPage(context).with_name('LoginPage').navigate_to("Optimization Rules").perform_as(stage.call_to_stage(ad_creator))


@step("at least 1 optimization rule is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    rules_number = GetAll(context).rules().length().perform_as(stage.the_actor_in_the_spotlight())
    assert rules_number >= 1


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