
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date


class AccountingInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    @api.onchange('partner_id', 'company_id')
    def _onchange_dnk_partner_id(self):
        print("Entro a OnChange Cliente")
        metodo_pago_id = False
        uso_cfdi_id = False
        company_id = self.company_id.id
        p = self.partner_id if not company_id else self.partner_id.with_context(force_company=company_id)
        type = self.type
        if p:
            metodo_pago_id = p.metodo_pago_id
            uso_cfdi_id = p.uso_cfdi_id
        self.metodo_pago_id = metodo_pago_id
        self.uso_cfdi_id = uso_cfdi_id
        return
