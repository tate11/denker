# -*- coding: utf-8 -*-
{
    'name': "Denker Promise To Pay DB",

    'summary': """
        Promise To pay and Payment solution""",

    'description': """
        This module adds to DB the Promise To Pay and  Payment Solution fields
    """,

    'author': "Servicios Corporativos Denker - BC",
    'website': "http://www.grupodenker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Account Invoice',
    'version': '10.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'data/payment_solution_data.xml',
        # 'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
