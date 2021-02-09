import os

books = {
    'BUK_1': {
        'id':'1',
        'name'  :'Merah Putih',
        'year'  :'1983',
        'author':'Hersevien M. Taulu'
    }, 
    'BUK_2': {
        'id':'2',
        'name'  :'Sang Pemimpi',
        'year'  :'2006',
        'author':'Andrea Hirata'   
    }, 'BUK_3': {
        'id':'3',
        'name'  :'A Gate of Night',
        'year'  :'2014',
        'author':'Bella Forrest'  
    }
}


# interface
def __init__():
    os.system('clear')
    print(" PERPUSTAKAAN MENU ")
    print("1. Daftar Buku")
    print("2. Tambah Buku")
    print("3. Update Buku")
    print("4. Delete Buku")
    print("0. Exit")

    mainMenu = int(input("Pilih Menu :"))
    menu(mainMenu)

def menu(mainMenu):
    if mainMenu == 0:
        print("exit, success")
        quit()
    elif mainMenu == 1:
        print("Menu : Daftar Buku")
        print("------------------")
        view()         
        message = 'Jumlah Buku '+str(len(books))
        alert(message, 1) 

    elif mainMenu == 2:
        print("Menu : Tambah Buku")
        print("------------------")

        insert()

    elif mainMenu == 3:
        print("Menu : Update Buku")
        print("------------------")        
        view()
        inputUpdate = input('input ID Buku yang akan diupdate : ')
        if inputUpdate != '':
            update(inputUpdate)
        else:
            message = 'ID buku tidak diketahui'
            alert(message, 3)
    
    elif mainMenu == 4:
        print("Menu : Delete Buku")
        print("------------------")

        view()
        inputDelete = input('input ID Buku yang akan dihapus : ')
        if inputDelete != '':
            delete(inputDelete)
        else:
            message = 'ID buku tidak diketahui'
            alert(message, 4)
    

    else:
        message = "Menu yang anda inputkan tidak tersedia"
        alert(message, 0)

def alert(message, menuOption):
    # os.system('clear')
    print(message)
    # print(menu)
    redirect = input('"ENTER" untk kembali ke Menu atau "y" untuk stay.. ')
    if redirect == "y" or redirect == "Y":
        menu(int(menuOption))
        os.system('clear')
    else:
        __init__()
        os.system('clear')


# helper
def generateId():
    idTemp = 0
    for key in books:

        idBook = int(books[key]['id'])      
        if idBook == 0:
            idTemp = idBook
            # print(idTemp)
        elif idTemp < idBook:
            idTemp = idBook
            # print(idTemp)
        else:
            print('error')
    
    # print('Last Vlaue :'+idTemp)
    # idTemp += idTemp
    idNew = idTemp + 1
    return idNew


# CRUD
def view():

    if len(books) == 0:
        # print("")
        message = 'data buku kosong...'
        alert(message, 1)
    else:
        print(" ID       | NAME         | YEAR          | AUTHOR           ")
        for key in books:
            keyBook = key
            idBook = books[key]['id']
            nameBook = books[key]['name']
            yearBook = books[key]['year']
            authorBook = books[key]['author']
            print(keyBook+'   | '+nameBook+'    | '+yearBook+'  | '+authorBook)

def insert():
   
    nameBook = input("  +Input nama buku : ")
    yearBook = input("  +Input tahun buku : ")
    nameAuthor = input("  +Input nama author : ")

    if nameBook != '' and yearBook != '' and nameAuthor != '':
        
        getId = str(generateId())
        idBook = 'BUK_'+getId
        book = {}
        book['id'] = getId
        book['name'] = nameBook
        book['year'] = yearBook
        book['author'] = nameAuthor

        books[idBook] = book
        message = 'input buku, success...'
        alert(message, 2)
    else:
        message = 'input buku, gagal!!!'
        alert(message, 2)        

def delete(key):
    print(key)
    books.pop(key)
    message = 'delete success...' 
    alert(message, 3)

def update(key):

    idBook = books[key]['id']
    nameBook = books[key]['name']
    yearBook = books[key]['year']
    authorBook = books[key]['author']

    print('Name : '+nameBook)
    print('Year : '+yearBook)
    print('Author : '+authorBook)

    nameBookUpdate = input("  +Update nama buku : ")
    yearBookUpdate = input("  +Update tahun buku : ")
    nameAuthorUpdate = input("  +Update nama author : ")

    if nameBookUpdate != '' and yearBookUpdate != '' and nameAuthorUpdate != '':
        
        book = {}
        book['id'] = idBook
        book['name'] = nameBookUpdate
        book['year'] = yearBookUpdate
        book['author'] = nameAuthorUpdate

        books[key] = book
        message = 'update buku, success...'
        alert(message, 4)
    else:
        message = 'update buku, gagal!!!'
        alert(message, 4) 


__init__()