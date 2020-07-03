from mycroft import MycroftSkill, intent_file_handler


class ListagemMediaAtv(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('atv.media.listagem.intent')
    def handle_atv_media_listagem(self, message):
        self.speak_dialog('atv.media.listagem')


def create_skill():
    return ListagemMediaAtv()

