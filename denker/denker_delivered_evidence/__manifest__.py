# -*- coding: utf-8 -*-
{
    'name' : '-Denker Delivered Evidence',
    'version' : '1',
    'description': """
        Agrega el campo 'evidencia de entrega' a la orden de entrega, el campo es de tipo imagen\n
    """,
    'category' : 'Inventory',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['stock'],
    'data': [
        'delivered_evidence.xml',
    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
