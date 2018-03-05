# -*- coding: utf-8 -*-
{
    'name' : '-Denker Delivered Evidence V2',
    'version' : '1',
    'description': """
        Este módulo es el complemento de -Denker Delivered Evidence\n
        Esta versión 2 agrega que la evidencia de entrega sea también obligatoria cuando el ubicación destino contenga 'tránsito'\n
        Támbien corrige el error que duplicaba la evidencia de entrega en las BackOrders
    """,
    'category' : 'Inventory',
    #'depends' : ['sale','custom_dnk'],
    'depends' : ['stock','denker_delivered_evidence'],
    'data': [
        'delivered_evidence_v2.xml',
    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
