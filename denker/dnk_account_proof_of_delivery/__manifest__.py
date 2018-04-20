# -*- coding: utf-8 -*-
{
    'name' : 'Denker Proof of delivery in Invoice',
    'version' : '1',
    'description': """
        This module adds an image field to invoice as proof of delivery"
    """,
    'category' : 'Account',
    'author': 'Servicios Corporativos Denker - BC',
    'website': 'www.grupodenker.com',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['account'],
    'data': [
        'proof_of_delivery.xml',
    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
