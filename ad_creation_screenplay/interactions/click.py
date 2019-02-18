from ad_creation_screenplay.interactions.interaction import Interaction

class Click(Interaction):

    def __init__(self, context):
        super().__init__(context)

    def element(self, element):
        self.element = element
        return self

    def execute(self):
        self.element.click()


class HoverAndClick(Interaction):

    def __init__(self, context):
        super().__init__(context)

    def elements(self, elements, count):
        self.elements = elements
        self.count = count
        return self

    def execute(self):
        self.elements.hover_and_click_elements(self.count)
