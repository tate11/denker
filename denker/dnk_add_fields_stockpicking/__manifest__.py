# -*- coding: utf-8 -*-
{
    'name' : '-Denker Add Fields To StockPicking',
    'version' : '1',
    'description': """
        Add fields to StockPicking tree view
    """,
    'category' : 'Partner',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale','account'],
    'data': [
        'add_fields_stockpicking.xml',
        #'security/groups.xml',
        #'security/ir.model.access.csv',

    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
