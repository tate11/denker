# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderCorrectionsModel(models.Model):
    _name = "dnk.sale.order.corrections.model"
    _rec_name = 'name'
    _order = 'sequence,name'
    name = fields.Char('Name')
    sequence = fields.Integer('Sequence')
