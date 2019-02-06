from behave import *

use_step_matcher("re")

@given("I am logged in")
def step_impl_validate_logged_in(context):
    context.execute_steps('''
            Given I am logged in
        ''')

@step("I choose Sandbox Adzwedo ad account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adcreationpage.select_ad_account()