# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date


class PurchaseOrderBool(models.Model):
    _inherit = "res.partner"

    attach_purchase_order_to_invoice_mail = fields.Boolean(
        'Attach PO to Invoice Mail', help='¿Adjuntar Orden de Compra al enviar la factura?',
        default=True, store=True)
