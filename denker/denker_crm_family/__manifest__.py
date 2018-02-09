# -*- coding: utf-8 -*-
{
    'name': "denker_crm_family",

    'summary': """
        Makes not required the field family_id (field added by custom_dnk module),
        the field is going to be required only when the lead is converted in opportunity
    """,

    'description': """
        Makes not required the field family_id (field added by custom_dnk module),
        the field is going to be required only when the lead is converted in opportunity
    """,

    'author': "José Candelas",
    'website': "http://www.grupodenker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'custom_dnk'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
