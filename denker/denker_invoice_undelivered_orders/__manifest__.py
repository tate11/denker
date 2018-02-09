# -*- coding: utf-8 -*-
{
    'name': 'Invoice Undelivered Orders',
    'version': '1',
    'description': """
         Sale orders with invoices differences
    """,
    'category': 'Sale',
    # 'depends' : ['sale','custom_dnk'],
    'depends': ['sale'],
    'data': [
        'sale_view.xml',
        # 'security/groups.xml',
        # 'security/ir.model.access.csv',

    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
