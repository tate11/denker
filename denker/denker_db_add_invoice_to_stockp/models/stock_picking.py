# -*- coding: utf-8 -*-
from odoo import models, fields, api


class account_invoice_to_stock_piking(models.Model):
    _inherit = ['stock.picking']

    invoice_id = fields.Many2one('account.invoice', string='Invoice', readonly=True, default=False)
