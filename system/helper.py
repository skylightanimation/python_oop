class Helper():

	def generate_key(self, code, key_id):
		key = code+key_id
		return key

	def generate_id(self, table):
		idTemp = 0
		for key in table:
			idAvb = int(table[key]['id'])
			if idAvb == 0:
				idTemp = idAvb
			elif idTemp < idAvb:
				idTemp = idAvb
			else:
				print('error')

		idNew = idAvb + 1
		return idNew