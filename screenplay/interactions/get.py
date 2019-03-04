from screenplay.interactions.interaction import Interaction
from screenplay.pages.unpublishedAds import UnpublishedAdsPage

class Get(Interaction):

    def __init__(self, context):
        self._elements = None
        self._element = None
        self._text = False
        self._texts = False
        self._length = False
        self._selected = None
        self._attr_name = None
        self.title_elements = None
        super().__init__(context)

    def from_element(self, name):
        self._element = name
        return self

    def elements(self, elements):
        self._elements = elements
        return self

    def attribute(self, attr_name):
        self._attr_name = attr_name
        return self

    def is_selected(self, element):
        self._selected = element
        return self

    def text(self):
        self._text = True
        return self

    def texts(self):
        self._texts = True
        return self

    def length_of(self):
        self._length = True
        return self

    def _split_by_newline(self, str):
        # example: 'campaign_name\n15/02/2019 16:38'
        part1, part2 = str.split('\n')
        return part1

    def campaign_titles(self, titles):
        self.title_elements = titles.get_elements()
        return self

    def execute(self):
        response = ''
        if self.title_elements:
            response = [self._split_by_newline(element.text) for element in self.title_elements]
        elif self._text:
            response = self._element.text
        elif self._texts:
            response = [_element.text for _element in self._elements.get_elements()]
        elif self._length:
            response = len(self._elements.get_elements())
        elif self._selected:
            response = self._selected.is_selected()
        elif self._attr_name:
            response = self._element.get_attribute(self._attr_name)
        return response