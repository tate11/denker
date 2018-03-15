# -*- coding: utf-8 -*-
{
    'name': "Account Invoice Attach Purchase Order",

    'summary': """
        Attach the Purchase Order Document linked to the Sale Order to send
        the invoice to the customer""",

    'description': """
        This module depends of the "dnk_add_purchase_order" module that adds a field to attach
        the purchase order to the sale order.

        The function of this module can be configurated for every customer in
        the "Sale and Purchase" tab.
    """,

    'author': "Grupo Denker - José Candelas - jcandelas@grupodenker.com",
    'website': "http://www.grupodenker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Account',
    'version': '10.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account', 'dnk_add_purchase_order', 'dnk_invoice_sale_order_link'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_invloice_views.xml',
        'views/partner_views.xml',
    ],
}
