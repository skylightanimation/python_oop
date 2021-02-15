import	os

class Menu():

	__featuresMain 	= ['Buku', 'Member', 'Pinjam']
	__featuresCrud 	= ['Daftar', 'Tambah', 'Update', 'Delete']
	__featuresOut 	= ['MAINMENU']
	__featuresQuit 	= ['Quit']
	__featuresBorrow= ['Meminjam', 'Mengembalikan']

	def __init__(self, title):
		if title == 'main':
			self.main()
		else:
			self.sub(title)

	def main(self):
		self.title()
		
		number = 0
		for i in self.__featuresMain:
			number += 1
			print(str(number)+'. '+str(i))
		for i in self.__featuresQuit:
			number = 0
			print(str(number)+'. '+str(i))


	def sub(self, name):
		self.title(name)
		
		number = 0
		for i in self.__featuresOut:
			number = 0
			print(str(number)+'. '+str(i))
		if name == 'Pinjam':
			for i in self.__featuresBorrow:
				number += 1
				print(str(number)+'. '+str(i))			
		else:
			for i in self.__featuresCrud:
				number += 1
				print(str(number)+'. '+str(i))

	def title(self, name=None):
		if name != None:
			title = ' SUB MENU : '+name
			print('---------------------')
			print(title)
			print('---------------------')
		else:
			title = ' MAIN MENU '
			print('---------------------')
			print(title)
			print('---------------------')

# menu = Menu('main')
# menu.__init__('trace')
# print(header)
