
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date


class SaleOrderPartner(models.Model):
    _inherit = "sale.order"

    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrderPartner, self)._prepare_invoice()
        res.update({'metodo_pago_id': self.partner_id.metodo_pago_id.id or False,
                    'uso_cfdi_id': self.partner_id.uso_cfdi_id.id or False,
                    'payment_term_id': self.partner_id.property_payment_term_id.id or False, })
        return res
