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
            'name'  : 'ar_ma',
            'books' : {}
        },
        'MEMBER_2': {
            'id'    : '2',
            'name'  : 'Roy',
            'books' : {
               'BUK_30201' : {
                    'id'        : '0201',
                    'title'     : 'A Gate of Night',
                    'author'    : 'Bella Forrest',
                    'date_out'  : '2021-02-01',
                    'date_in'   : '2021-02-08',
                    'status'    : 'true'
                },
            },
        }, 
    }