{
    'name': "test_task_module",

    'summary': "",


    'author': "Andry",

    'category': 'Cusomizations',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/respartner.xml',
        'views/route.xml',
        'views/order.xml',
        'views/orderline.xml',
        'views/product.xml',
        'views/car.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
