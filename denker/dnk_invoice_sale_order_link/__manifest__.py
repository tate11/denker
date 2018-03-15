# -*- coding: utf-8 -*-
{
    'name': "Invoice - Sale Order Link",

    'summary': """
        Adds a link between an Invoice and its Sale Order source.""",

    'description': """
        Resume:
        Adds a field sale_id on the object "account.invoice", which is the reverse many2one field of the field invoice_id of the object "sale.order".

        Description:
        On the customer invoice report, you usually need to display the customer order number.
        For that, you need to have the link from invoices to sale order, and this link is not available in the official addons.

        This module adds a field sale_id on the object account.invoice, which is the reverse one2many field of the field invoice_id of the object sale.order.
        It is displayed in the "Other Information" tab on the invoice form view.

        Please contact José Candelas from Grupo Denker <jcandelas@grupodenker.com> for any help or question about this module.""",

    'author': "Grupo Denker - José Candelas - jcandelas@grupodenker.com",
    'website': "http://www.grupodenker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '10.0.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_invoice_views.xml',
    ],
}
