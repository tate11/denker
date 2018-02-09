{
    "name": "Add Invoice to Sock Picking ",
    "version": "10.0.1.0.1",
    'author': 'Servicios Corporativos Denker - BC',
    'website': 'www.grupodenker.com',
    'license': 'AGPL-3',
    "category": "Stock_picking - Account Invoice",
    "description": """ This module adds the Invoice Field to Stock Picking Form and Account Invoice PDF View """,
    'depends': ['account', 'stock'],
    'data': [
        'views/stock_picking.xml',
        'views/account_invoice.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
}
