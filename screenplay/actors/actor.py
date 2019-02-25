class Actor(object):


    def attempts_to(self, *args):
        last_response = ''
        for arg in args:
            last_response = arg.execute()
        return last_response
