# -*- coding: utf-8 -*-
{
    'name': 'Denker Mod Invoice Format',
    'version': '10.0.0.1',
    'category': 'Denker',
    'description': """
    This module modifys the Invoice Form, add filters to customer.
    """,
    'author': 'Servicios Corporativos Denker - BC',
    'website': 'www.grupodenker.com',
    'depends': ['account'],
    'data': [
        'views/account_invoice_form.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
