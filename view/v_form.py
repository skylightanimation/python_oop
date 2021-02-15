import	os

class Form():

	__output = {}

	def input_f(self, data):
		# print(data)

		for key in data:
			data[key] = input(data[key])
			self.__output[key] = data[key]



		return self.__output

		# print(data)

	def input_k(self, data):
		# print(data)

		if data != '':
			dataKey = input(data)
			return dataKey
		else:
			return 'false'

		


# form = Form()
# data = {
# 	'title' 	: '	+input name 	: ',
# 	'year' 		: '	+input year 	: ',
# 	'author' 	: '	+input author 	: '	
# }

# form.input_f(data)