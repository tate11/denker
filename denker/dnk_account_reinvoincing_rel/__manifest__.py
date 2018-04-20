# -*- coding: utf-8 -*-
{
    'name' : 'dnk_account_reinvoicing_rel',
    'version' : '1',
    'description': """
        This module adds  fields on invoice to relate sale order"
    """,
    'category' : 'Account',
    'author': 'Servicios Corporativos Denker - BC',
    'website': 'www.grupodenker.com',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['account', 'sale'],
    'data': [
        'account_reinvoicing.xml',
    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
