import sys
import os

view_path = 'view'
sys.path.append(view_path)
import v_menu
from v_menu import *

import v_action
from v_action import *

import v_form
from v_form import *

import v_table
from v_table import *


controller_path = 'controller'
sys.path.append(controller_path)
import book
from book import *

import member
from member import *

import borrow
from borrow import *


class App(Menu, Action, Form, Table):

    book = Book()
    member = Member()
    borrow = Borrow()

    def __init__(self):
        self.__home()
        self.__switch('main')

    def __home(self):
        menu = Menu('main')


    def __switch(self, access):
        option = int(input('Choose Menu :'))

        if access == 'main' :
            if option == 0:
                self.logout()

            elif option == 1:
                self.clear_screen()
                menu = Menu('Buku')
                self.__book()

            elif option == 2:
                self.clear_screen()
                menu = Menu('Member')
                self.__member()

            elif option == 3:
                self.clear_screen()
                menu = Menu('Pinjam')
                self.__borrow()

            else:
                message = 'option not define!!!'
                menu = self.alert(message, 0)

        else:
            if option == 0:
                self.clear_screen()
                self.__home()
                self.__switch('main')

            elif option == 1:
                self.clear_screen()
                menu = Menu('Buku')
                self.__book()

            elif option == 2:
                self.clear_screen()
                menu = Menu('Member')
                self.__member()

            elif option == 3:
                self.clear_screen()
                menu = Menu('Pinjam')
                self.__borrow()

            else:
                message = 'option not define!!!'
                menu = self.alert(message, 0)


    def alert(self, message, option):
        print(message)
        # print(option)
        redirect = input('press "ENTER" for MAIN MENU, atau "y" for stay.. ')
        if redirect == "y" or redirect == "Y":
            # self.clear_screen()
            menu = Menu(option)
            if option == 'Buku':
                self.clear_screen()
                menu = Menu('Buku')
                self.__book()

            elif option == 'Member':
                self.clear_screen()
                menu = Menu('Member')
                self.__member()

            elif option == 'Pinjam':
                self.clear_screen()
                menu = Menu('Pinjam')
                self.__borrow()


        else:
            self.clear_screen()
            self.__init__()


    def __book(self):
        option = int(input('Choose Menu :'))
        if option == 0:
            self.clear_screen()
            self.__home()
            self.__switch('main')
        if option == 1:
            self.clear_screen()
            self.title("BOOK")
            message = ''
            data = self.book.get()
            if isinstance(data, dict):
                Table(data)
                available = 0
                borrowed = 0

                for key in data:
                    available = available+int(data[key]['stock'])
                    borrowed = borrowed+int(data[key]['used'])
                message = ' Books Variant : <'+str(len(data))+'> | Available : <'+str(available)+'> | Borrowed : <'+str(borrowed)+'>  '
            else:
                message = data
            menu = self.alert(message, 'Buku')
        elif option == 2:
            self.clear_screen()
            self.title("BOOK <Add>")
           

            dataInput = {
                'title' : '  +Input "Book Title" : ',
                'year' : '  +Input "Book Year" : ',
                'author' : '  +Input "Book Author" : ',
                'stock' : '  +Input "Book Stock" : '
            }
            inputBook = self.input_f(dataInput)
            doAction = self.book.add(inputBook)

            if doAction == 'true':
                message = 'insert success...'
                menu = self.alert(message, 'Buku')
            else:
                message = 'insert failed!!!'
                menu = self.alert(message, 'Buku')
        elif option == 3:
            self.clear_screen()
            self.title("BOOK <Edit>")
            data = self.book.get()
            if isinstance(data, dict):
                Table(data)
                idBook = self.input_k('Input "ID" buku  : ')
                # print()
                doAction = self.book.update(idBook, data[idBook])
                if doAction == 'true':
                    message = 'update success...'
                    menu = self.alert(message, 'Buku')
                else:
                    message = 'update failed!!!'
                    menu = self.alert(message, 'Buku')

            else:
                message = data
                menu = self.alert(message, 'Buku')
        elif option == 4:
            self.clear_screen()
            self.title("BOOK <Delete>")
            data = self.book.get()
            if isinstance(data, dict):
                Table(data)
                idBook = self.input_k('Input "ID" buku  : ')
                doAction = self.book.delete(idBook)
                if doAction == 'true':
                    message = 'delete success...'
                    menu = self.alert(message, 'Buku')
                else:
                    message = 'delete failed!!!'
                    menu = self.alert(message, 'Buku')                
            else:
                message = data
                menu = self.alert(message, 'Buku')

        else:
            message = 'access not found!!!'
            menu = self.alert(message, 0)


    def __member(self):
        option = int(input('Choose Menu :'))
        if option == 0:
            self.clear_screen()
            self.__home()
            self.__switch('main')
        if option == 1:
            self.clear_screen()
            self.title("MEMBER")
            message = ''
            data = self.member.get()

            if isinstance(data, dict):
                Table(data)
                message = ' Amount Member : <'+str(len(data))+'>'
            else:
                message = data
            menu = self.alert(message, 'Member')

        elif option == 2:
            self.clear_screen()
            self.title("MEMBER <Add>")

            dataInput = {
                'name' : '  +Input "Name Member" : ',
            }
            inputMember = self.input_f(dataInput)

            doAction = self.member.add(inputMember)
            if doAction == 'true':
                message = 'insert success...'
                menu = self.alert(message, 'Member')
            else:
                message = 'insert failed!!!'
                menu = self.alert(message, 'Member')

        elif option == 3:
            self.clear_screen()
            self.title("MEMBER <Edit>")
            data = self.member.get()

            if isinstance(data, dict):
                Table(data)

                idMember = self.input_k('Input "ID" Member  : ')
                doAction = self.member.update(idMember, data[idMember])
                if doAction == 'true':
                    message = 'update success...'
                    menu = self.alert(message, 'Member')
                else:
                    message = 'update failed!!!'
                    menu = self.alert(message, 'Member')

            else:
                message = data
            menu = self.alert(message, 'Member')

        elif option == 4:
            self.clear_screen()
            self.title("MEMBER <Delete>")
            data = self.member.get()

            if isinstance(data, dict):
                Table(data)
                idMember = self.input_k('Input "ID" Member  : ')

                doAction = self.member.delete(idMember)
                if doAction == 'true':
                    message = 'delete success...'
                    menu = self.alert(message, 'Member')
                else:
                    message = 'delete failed!!!'
                    menu = self.alert(message, 'Member')
            else:
                message = data
            menu = self.alert(message, 'Member') 


        else:
            message = 'access not found!!!'
            menu = self.alert(message, 0)


    def __borrow(self):
        option = int(input('Choose Menu : '))
        if option == 0:
            self.clear_screen()
            self.__home()
            self.__switch('main')
        elif option == 1:
            self.clear_screen()
            self.title("Borrow <do>")
            dataMember = self.member.get()
            Table(dataMember)

            idMember = self.input_k(' Input "ID" member : ')


            dataBook = self.book.get()
            Table(dataBook)
            
            idBook = self.input_k(' Input "ID" book : ')

            doAction = self.borrow.do(idMember, dataMember[idMember], idBook, dataBook[idBook])

            if doAction == 'true':
                message = 'borrow success...'
                menu = self.alert(message, 'Pinjam')
            else:
                message = 'borrow failed!!!'
                menu = self.alert(message, 'Pinjam')



        elif option == 2:
            self.clear_screen()
            self.title("Borrow <return>")
            dataMember = self.member.get()

            Table(dataMember)
            idMember = self.input_k(' Input "ID" member : ')
            self.clear_screen()
            self.title("Borrow <return>")
            booksMember = dataMember[idMember]['books']

            if isinstance(booksMember, dict) and len(booksMember) > 0 :
                Table(booksMember)

                idBorrow = self.input_k(' Input "ID" Borrow : ')
                
                if idBorrow in booksMember:
                    statusBorrow = dataMember[idMember]['books'][idBorrow]['status']
                    if statusBorrow == 'false':
                        doAction = self.borrow.re(idMember, dataMember[idMember], idBorrow)
                        if doAction == 'true':
                            message = 'return success...'
                            menu = self.alert(message, 'Pinjam')
                        else:
                            message = 'return failed!!!'
                            menu = self.alert(message, 'Pinjam')
                    else:
                        message = 'book not available!!!'
                        menu = self.alert(message, 'Pinjam')
                else:
                    message = 'book not found!!!'
                    menu = self.alert(message, 'Pinjam')
            else:
                message = 'Books not found!!!'
                menu = self.alert(message, 'Pinjam')

        else:
            message = 'access not found!!!'
            menu = self.alert(message, 0)

app = App()


# book = Book()
# book.get()