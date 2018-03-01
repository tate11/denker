# -*- coding: utf-8 -*-

from odoo import models, fields, api

# lo creo sólo para poder asignarle permisos de lectura  a los nuevos campos que hice.
class dnk_account_promise_to_pay_mod(models.Model):
    _inherit = "account.invoice"
    _name = "dnk.account.promise.to.pay"
