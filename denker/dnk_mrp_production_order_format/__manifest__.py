# -*- coding: utf-8 -*-
{
    'name': 'Mod Production Order Report',
    'version': '1.0',
    'category': 'Denker',
    'description': """
    This module modify pdf format of Production Order Report
    """,
    'author': 'Servicios Corporativos Denker - BC',
    'website': 'www.grupodenker.com',
    'depends': ['mrp'],
    'data': [
        'report/mrp_report_view.xml',
        'mrp_report_format.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
