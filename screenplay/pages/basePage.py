class BasePage(object):

    def __init__(self, context):
        self.context = context
        self.URL = ""

    def get_element(self, name, *args):
        element = ''
        if hasattr(self, name):
            element = getattr(self, name)
            element.set_parameters(*args)
        return element