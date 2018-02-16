# -*- coding: utf-8 -*-
{
    'name' : '-DNK Move Other Information SaleOrder',
    'version' : '1',
    'description': """
        Move the field in Other Information Page to the Main View
    """,
    'category' : 'Sale',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale'],
    'data': [
        'move_other_information.xml',
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
