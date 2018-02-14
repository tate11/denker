
# -*- coding: utf-8 -*-
import openerp
from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
from odoo import api, fields, models, tools
import sys


class SubTotalSaleOrder(models.Model):
    _inherit = ['sale.order']

    @api.multi
    @api.depends('amount_untaxed', 'pricelist_id')
    def _get_subtotal(self):
        print('############################ GET SUBTOTAL SALEORDERY')
        ProductPriceList = self.env['product.pricelist']
        ResCurrencyRate = self.env['res.currency.rate']
        tipo_de_cambio = ResCurrencyRate.search([('currency_id', '=', 3)], limit=1, order="name desc")
        if tipo_de_cambio:
            tipo_de_cambio = tipo_de_cambio[0].rate2
        for rec in self:
            subtot = rec.amount_untaxed
            price_list = rec.pricelist_id.id
            currency_id = ProductPriceList.search([('id', '=', price_list)])
            if currency_id:
                currency_id = currency_id[0].currency_id.id
                if currency_id == 34:
                    rec.subtotal_usd = subtot/tipo_de_cambio
                elif currency_id == 3:
                    rec.subtotal_usd = subtot
                else:
                    rec.subtotal_usd = -1
            print('AmountUntax: '+str(subtot)+' Currency ID: '+str(currency_id)+' Tipo de cambio: '+str(tipo_de_cambio)+' SubTotal: '+str(rec.subtotal_usd))
        return

    subtotal_usd = fields.Float("SubTotal USD", compute="_get_subtotal", store=True)
