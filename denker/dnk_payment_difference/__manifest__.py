# -*- coding: utf-8 -*-
{
    'name' : '-Denker Payment Difference',
    'version' : '1',
    'description': """
        Creates customized view in sales
    """,
    'category' : 'Sale',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale','account'],
    'data': [
        'payment_difference_view.xml',
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
