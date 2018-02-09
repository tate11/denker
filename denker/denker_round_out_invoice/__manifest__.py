# -*- coding: utf-8 -*-
{
    'name' : '-Denker Round Out Invoice',
    'version' : '1',
    'description': """
        Redondea en la vista de factura los campos de Subtotal, Impuestos y Total de 4 a 2 decimales\n
        Se modificó también los mismos campos directamente la vista 'view_invoice_line_calendar'\n
    """,
    'category' : 'Invoice',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale','account'],
    'data': [
        'round_out_invoice.xml',
        'round_out_invoice_supplier.xml',
    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
