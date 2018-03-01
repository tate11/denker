# -*- coding: utf-8 -*-
{
    'name': "dnk_sale_commercial_name",

    'summary': """
        Add "Commercial Name" as a search option""",

    'description': """
        This module adds in sale view the "Commercial Company Name" field and adds options to search by this field.
    """,

    'author': "Servicios Corporativos Denker - BC",
    'website': "http://www.grupodenker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '10.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
