import sys
system_path = 'system'
sys.path.append(system_path)
import igud
from igud import *

import helper
from helper import *


class M_book(IGUD, Helper):

	__table = 'books'
	__code 	= 'BUK_'

	def insert(self, data):
		key_id = data['id']
		key = self.generate_key(self.__code, key_id)
		dataTemp = getattr(self, '_'+self.__table)
		dataTemp[key] = data
		setattr(self, '_'+self.__table, dataTemp)


	def update(self, data, key):
		dataTemp = getattr(self, '_'+self.__table)
		dataTemp[key] = data
		setattr(self, '_'+self.__table, dataTemp)


	def delete(self, key):
		dataTemp = getattr(self, '_'+self.__table)
		dataTemp.pop(key)
		setattr(self, '_'+self.__table, dataTemp)


	def get(self, key=None):
		# print(self.__table)		
		data = getattr(self, '_'+self.__table)

		if key != None:	
			return data[key]
		else:
			return data



# m_book = M_book('books')
# m_book.get()
# m_book.get('BUK_1')

# value =  {
#             'id':'5',
#             'title'  :'A Gate of Night',
#             'year'  :'2014',
#             'author':'Bella Forrest',
#             'stock' :'10',
#             'used'  :'0'
#         }

# m_book.insert(value)
# print('RESULT : ')
# m_book.get()

# value2 =  {
#             'id':'3',
#             'title'  :'Heaven Gate',
#             'year'  :'2014',
#             'author':'Bella Forrest',
#             'stock' :'10',
#             'used'  :'0'
#         }

# m_book.update(value2, 'BUK_3')
# print('RESULT U : ')
# m_book.get()


# m_book.delete('BUK_2')
# print('RESULT D : ')
# m_book.get()