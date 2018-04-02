# -*- coding: utf-8 -*-
{
    'name' : 'Denker Delivery Evidence in Invoice',
    'version' : '1',
    'description': """
        This module adds an image field to invoice as delivery evidence"
    """,
    'category' : 'Account',
    'author': 'Servicios Corporativos Denker - BC',
    'website': 'www.grupodenker.com',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['account'],
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
