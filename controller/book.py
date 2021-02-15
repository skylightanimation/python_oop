import sys
system_path = 'system'
sys.path.append(system_path)
import helper
from helper import *

import sys
model_path = 'model'
sys.path.append(model_path)
import m_book
from m_book import *

class Book(M_book):

	__helper = Helper()
	__book = M_book()

	def add(self, data):
		nameBook = data['title']
		yearBook = data['year']
		nameAuthor = data['author']
		stockBook = data['stock']

		if nameBook != '' and yearBook != '' and nameAuthor != '' and stockBook != '':
			
			table = self.__book.get()
			getId = str(self.__helper.generate_id(table))

			data = {}
			data['id'] = getId
			data['title'] = nameBook
			data['year'] = yearBook
			data['author'] = nameAuthor
			data['stock'] = stockBook
			data['used'] = '0'

			self.__book.insert(data)
			return 'true'
		else:
			return 'false'	  


	def update(self, key, data):

		if key != '' and data != '':
			idBook = str(data['id'])
			nameBook = data['title']
			yearBook = data['year']
			authorBook = data['author']
			stockBook = data['stock']
			usedBook = data['used']

			print('Name : '+nameBook)
			print('Year : '+yearBook)
			print('Author : '+authorBook)

			nameBookUpdate = input("  +Update book name  : ")
			yearBookUpdate = input("  +Update book year : ")
			nameAuthorUpdate = input("  +Update author name : ")

			if nameBookUpdate != '' and yearBookUpdate != '' and nameAuthorUpdate != '':
				
				dataUpdate = {}
				dataUpdate['id'] = str(idBook)
				dataUpdate['title'] = nameBookUpdate
				dataUpdate['year'] = yearBookUpdate
				dataUpdate['author'] = nameAuthorUpdate
				dataUpdate['stock'] = stockBook
				dataUpdate['used'] = usedBook

				self.__book.update(dataUpdate, key)

				return 'true'
			else:
				return 'false'

		else:
			return 'false'


	def delete(self, key):
		data = self.__book.get()
		if key in data:
			self.__book.delete(key)
			return 'true'
		else:
			return 'false'


	def get(self, key = None):
		if key != None:
			data = self.__book.get(key)
			return data;

		else:
			data = self.__book.get()
			if len(data) == 0:
				message = 'book empty...'
				return message
			else:
				return data