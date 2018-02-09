
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date


class PurchaseOrderBool(models.Model):
    _inherit = "res.partner"

    customer_purchase_order_bool = fields.Boolean('Purchase Order Required', help='Requiere anexar Orden de Compra a sus pedidos', default=True, store=True)
