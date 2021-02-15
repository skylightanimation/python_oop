import datetime
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


class Borrow(M_member, M_book):

	__helper = Helper()
	__member = M_member()
	__book 	= M_book()
	# __v_action = Action()


	def do(self, keyMember, dataMember, keyBook, dataBook):

		if keyMember != '':

			getDate = datetime.datetime.now()

			date = getDate.strftime('%Y-%m-%d')
			idDate = getDate.strftime('%m%d')

			dataInsert = {}
			key = keyBook+idDate
			dataInsert['id'] = idDate
			dataInsert['title'] = dataBook['title']
			dataInsert['author'] = dataBook['author']
			dataInsert['date_out'] = date
			dataInsert['date_in'] = '-'
			dataInsert['status'] = 'false'

			dataMember['books'][key] = dataInsert
			dataUpdate = dataMember

			self.__member.update(dataUpdate, keyMember)

			return 'true'
		else:
			return 'false'

	def re(self):
		key = input("Input 'ID' Member  : ")
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

	def test(self, data):
		pass

# className = Borrow()
# className.test()