from screenplay.pages.basePage import BasePage
from screenplay.elements.element import Element
from selenium.webdriver.common.by import By


class OptimizationRulesPage(BasePage):

    def __init__(self, context):
        self.overlay = Element(By.CLASS_NAME, "optimization-rules-loading-overlay", context)
        self.datatable_overlay1 = Element(By.XPATH, "(//div[@class='js-datatable-loading-overlay'])[1]", context)
        self.datatable_overlay2 = Element(By.XPATH, "(//div[@class='js-datatable-loading-overlay'])[2]", context)
        self.existing_rules = Element(By.XPATH, "//div[@id='rule_container']/div", context)
        self.existing_rule_names = Element(By.CLASS_NAME, "rule-name", context)
        self.rule_search_field = Element(By.XPATH, "//input[@name='search_rule']", context)
        self.search_icon = Element(By.XPATH, "//input[@placeholder='{}']/following-sibling::span", context)
        self.icons = Element(By.XPATH, "(//div[@class='action-buttons-item {}']){}", context)
        self.ddown_opt = Element(By.XPATH, "(//div[contains(@class,' dropdown')])[{}]//li[./span[text()=' {}']]", context)
        self.cancel_edit_btn = Element(By.XPATH, "//div[@id='optimRulesList']//button[text()='Cancel']", context)
        self.cancel_assign_btn = Element(By.ID, "ruleCampaignsCancel", context)
        self.delete_rule_btn = Element(By.ID, "delete-rule-btn", context)
        self.apply_button = Element(By.ID, "assignRuleCampaigns", context)
        self.rule_creation_modal = Element(By.XPATH, "(//div[contains(@class,'js-rule-creation-block')])[{}]", context)
        self.assign_rule_chbx = Element(By.XPATH, "//div[@id='dashboardTable']//div[@class='check-box']", context)
        self.assign_rule_chbx_input = Element(By.XPATH, "//div[@id='dashboardTable']//input", context)
        self.assign_rule_modal = Element(By.ID, "optimRulesCampaignsList", context)
        self.campaign_search_field = Element(By.XPATH, "//input[@placeholder='Search by name...']", context)
        self.loading = Element(By.CLASS_NAME, "ftLoading", context)
        self.success_message = Element(By.ID, "successMessage", context)
        self.action_ddown = Element(By.XPATH, "//div[contains(@class,'rule_action ')]/div/button", context)
        self._option = Element(By.XPATH, "//a[./span[text()='{}']]", context)
        self.cpc_cpm_ddown = Element(By.XPATH, "(//div[contains(@class,'rule_cpc_cpm_select')])[1]/div[2]/button", context)
        self.period_ddown = Element(By.XPATH, "(//div[contains(@class, 'period-select')])[1]/div/button", context)
        self.adset_radio_btn = Element(By.XPATH, "//div[contains(@class,'rule_ad_adset_camp_select')]/div[3]/label", context)
        self.adset_radio_input = Element(By.XPATH, "//div[contains(@class,'rule_ad_adset_camp_select')]/div[3]/input", context)
        self.edit_save_btn = Element(By.XPATH, "//div[@id='optimRulesList']//button[text()='Save']", context)
        self.create_save_btn = Element(By.XPATH, "//div[@id='modal-for-create-rule']//button[text()='Save']", context)
        self.create_rule_btn = Element(By.CLASS_NAME, "create_new_rule", context)
        self.rule_name_field = Element(By.NAME, "rule_name", context)
        self.rule_price_field = Element(By.NAME, "rule_price", context)
        super().__init__(context)

