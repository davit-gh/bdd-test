from ad_creation_screenplay.interactions.interaction import Interaction

class WaitForOverlayToDisappear(Interaction):

    def __init__(self, context):
        super().__init__(context)

    def element(self, element):
        self.element = element
        return self

    def execute(self):
        self.element.is_element_not_visible()
