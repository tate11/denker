# -*- coding: utf-8 -*-
{
    'name' : '-DNK Add Duedate To Invoice View',
    'version' : '1',
    'description': """
        Add the duedate invoice field to the main view of Account Invoice\n
    """,
    'category' : 'Sale',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['account'],
    'data': [
        'add_duedate_invoice.xml',
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
