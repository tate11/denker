# -*- coding: utf-8 -*-
{
    'name' : '-DNK Link SaleOrder to StockPicking',
    'version' : '1',
    'description': """
        Create a link between the models SaleOrder and StockPicking
    """,
    'category' : 'Sale',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale'],
    'data': [
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
