from ad_creation_screenplay.elements.baseElement import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class Element(BaseElement):

    def __init__(self, locator, selector, context):
        super(Element, self).__init__(locator, selector, context)

    def hover_and_click_elements(self, count):
        """Hover each element from the list of elements and click on it

                :return: None
                """
        webelements = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_all_elements_located((self.locator, self.selector))
        )
        count = int(count)
        try:
            webelements = webelements[:count]
        except IndexError:
            raise Exception("Not enough available elements to click.")
        for webelement in webelements:
            webdriver.ActionChains(self.driver.instance).move_to_element(webelement).perform()
            time.sleep(0.5)
            webelement.click()