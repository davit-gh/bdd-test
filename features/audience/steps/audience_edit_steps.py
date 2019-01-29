from behave import *

use_step_matcher("re")


@given("Edit Audience modal is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.audiencemodal.edit_audience_modal_is_opened()