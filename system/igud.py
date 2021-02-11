import sys
system_path = 'config'
sys.path.append(system_path)
import database
from database import *


class IGUD(Database):

	

	# def __init__(self, table, data = None, key = None):
	# 	# self.action = action
	# 	self.table = table
	# 	self.data = data

	# 	if action == 'gets':
	# 	elif action == 'get':
	# 	elif action == 'insert':
	# 	elif action == 'update':
	# 	elif action == 'delete':
	# 	else:
	# 		print('ERROR : action')

	def insert(self, data):
		pass


	def update(self, table, data, key):
		pass


	def delete(self, table, key):
		pass


	def get(self, key):
		pass


# igud = IGUD('books')
# igud.gets('books')