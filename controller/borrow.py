import sys
system_path = 'system'
sys.path.append(system_path)
import helper
from helper import *


model_path = 'model'
sys.path.append(model_path)
import m_book
from m_book import *

import m_member
from m_member import *


class Member(M_member):

	__helper = Helper()
	__member = M_member()
	__book 	= M_books()
	# __v_action = Action()


	def do(self):
		key = input("Input 'ID' Memer  : ")
		data = self.__member.get()
		if key in data:
			idMember = str(data[key]['id'])
			nameMember = data[key]['name']
			bookMember = data[key]['books']

			print('Name : '+nameMember)
			
			print(" ID	   | NAME		 | YEAR	| AUTHOR			")

			keyBook = key
			idBook = int(data['id'])
			nameBook = data['title']
			yearBook = data['year']
			authorBook = data['author']
			total = int(stockBook) + int(usedBook)
			print(keyBook+'   | '+nameBook+'	| '+yearBook+'  | '+authorBook)



			data = self.__book.get(key)

			nameMemberUpdate = input("  +Update nama member : ")

			if nameMemberUpdate != '':
				
				dataUpdate = {}
				dataUpdate['id'] = str(idMember)
				dataUpdate['name'] = idMember
				dataUpdate['books'] = bookMember

				# print(key)


				self.__member.update(dataUpdate, key)
				self.__member.update(dataUpdate, key)

				return 'true'
			else:
				return 'false'

		else:
			return 'false'


	def re(self):
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


