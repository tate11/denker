# -*- coding: utf-8 -*-
{
    'name' : '-DNK Add Delivery Status',
    'version' : '1',
    'description': """
        Add Field 'Delivery Status' to the table 'sale_order'
    """,
    'category' : 'Sale',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale','dnk_link_saleorder_stockpicking'],
    'data': [
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
