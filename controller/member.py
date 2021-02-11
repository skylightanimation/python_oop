import sys
system_path = 'system'
sys.path.append(system_path)
import helper
from helper import *

import sys
model_path = 'model'
sys.path.append(model_path)
import m_member
from m_member import *

# view_path = 'view'
# sys.path.append(view_path)
# import v_action
# from v_action import *

class Member(M_member):

	__helper = Helper()
	__member = M_member()
	# __v_action = Action()

	def add(self):
		nameMember = input("  +Input nama member: ")

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


	def update(self):
		key = input("Input 'ID' Memer  : ")
		data = self.__member.get()
		if key in data:
			idMember = str(data[key]['id'])
			nameMember = data[key]['name']
			bookMember = data[key]['books']

			print('Name : '+nameMember)

			nameMemberUpdate = input("  +Update nama member : ")

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


	def delete(self):
		key = input("Input 'ID' Member  : ")
		data = self.__member.get()
		if key in data:
			self.__member.delete(key)
			return 'true'
		else:
			return 'false'


	def get(self, key = None):
		if key != None:
			# print(key)
			data = self.__member.get(key)
			# print(data)
			print(" ID	   | NAME		 | JUMLAH PINJAM		")

			keyMember = key
			idMember = int(data['id'])
			nameMember = data['name']
			booksMember = data['books']
			print(keyMember+'   | '+nameMember+'	| '+str(len(booksMember)))
			message = 'Jumlah buku yang sedang di pinjam : '+str(len(booksMember))

		else:
			data = self.__member.get()
			if len(data) == 0:
				message = 'data buku kosong...'
				return message
			else:
				print(" ID	   | NAME		 |  BORROWED 	")
				totalAvailable = 0
				totalBorrowed = 0
				for key in data:
					keyMember = key
					idMember = int(data[key]['id'])
					nameMember = data[key]['name']
					booksMember = data[key]['books']
					print(keyMember+'   | '+nameMember+'	  | '+str(len(booksMember)))
				message = 'Jumlah Member : '+str(len(data))
				return message