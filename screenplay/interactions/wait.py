from screenplay.interactions.interaction import Interaction

class WaitForOverlayToDisappear(Interaction):

    def __init__(self, context):
        super().__init__(context)
        self._element = None
        self._elements = None

    def element(self, element):
        self._element = element
        return self

    def elements(self, elements):
        self._elements = elements
        return self

    def execute(self):
        invisible = True
        if self._element:
            invisible = self._element.is_element_not_visible()
        elif self._elements:
            invisible = self._elements.are_elements_not_visible()
        if not invisible:
            raise Exception("Didn't disappear")


class WaitForVisible(Interaction):

    def __init__(self, context):
        super().__init__(context)
        self._element = None

    def element(self, name, locators_group):
        locators = getattr(self.context, locators_group)
        self._element = locators.get_element(name)
        return self

    def timeout(self, duration):
        self.duration = duration
        return self

    def execute(self):
        return self._element.is_element_visible(timeout=self.duration)