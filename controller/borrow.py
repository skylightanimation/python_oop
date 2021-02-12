import sys
system_path = '../system'
sys.path.append(system_path)
import helper
from helper import *


model_path = '../model'
sys.path.append(model_path)
import m_book
from m_book import *

import m_member
from m_member import *


class Borrow(M_member, M_book):

	__helper = Helper()
	__member = M_member()
	__book 	= M_book()
	# __v_action = Action()


	def do(self):
		dataMembers = self.__member.get()
		if len(dataMembers) == 0:
			message = 'data buku kosong...'
			return message
		else:
			print(" ID	   | NAME		 |  BORROWED 	")
			totalAvailable = 0
			totalBorrowed = 0
			for key in dataMembers:
				keyMember = key
				idMember = int(dataMembers[key]['id'])
				nameMember = dataMembers[key]['name']
				booksMember = dataMembers[key]['books']
				print(keyMember+'   | '+nameMember+'	  | '+str(len(booksMember)))
			message = 'Jumlah Member : '+str(len(dataMembers))
			print(message)

		key = input("Input 'ID' Member  : ")
		dataBooks = self.__book.get()
		print(dataBooks)
		print(" ID	   | NAME		 | YEAR	| AUTHOR			")
		
		for key in dataBooks:
			keyBook = key

			idMember = str(dataBooks[key]['id'])
			nameBook = dataBooks[key]['title']
			yearBook = dataBooks[key]['year']
			authorBook = dataBooks[key]['author']
			stockBook = dataBooks[key]['stock']
			usedBook = dataBooks[key]['used']

			# keyBook = key
			# idBook = int(dataMembers['id'])
			# nameBook = dataMembers['title']
			# yearBook = dataMembers['year']
			# authorBook = data['author']
			total = int(stockBook) + int(usedBook)
			print(keyBook+'   | '+nameBook+'	| '+yearBook+'  | '+authorBook)


		idMemberUpdate = input("Input 'ID' buku : ")


		idMember = str(dataBooks[idMemberUpdate]['id'])
		nameBook = dataBooks[idMemberUpdate]['title']
		yearBook = dataBooks[idMemberUpdate]['year']
		authorBook = dataBooks[idMemberUpdate]['author']



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


className = Borrow()
className.do()