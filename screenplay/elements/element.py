from screenplay.elements.baseElement import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, random

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

    def check_checkboxes(self, count):
        count = int(count)
        labels = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_all_elements_located((self.locator, self.selector))
        )
        checkboxes = [label.find_element_by_xpath("./preceding-sibling::input") for label in labels]
        checked = [label for label, checkbox in zip(labels, checkboxes) if checkbox.is_selected()]
        if count > len(checked) or count < 1:
            raise Exception("Wrong count number. Should be between 1 and 5.")
        diff = len(checked) - count
        [label.click() for label in checked[-diff:]] if diff else None


    def click_one_of_elements(self):
        """Randomly click one of the available elements
              :return: int
        """
        webelements = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_all_elements_located((self.locator, self.selector))
        )
        random_index = random.randrange(len(webelements))
        webelements[random_index].click()
        # xpath index is 1-based
        random_index += 1
        return random_index

    def is_selected(self):
        return self.element.is_selected()