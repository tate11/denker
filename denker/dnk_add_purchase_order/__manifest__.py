# -*- coding: utf-8 -*-
{
    'name' : '-Denker Add Purchase Order',
    'version' : '1',
    'description': """
        Agrega el campo 'order de compra' como attach al pedido, obligatorio para avanzar\n
    """,
    'category' : 'Inventory',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale'],
    'data': [
        'add_purchase_order.xml',
    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
