class Table():

	__text_limit = 20
	__year_limit = 4
	__datetime_limit = 8
	__int_limit = 5
	__id_limit = 8


	def __init__(self, data):
		# print(data)
		head = self.thead(data)
		hr = self.tbreak(len(head))
		print(hr)
		print(head)
		print(hr)
		
		body = self.tbody(data)
		print(body)
		hr = self.tbreak(len(head))
		print(hr)


	def tbody(self, data):
		body = ''

		
		for key in data:

			index = 0
			for keySub in data[key]:
				attribute = keySub
				value = data[key][keySub]

				if attribute == 'name' or attribute == 'author' or attribute == 'title' :
					rowValue = self.row(value, 'text')

				elif attribute == 'year':
					rowValue = self.row(value, 'year')

				elif attribute == 'date_out' or attribute == 'date_in':
					rowValue = self.row(value, 'datetime')

				elif attribute == 'stock' or attribute == 'used':
					rowValue = self.row(value, 'int')

				elif attribute == 'id':
					rowValue = self.row(key, 'id')
					
				else:
					rowValue = ''

				index = index+1
				# print(index)
				# print(len(data[key]))
				if index == len(data[key]):
					body = body+str(rowValue)+'\n'
				else:
					body = body+str(rowValue)

		return body	

	def thead(self, data):
		head = ''

		for key in data:
			for keySub in data[key]:
				attribute = keySub
				title = attribute.upper()

				if attribute == 'name' or attribute == 'author' or attribute == 'title' :
					rowValue = self.row(title, 'text')

				elif attribute == 'year':
					rowValue = self.row(title, 'year')

				elif attribute == 'date_out' or attribute == 'date_in':
					rowValue = self.row(title, 'datetime')

				elif attribute == 'stock' or attribute == 'used':
					rowValue = self.row(title, 'int')

				elif attribute == 'id':
					rowValue = self.row(title, 'id')

				else:
					continue

				head = head+str(rowValue)

			break
		return head

	def row(self, textValue, typeValue):
		textLenght = len(textValue)
		emptyLenght = 0
		typeLenght = 0
		row = ''


		if typeValue == 'text':
			typeLenght = self.__text_limit

		elif typeValue == 'year':
			typeLenght = self.__year_limit			

		elif typeValue == 'datetime':
			typeLenght = self.__datetime_limit

		elif typeValue == 'int':
			typeLenght = self.__int_limit

		elif typeValue == 'id':
			typeLenght = self.__id_limit



		emptyLenght = typeLenght-textLenght

		for i in range(0, emptyLenght):
			row = str(row)+' '


		if typeValue == 'int':
			row = " "+row+str(textValue)+" |"
		else:
			row = " "+str(textValue)+row+" |"
		
		return row

	def tbreak(self, length):
		space = ''
		for i in range(0, length):
			space = str(space)+'-'

		return space


books = {
    'BUK_1': {
        'id':'1',
        'title'  :'Merah Putih',
        'year'  :'1983',
        'author':'Hersevien M. Taulu',
        'stock' :'10',
        'used'  :'0'
    }, 
    'BUK_2': {
        'id':'2',
        'title'  :'Sang Pemimpi',
        'year'  :'2006',
        'author':'Andrea Hirata',
        'stock' :'10',
        'used'  :'0'
    },
    'BUK_3': {
        'id':'3',
        'title'  :'A Gate of Night',
        'year'  :'2014',
        'author':'Bella Forrest',
        'stock' :'10',
        'used'  :'0'
    }
}

# tb = Table(books)
# tb.__init__(books)

# test_str = "GeeksforGeeks"

# print(len(test_str))

# counter = test_str.count('e')
# print(counter)