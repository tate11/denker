# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Pending Manufacturing Orders",
    "version": "10.0.1.0.1",
    'author': 'SERVICIOS CORPORATIVOS DENKER',
    'website': 'www.grupodenker.com',
    'license': 'AGPL-3',
    "category": "Manufacturing",
    "description": """ This module is to desactivate unused Daily more.
Account Journal Active Field
============================
Adds active field on account journal
    """,
    'depends': ['mrp', 'sale', 'crm'],
    'data': [
        'views/sale_order.xml',
        'views/mrp.xml',
        'views/crm_team.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
}
