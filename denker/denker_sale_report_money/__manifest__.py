# -*- coding: utf-8 -*-
{
    'name' : '-Denker Sale Report Money',
    'version' : '1',
    'description': """
        Creates customized view in sales
    """,
    'category' : 'Sale',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale','denker_sale_report','dnk_add_delivery_status'],
    'data': [
        'sale_view.xml',
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
