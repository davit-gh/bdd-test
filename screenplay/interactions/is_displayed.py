from screenplay.interactions.interaction import Interaction

class NotVisible(Interaction):

    def __init__(self, context):
        self._element = None
        super().__init__(context)

    def element(self, element):
        self._element = element
        return self

    def execute(self):
        return self._element.is_element_not_visible()