import sys
import os

view_path = 'view'
sys.path.append(view_path)
import v_menu
from v_menu import *

import v_action
from v_action import *


controller_path = 'controller'
sys.path.append(controller_path)
import book
from book import *

import member
from member import *

import borrow
from borrow import *


class App(Menu, Action):

    book = Book()
    member = Member()

    def __init__(self):
        self.__home()
        self.__switch('main')

    def __home(self):
        menu = Menu('main')

    def __switch(self, access):
        option = int(input('Pilih Menu :'))

        if access == 'main' :
            if option == 0:
                self.logout()

            elif option == 1:
                menu = Menu('Buku')
                self.__book()

            elif option == 2:
                menu = Menu('Member')
                self.__member()

            elif option == 3:
                menu = Menu('Pinjam')
                self.__switch('Pinjam')

            else:
                message = 'option not define!!!'
                menu = self.alert(message, 0)

        else:
            if option == 0:
                self.__home()
                self.__switch('main')

            elif option == 1:
                menu = Menu('Buku')
                self.__book()

            elif option == 2:
                menu = Menu('Member')
                self.__member()
                # self.__switch('Member')

            elif option == 3:
                menu = Menu('Pinjam')
                # self.__switch('Pinjam')

            else:
                message = 'option not define!!!'
                menu = self.alert(message, 0)

    def alert(self, message, option):
        print(message)
        print(option)
        redirect = input('"ENTER" utk kembali ke MAIN MENU, atau "y" utk stay.. ')
        if redirect == "y" or redirect == "Y":
            # self.clear_screen()
            menu = Menu(option)
            if option == 'Buku':
                menu = Menu('Buku')
                self.__book()

            elif option == 'Member':
                menu = Menu('Member')
                self.__member()

            elif option == 'Pinjam':
                menu = Menu('Pinjam')
                self.__switch('Pinjam')


        else:
            self.clear_screen()
            self.__init__()


    def __book(self):
        option = int(input('Pilih Menu :'))
        if option == 0:
            self.__home()
            self.__switch('main')
        if option == 1:
            message = self.book.get()
            menu = self.alert(message, 'Buku')
        elif option == 2:
            doAction = self.book.add()
            if doAction == 'true':
                message = 'insert success...'
                menu = self.alert(message, 'Buku')
            else:
                message = 'insert failed!!!'
                menu = self.alert(message, 'Buku')
        elif option == 3:
            doAction = self.book.update()
            if doAction == 'true':
                message = 'update success...'
                menu = self.alert(message, 'Buku')
            else:
                message = 'update failed!!!'
                menu = self.alert(message, 'Buku')
        elif option == 4:
            doAction = self.book.delete()
            if doAction == 'true':
                message = 'delete success...'
                menu = self.alert(message, 'Buku')
            else:
                message = 'delete failed!!!'
                menu = self.alert(message, 'Buku')
        else:
            message = 'access not found!!!'
            menu = self.alert(message, 0)


    def __member(self):
        option = int(input('Pilih Menu :'))
        if option == 0:
            self.__home()
            self.__switch('main')
        if option == 1:
            message = self.member.get()
            menu = self.alert(message, 'Member')
        elif option == 2:
            doAction = self.member.add()
            if doAction == 'true':
                message = 'insert success...'
                menu = self.alert(message, 'Member')
            else:
                message = 'insert failed!!!'
                menu = self.alert(message, 'Member')
        elif option == 3:
            doAction = self.member.update()
            if doAction == 'true':
                message = 'update success...'
                menu = self.alert(message, 'Member')
            else:
                message = 'update failed!!!'
                menu = self.alert(message, 'Member')
        elif option == 4:
            doAction = self.member.delete()
            if doAction == 'true':
                message = 'delete success...'
                menu = self.alert(message, 'Member')
            else:
                message = 'delete failed!!!'
                menu = self.alert(message, 'Member')
        else:
            message = 'access not found!!!'
            menu = self.alert(message, 0)

    def __borrow(self):
        option = int(input('Pilih Menu :'))
        if option == 0:
            self.__home()
            self.__switch('main')
        if option == 1:
            message = self.member.get()
            menu = self.alert(message, 'Member')
        elif option == 2:
            doAction = self.member.add()
            if doAction == 'true':
                message = 'insert success...'
                menu = self.alert(message, 'Member')
            else:
                message = 'insert failed!!!'
                menu = self.alert(message, 'Member')
        elif option == 3:
            doAction = self.member.update()
            if doAction == 'true':
                message = 'update success...'
                menu = self.alert(message, 'Member')
            else:
                message = 'update failed!!!'
                menu = self.alert(message, 'Member')
        elif option == 4:
            doAction = self.member.delete()
            if doAction == 'true':
                message = 'delete success...'
                menu = self.alert(message, 'Member')
            else:
                message = 'delete failed!!!'
                menu = self.alert(message, 'Member')
        else:
            message = 'access not found!!!'
            menu = self.alert(message, 0)

    def __borrow(self):
        option = int(input('Pilih Menu :'))
        if option == 0:
            self.__home()
            self.__switch('main')
        if option == 1:
            message = self.borrow.do()
            if doAction == 'true':
                message = 'insert success...'
                menu = self.alert(message, 'Pinjam')
            else:
                message = 'insert failed!!!'
                menu = self.alert(message, 'Pinjam')
        elif option == 2:
            doAction = self.borrow.re()
            if doAction == 'true':
                message = 'insert success...'
                menu = self.alert(message, 'Pinjam')
            else:
                message = 'insert failed!!!'
                menu = self.alert(message, 'Pinjam')
        else:
            message = 'access not found!!!'
            menu = self.alert(message, 0)


app = App()


# book = Book()
# book.get()