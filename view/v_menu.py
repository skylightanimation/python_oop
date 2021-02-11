import	os

class Menu():

	__featuresMain 	= ['Buku', 'Member', 'Pinjam']
	__featuresSub 	= ['Daftar', 'Tambah', 'Update', 'Delete']
	__featuresOut 	= ['MAINMENU']
	__featuresQuit 	= ['Quit']

	def __init__(self, title):
		if title == 'main':
			self.main()
		else:
			self.sub(title)

	def main(self):
		title = ' MAIN MENU'
		print('---------------------')
		print(title)
		print('---------------------')
		

		number = 0
		for i in self.__featuresMain:
			number += 1
			print(str(number)+'. '+str(i))
		for i in self.__featuresQuit:
			number = 0
			print(str(number)+'. '+str(i))


	def sub(self, name):
		title = ' SUB MENU : '+name
		print('---------------------')
		print(title)
		print('---------------------')
		
		number = 0
		for i in self.__featuresOut:
			number = 0
			print(str(number)+'. '+str(i))
		for i in self.__featuresSub:
			number += 1
			print(str(number)+'. '+str(i))


# menu = Menu('main')
# menu.__init__('trace')
# print(header)
