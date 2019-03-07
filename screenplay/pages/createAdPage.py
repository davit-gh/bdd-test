from screenplay.pages.basePage import BasePage
from screenplay.elements.element import Element
from selenium.webdriver.common.by import By


class AdCreationPage(BasePage):

    def __init__(self, context):
        self.create_ad_btn = Element(By.XPATH, "//button[text()='Create Ad']", context)
        self.loading_overlay = Element(By.CLASS_NAME, "js-get-data-loading-overlay", context)
        self.profile_overlay = Element(By.CLASS_NAME, "loading-user-profile", context)
        self.ad_account_ddown = Element(By.XPATH, "(//div[@id='adcreationSteps']//button)[1]", context)
        self.ad_account_ddown_option = Element(By.XPATH, "//div[@id='adcreationSteps']//a/span[text()='{}']", context)
        self.page_ddown = Element(By.XPATH, "//button[@data-id='wizardPageSelect']", context)
        self.page_ddown_option = Element(
            By.XPATH, "//button[@data-id='wizardPageSelect']/following-sibling::div/ul/li[.//p[text()='{}']]", context
        )
        self.campaign_title_field = Element(By.XPATH, "//input[@name='campaign_name']", context)
        self.campaign_type = Element(By.XPATH, "//label[@for='{}']", context)
        self.next_btn = Element(By.XPATH, "//footer/div/button[text()='Next']", context)
        self.audiences = Element(By.XPATH, "//div[@id='adFlexContent2']//tbody/tr", context)
        self.audience_select_btn = Element(
            By.XPATH, "//div[@id='adFlexContent2']//tbody/tr[@data-id='{}']//button[text()='Select']", context
        )
        self.audience_select_btns = Element(By.XPATH, "//div[@id='adFlexContent2']//button[text()='Select']", context)
        self.ad_designs = Element(By.XPATH, "//div[@data-pageid]", context)
        self.ad_design_select_btns = Element(By.XPATH, "//div[@class='ads-block']//button[text()='Select']", context)
        self.ad_design_select_btn = Element(By.XPATH, "//div[@data-pageid and @data-id='{}']//button[text()='Select']", context)
        self.ad_type_ddown = Element(By.XPATH, "//a[@class='chosen-single']/span[text()='Ad types']", context)
        self.ad_type_ddown_option = Element(By.XPATH, "//ul[@class='chosen-results']/li[text()='{}']", context)
        self.publish_later_link = Element(By.CLASS_NAME, "publish-later-action", context)
        self.validation_error_field = Element(By.XPATH, "//label[@class='error_message']/p", context)
        self.adset_per_ad = Element(By.XPATH, "//label[@for='adset_per_ad'][1]", context)
        self.adsets_ready_to_publish = Element(By.CLASS_NAME, "campaign-row--content", context)
        super().__init__(context)