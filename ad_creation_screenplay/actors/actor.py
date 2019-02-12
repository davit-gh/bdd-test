class Actor(object):


    def attempts_to(self, *args):
        for arg in args:
            arg.execute()
