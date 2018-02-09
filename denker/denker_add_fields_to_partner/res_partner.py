
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date


class ResPartner(models.Model):
    _inherit = "res.partner"

    metodo_pago_id = fields.Many2one('sat.metodo.pago', string='Método de Pago', help='Método de Pago Requerido por el SAT', default=2)
    uso_cfdi_id = fields.Many2one('sat.uso.cfdi', string='Uso CFDI', help='Método de Pago Requerido por el SAT', default=22)
