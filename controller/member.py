import sys
system_path = 'system'
sys.path.append(system_path)
import helper
from helper import *

model_path = 'model'
sys.path.append(model_path)
import m_member
from m_member import *

class Member(M_member):

	__helper = Helper()
	__member = M_member()


	def add(self, data):		
		nameMember = data['name']

		if nameMember != '':			
			table = self.__member.get()
			getId = str(self.__helper.generate_id(table))

			data = {}
			books = {}
			data['id'] = getId
			data['name'] = nameMember
			data['books'] = books

			self.__member.insert(data)
			return 'true'
		else:
			return 'false'	  


	def update(self, key, data):

		if key != '' and data != '':
			idMember = str(data['id'])
			nameMember = data['name']
			bookMember = data['books']

			print('Name : '+nameMember)

			nameMemberUpdate = input("  +Update name member : ")

			if nameMemberUpdate != '':
				
				dataUpdate = {}
				dataUpdate['id'] = str(idMember)
				dataUpdate['name'] = nameMemberUpdate
				dataUpdate['books'] = bookMember

				self.__member.update(dataUpdate, key)

				return 'true'
			else:
				return 'false'

		else:
			return 'false'


	def delete(self, key):
		data = self.__member.get()
		if key in data:
			self.__member.delete(key)

			return 'true'
		else:
			return 'false'


	def get(self, key = None):
		if key != None:
			data = self.__member.get(key)
			return data;

		else:
			data = self.__member.get()
			if len(data) == 0:
				message = 'member empty...'
				return message
			else:
				return data