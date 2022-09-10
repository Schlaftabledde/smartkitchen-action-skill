from mycroft import MycroftSkill, intent_file_handler


class SmartkitchenAction(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('action.smartkitchen.intent')
    def handle_action_smartkitchen(self, message):
        self.speak_dialog('action.smartkitchen')


def create_skill():
    return SmartkitchenAction()

