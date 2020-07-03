from mycroft import intent_file_handler, MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context
import requests


class ListagemMediaAtv(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)

	@intent_file_handler('atv.media.listagem.intent')
	def handle_atv_media_listagem(self, message):

		r = requests.get('http://localhost:3000/media-atividades-30dias')
		rn = r.json()[0]

		for ri in rn:

			self.speak_dialog('atv.media.listagem', data=ri)


def create_skill():
	return ListagemMediaAtv()

