# books = {'BUK_1': {'id':'1'}, 'BUK_2': {'id':'2'}, 'BUK_3': {'id':'3'}} 
# # d.items()
# # print(d['x'])
# # print(d['x']['z'])
# # print(d.items())

# def generateId():
#     idTemp = 0
#     for key in books:
#         # print (key)
#         idBook = int(books[key]['id'])
#         # print(idBook)
#         if idTemp == 0:
#             idTemp = idBook
#             print(idTemp)
#         elif idTemp < idBook:
#             idTemp = idBook
#             print(idTemp)
#         else:
#             print('error')
    
#     idTemp += 1
#     idNew = 'BUK_'+str(idTemp)
#     return idNew

# value = generateId()

# print(value)

# print(chr(27) + "[2J")
# print(chr(27))
# print("[2J")