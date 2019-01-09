from selenium.webdriver.common.by import By
from framework.webapp import WebApp


class NavigationMenuLocators(object):
    DASHBOARD_TAB = (By.XPATH, "//ul[@id='headerMenu']//a[contains(@href, 'dashboard')]")
    CAMPAIGNS_TAB = (By.XPATH, "//ul[@id='headerMenu']//a[contains(@href, 'campaigns')]")
    AD_DESIGN_TAB = (By.XPATH, "//ul[@id='headerMenu']//a[contains(@href, 'addesign')]")
    AUDIENCE_TAB = (By.XPATH, "//ul[@id='headerMenu']//a[contains(@href, 'audience')]")
    UNPUBLISHED_ADS_TAB = (By.XPATH, "//ul[@id='headerMenu']//a[contains(@href, 'unpublishedads')]")
    OPTIMIZATION_RULES_TAB = (By.XPATH, "//ul[@id='headerMenu']//a[contains(@href, 'optimization')]")


class NavigationMenu(WebApp):

    def navigate_to_page(self, page_name):
        """
        Navigates to the page
        :param page_name: name of wanted page
        :type page_name: string
        """
        if page_name == "Dashboard":
            self.click_on_menu_tab(NavigationMenuLocators.DASHBOARD_TAB)
        elif page_name == "Campaigns":
            self.click_on_menu_tab(NavigationMenuLocators.CAMPAIGNS_TAB)
        elif page_name == "Ad Designs":
            self.click_on_menu_tab(NavigationMenuLocators.AD_DESIGN_TAB)
        elif page_name == "Audience":
            self.click_on_menu_tab(NavigationMenuLocators.AUDIENCE_TAB)
        elif page_name == "Unpublished Ads":
            self.click_on_menu_tab(NavigationMenuLocators.UNPUBLISHED_ADS_TAB)
        elif page_name == "Optimization Rules":
            self.click_on_menu_tab(NavigationMenuLocators.OPTIMIZATION_RULES_TAB)
        else:
            raise Exception("Page '{}' not found".format(page_name))

    def click_on_menu_tab(self, tab_name):
        element = self.wait_for_element(tab_name)
        element.click()
