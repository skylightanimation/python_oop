import sys
system_path = '../system'
sys.path.append(system_path)
import igud
from igud import *

import helper
from helper import *


class M_member(IGUD, Helper):

	__table = 'members'
	__code 	= 'MEMBER_'

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
		print(self.__table)		
		data = getattr(self, '_'+self.__table)

		if key != None:	
			return data[key]
		else:
			return data
