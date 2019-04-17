from screenplay.actors.ad_creator import Ad_Creator, Live_User

class Stage(object):

    def __init__(self):
        self.current_actor = None

    def call_to_stage(self, actor):
        if actor == "Ad_Creator":
            self.current_actor = Ad_Creator
        elif actor == "Live_User":
            self.current_actor = Live_User
        return self.the_actor_in_the_spotlight()

    def the_actor_in_the_spotlight(self):
        return self.current_actor