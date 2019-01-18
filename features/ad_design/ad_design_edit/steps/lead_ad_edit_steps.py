from behave import *
from features.ad_design.ad_design_actions.steps.ad_design_actions_steps import *
from features.ad_design.ad_design_create.steps.addesign_steps import *

use_step_matcher("re")

def name2id(name):
    no_space = name.replace(' ', '')
    _id = no_space[:1].lower() + no_space[1:] + 'Type'
    return _id

@step("At least one ad design of type (?P<ad_type>.+) is created")
def step_impl(context, ad_type: str):
    """
    :param ad_type: type of wanted ad design
    :type context: behave.runner.Context
    """
    context.adsdesignpage.filer_ad_designs_by_type(ad_type)
    context.adsdesignpage.verify_that_ad_with_specific_type_exists(ad_type)
    context.ad_type = name2id(ad_type)


@then("The (?P<field_type>.+) should change to the new value")
def step_impl(context, field_type):
    """
    :type field_type: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.edit_first_ad_design()
    context.popup_window.verify_edit_window_text_input_is_correct(field_type, context.ad_type)


@then("The thumbnail image should change to the new image")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.compare_img_urls()


@step("I upload a new Single Image")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ad_type = context.ad_type if hasattr(context, 'ad_type') else None
    context.popup_window.upload_file("image_edit", ad_type)


@step("I click on Select Published Page posts radio-button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.popup_window.click_on_published_radio(context.ad_type)