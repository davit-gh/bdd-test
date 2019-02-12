from ad_creation_screenplay.actors.ad_creator import Ad_Creator

class Stage(object):

    def __init__(self):
        self.current_actor = None

    def call_to_stage(self, actor):
        if actor == "Ad_Creator":
            self.current_actor = Ad_Creator
        else:
            pass
        return self.the_actor_in_the_spotlight()

    def the_actor_in_the_spotlight(self):
        return self.current_actor