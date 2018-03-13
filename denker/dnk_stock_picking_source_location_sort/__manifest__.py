# -*- coding: utf-8 -*-
{
    'name': "Dnk - Stock Picking Source Location Sort",

    'summary': """
        You can sort the Pickings from a Sale Order with the new field "Sequence",
        The "Sequence" is set on the "Stock Location" model from the "Stock Location Source"
        of the Picking
    """,

    'description': """
    """,

    'author': "Grupo Denker - José Candelas - jcandelas@grupodenker.com",
    'website': "http://www.grupodenker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Stock',
    'version': '10.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_location_views.xml',
        'views/stock_picking_views.xml',
    ],
}
