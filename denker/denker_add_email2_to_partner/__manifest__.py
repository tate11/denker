# -*- coding: utf-8 -*-
{
    'name' : '-Denker Add Email2 To Partner',
    'version' : '1',
    'description': """
        Se modificaron los siguientes archivos de odoo10prod/enterprise/account_reports:\n\n
        views/account_report_view.xml (email cambio a email2)\n
        models/account_followup_report.py (email cambio a email2)

    """,
    'category' : 'Partner',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['sale','account'],
    'data': [
        'res_partner_view.xml',
        #'security/groups.xml',
        #'security/ir.model.access.csv',

    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
