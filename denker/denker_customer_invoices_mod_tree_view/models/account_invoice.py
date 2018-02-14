# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields, api, _
from datetime import datetime, timedelta, date


class crm_team_transit_days(models.Model):
    _inherit = "account.invoice"

    @api.multi
    @api.depends('amount_total_signed')
    def _get_invoice_amount_usd(self):
        res_currency_rate = self.env['res.currency.rate']
        for rec in self:
            rec.amount_untaxed_usd = -2
            rec.amount_untaxed_mxn = -2
            rec.exchange_rate = 17
            if rec.date_invoice:
                ob_date_invoice = datetime.strptime(rec.date_invoice, '%Y-%m-%d')
                ob_exchange_date = ob_date_invoice - timedelta(days=1)
            else:
                ob_exchange_date = datetime.strptime(rec.create_date, '%Y-%m-%d %H:%M:%S')
            string_exchange_date = datetime.strftime(ob_exchange_date, "%Y-%m-%d")
            rec.exchange_rate = res_currency_rate.search([('currency_id', '=', 3), ('name', '<=', string_exchange_date)], limit=1, order="name desc").rate2

            # Calcular el adeudo en USD
            rec.last_exchange_rate = res_currency_rate.search([('currency_id', '=', 3)], limit=1, order="name desc").rate2
            if rec.last_exchange_rate:
                if rec.currency_id.name == 'USD':
                    rec.residual_usd = rec.residual
                elif rec.currency_id.name == 'MXN':
                    rec.residual_usd = rec.residual / rec.last_exchange_rate
                else:
                    rec.residual_usd = -1
            else:
                rec.residual_usd = -1
                rec.last_exchange_rate = 0

            # calcular el monto de la factura en MXN y USD
            if rec.exchange_rate > 0:
                if rec.currency_id.name == 'USD':
                    rec.amount_untaxed_usd = rec.amount_untaxed
                    rec.amount_untaxed_mxn = rec.amount_untaxed * rec.exchange_rate
                elif rec.currency_id.name == 'MXN':
                    rec.amount_untaxed_mxn = rec.amount_untaxed
                    rec.amount_untaxed_usd = rec.amount_untaxed / rec.exchange_rate
                else:
                    rec.amount_untaxed_usd = -1
                    rec.amount_untaxed_mxn = -1
            else:
                    rec.amount_untaxed_usd = 0
                    rec.amount_untaxed_mxn = 0
            if rec.amount_total_signed < 0:
                rec.amount_untaxed_usd = rec.amount_untaxed_usd * -1
                rec.amount_untaxed_mxn = rec.amount_untaxed_mxn * -1
        return

    amount_untaxed_usd = fields.Float('Subtotal USD', digits=(10, 4),  compute='_get_invoice_amount_usd', store=True)
    amount_untaxed_mxn = fields.Float('Subtotal MXN', digits=(10, 4), compute='_get_invoice_amount_usd', store=True)
    exchange_rate = fields.Float('Exchange Rate', digits=(5, 4), compute='_get_invoice_amount_usd')
    last_exchange_rate = fields.Float('Last Exchange Rate', digits=(5, 4), compute='_get_invoice_amount_usd')
    residual_usd = fields.Float('Residual USD', digits=(5, 4), compute='_get_invoice_amount_usd')
