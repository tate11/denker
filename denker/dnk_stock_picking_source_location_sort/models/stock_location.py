# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Location(models.Model):
    _inherit = "stock.location"

    sequence = fields.Integer('Sequence', default=1, help="Sequence to sort \"Stock Pickings\" in Sales Orders")
