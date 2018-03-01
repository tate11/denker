# -*- coding: utf-8 -*-
{
    'name': "-DNK Order Corrections",

    'summary': """
        Sale Order Corrections""",

    'description': """
        Add Field 'Order Correction' to Sale Model\n
    """,

    'author': "Servicios Corporativos Denker - DAG",
    'website': "http://www.grupodenker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale Order',
    'version': '10.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','dnk_order_corrections_db'],

    # always loaded
    'data': [
        'order_corrections.xml',
        # 'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
