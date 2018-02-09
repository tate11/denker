# -*- coding: utf-8 -*-
{
    'name' : '-Denker Add Customer Purchase Bool',
    'version' : '1',
    'description': """
        Agrega un campo booleano a clientes para identificar si sus pedidos requieren orden de compra\n
    """,
    'category' : 'Partner',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale','account'],
    'data': [
        'purchase_order_bool.xml',
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
