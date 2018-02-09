# -*- coding: utf-8 -*-
{
    'name' : '-Denker Show Cost Variants',
    'version' : '1',
    'description': """
        Show Cost Field in Variants
    """,
    'category' : 'Inventory',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale','stock','product_hide_cost'],
    'data': [
        'show_cost_variants.xml',
    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
