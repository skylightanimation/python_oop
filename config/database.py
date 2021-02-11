class Database():

    _books = {
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

    _members = {
        'MEMBER_1': {
            'id'    : '1',
            'name'  : 'darma',
            'books' : {}
        },
        'MEMBER_2': {
            'id'    : '2',
            'name'  : 'Roy',
            'books' : {
               'BUK_3' : {
                    'id':'3',
                    'title'  :'A Gate of Night',
                    'year'  :'2014',
                    'author':'Bella Forrest',
                },
            },
        }, 
    }


        # 'MEMBER_2': {
        #     'id'    : '2',
        #     'name'  : 'Roy',
        #     'books' : {
        #        'BUK_3' : {
        #             'title'     : 'A Gate of Night',
        #             'year'      : '2014',
        #             'author'    : 'Bella Forrest',
        #             'date_out'  : '2021-02-01 08:40:43',
        #             'date_in'   : '2021-02-08 19:20:27',
        #             'status'    : 'true'
        #         },
        #     },
        # }, 