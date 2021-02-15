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

		if keyMember != '' and keyBook:
			# insert borrow
			getDate = datetime.datetime.now()

			date = getDate.strftime('%Y-%m-%d')
			idDate = getDate.strftime('%m%d')

			dataInsert = {}
			key = keyBook+idDate
			dataInsert['id'] = keyBook
			dataInsert['title'] = dataBook['title']
			dataInsert['author'] = dataBook['author']
			dataInsert['date_out'] = date
			dataInsert['date_in'] = '-'
			dataInsert['status'] = 'false'

			dataMember['books'][key] = dataInsert
			dataUpdate = dataMember
			# insert borrow

			# update book
			dataBook['stock'] =  str(int(dataBook['stock'])-1)
			dataBook['used'] =  str(int(dataBook['used'])+1)

			self.__book.update(dataBook, keyBook)
			# update book

			self.__member.update(dataUpdate, keyMember)

			return 'true'
		else:
			return 'false'

	def re(self, keyMember, dataMember, keyBorrow):

		if keyMember != '' and keyBorrow != '':

			# update borrow
			getDate = datetime.datetime.now()
			date = getDate.strftime('%Y-%m-%d')

			dataMember['books'][keyBorrow]['status'] = 'true'
			dataMember['books'][keyBorrow]['date_in'] = date
			keyBook = dataMember['books'][keyBorrow]['id']

			idMember = str(dataMember['id'])
			nameMember = dataMember['name']
			bookMember = dataMember['books']


				
			dataUpdate = {}
			dataUpdate['id'] = str(idMember)
			dataUpdate['name'] = nameMember
			dataUpdate['books'] = bookMember

			# update borrow

			# update book
			getBook = self.__book.get()
			getBook[keyBook]['stock'] =  str(int(getBook[keyBook]['stock'])+1)
			getBook[keyBook]['used'] =  str(int(getBook[keyBook]['used'])-1)
			dataBook = getBook[keyBook]

			self.__book.update(dataBook, keyBook)
			# update book

			self.__member.update(dataUpdate, keyMember)

			return 'true'

		else:
			return 'false'


# className = Borrow()
# className.test()