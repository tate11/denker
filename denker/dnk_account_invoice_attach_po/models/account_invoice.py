# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CustomPurchaseOrder(models.Model):
    _inherit = ['account.invoice']

    customer_purchase_order_file = fields.Binary(
        "Purchase Order Document", related='sale_order_id.customer_purchase_order_file',
        readonly=True, store=False)
    filename = fields.Char(related='sale_order_id.filename')
