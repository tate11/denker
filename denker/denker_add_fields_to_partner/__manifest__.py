# -*- coding: utf-8 -*-
{
    'name' : '-Denker Add Fields To Partner',
    'version' : '1',
    'description': """
        Creates customized view in sales
    """,
    'category' : 'Partner',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale','account'],
    'data': [
        'res_partner_view.xml',
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
