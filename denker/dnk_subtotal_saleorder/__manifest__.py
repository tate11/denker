# -*- coding: utf-8 -*-
{
    'name' : '-DNK Subtotal SaleOrder',
    'version' : '1',
    'description': """
        Replace Total for Subtotal in the TreeView in SaleOrder
    """,
    'category' : 'Sale',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale'],
    'data': [
        'subtotal_sale_view.xml'
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
