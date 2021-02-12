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

	def add(self):
		nameBook = input("  +Input nama buku : ")
		yearBook = input("  +Input tahun buku : ")
		nameAuthor = input("  +Input nama author : ")
		stockBook = input("  +Input jumlah buku : ")

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


	def update(self):
		key = input("Input 'ID' buku  : ")
		data = self.__book.get()
		if key in data:
			idBook = str(data[key]['id'])
			nameBook = data[key]['title']
			yearBook = data[key]['year']
			authorBook = data[key]['author']
			stockBook = data[key]['stock']
			usedBook = data[key]['used']

			print('Name : '+nameBook)
			print('Year : '+yearBook)
			print('Author : '+authorBook)

			nameBookUpdate = input("  +Update nama buku : ")
			yearBookUpdate = input("  +Update tahun buku : ")
			nameAuthorUpdate = input("  +Update nama author : ")

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


	def delete(self):
		key = input("Input 'ID' buku  : ")
		data = self.__book.get()
		if key in data:
			self.__book.delete(key)
			return 'true'
		else:
			return 'false'


	def get(self, key = None):
		if key != None:
			# print(key)
			data = self.__book.get(key)
			# print(data)
			print(" ID	   | NAME		 | YEAR	| AUTHOR		  | AVAILABLE	| BORROWED 	")

			keyBook = key
			idBook = int(data['id'])
			nameBook = data['title']
			yearBook = data['year']
			authorBook = data['author']
			stockBook = data['stock']
			usedBook = data['used']
			total = int(stockBook) + int(usedBook)
			print(keyBook+'   | '+nameBook+'	| '+yearBook+'  | '+authorBook+'	| '+stockBook+'		| '+usedBook)
			message = 'Jumlah Buku : '+str(total)

		else:
			data = self.__book.get()
			if len(data) == 0:
				message = 'data buku kosong...'
				return message
			else:
				print(" ID	   | NAME		 | YEAR	| AUTHOR		  | AVAILABLE	| BORROWED 	")
				totalAvailable = 0
				totalBorrowed = 0
				for key in data:
					keyBook = key
					idBook = int(data[key]['id'])
					nameBook = data[key]['title']
					yearBook = data[key]['year']
					authorBook = data[key]['author']
					stockBook = data[key]['stock']
					usedBook = data[key]['used']
					totalAvailable += int(stockBook)
					totalBorrowed += int(usedBook)
					print(keyBook+'   | '+nameBook+'	| '+yearBook+'  | '+authorBook+'	| '+stockBook+'		| '+usedBook)
				message = 'Jumlah Buku : '+str(len(data))+' | Buku Tersedia : '+str(totalAvailable)+' | Buku Dipinjam : '+str(totalBorrowed)
				return message