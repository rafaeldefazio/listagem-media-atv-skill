from mycroft import intent_file_handler, MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context
import requests


class ListagemMediaAtv(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)

	@intent_file_handler('atv.media.listagem.intent')
	def handle_atv_media_listagem(self, message):

		ipAPI = 'http://177.21.53.138:3000'


		payload = {'user':'publico','password':'123'}
		getToken = requests.post(ipAPI + "/login", data=payload)


		myToken = getToken.content;
		headers = {'x-access-token': myToken}

		r = requests.get(ipAPI + '/media-atividades-30dias', headers=headers)

		if r.status_code != 200:
			self.speak('Ocorreu algum problema ao me conectar ao servidor de dados. Por favor, verifique as credenciais e tente novamente.')

		else:
			rn = r.json()[0]

			for ri in rn:

				self.speak_dialog('atv.media.listagem', data=ri)


def create_skill():
	return ListagemMediaAtv()

