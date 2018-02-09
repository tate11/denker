# -*- coding: utf-8 -*-
{
    'name': "denker_project_task",

    'summary': """
        Add new fields to project task such as:
        priority, requestor, evidence, etc.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "José Candelas",
    'website': "http://www.grupodenker.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_task_view.xml',
    ],
}
