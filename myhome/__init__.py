import requests
import re
import json

inside_match = re.compile(r'inside: [0-9\.]+')
outside_match = re.compile(r'outside: [0-9\.]+')
target_match = re.compile(r'target: [0-9\.]+')
heatingControl_match = re.compile(r'heatingControl: ".+[A-Z]+"')

class IncorrectUsernameOrPassword(Exception):
	pass

class MyHome(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.session = requests.session()
		
		login_success = self.session.post('https://myhome.britishgas.co.uk/myhome/login/', data={'username': self.username, 'password': self.password}).text
		if 'The email address or password is incorrect, please try again' in login_success:
			raise IncorrectUsernameOrPassword()

	def get(self):
		html = self.session.get('https://myhome.britishgas.co.uk/myhome2/climate/').text.replace('\n', ' ')
		# print inside_match.search(html).group()
		inside_temperature = float(inside_match.search(html).group().split(' ')[-1])
		outside_temperature = float(outside_match.search(html).group().split(' ')[-1])
		try:
			target_temperature = float(target_match.search(html).group().split(' ')[-1])
		except:
			target_temperature = 0.0
		heatingControl = heatingControl_match.search(html).group().split('"')[1]
		return {"inside_temperature": inside_temperature, "outside_temperature": outside_temperature, "target_temperature": target_temperature, "heatingControl": heatingControl}

	def set_manual(self):
		self.session.put('https://myhome.britishgas.co.uk/myhome2/climate', data=json.dumps({'heatingControl': "MANUAL"}))

	def set_schedule(self):
		self.session.put('https://myhome.britishgas.co.uk/myhome2/climate', data=json.dumps({'heatingControl': "SCHEDULE"}))

	def set_off(self):
		self.session.put('https://myhome.britishgas.co.uk/myhome2/climate', data=json.dumps({'heatingControl': "OFF"}))

	def set_target(self, target):
		self.session.put('https://myhome.britishgas.co.uk/myhome2/climate', data=json.dumps({'target': target}))



if __name__ == '__main__':
	myhome = MyHome(USERNAME, PASSWORD)
	print myhome.get()