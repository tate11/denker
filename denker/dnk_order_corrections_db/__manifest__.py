# -*- coding: utf-8 -*-
{
    'name': "-DNK Order Corrections DB",

    'summary': """
        Sale Order Corrections Values DB""",

    'description': """
        Create New Status in the DB to Sale Corrections Field\n
    """,

    'author': "Servicios Corporativos Denker - DAG",
    'website': "http://www.grupodenker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale Order',
    'version': '10.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'data/order_corrections_data.xml',
        # 'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
