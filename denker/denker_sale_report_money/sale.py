
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
from functions import add_business_days
import pytz


class SaleOrderLineMoney(models.Model):
    _inherit = "sale.order.line"


    @api.multi
    def _compute_delivery_days(self):
        for rec in self:
            date_order = rec.order_id.date_order
            commitment_date = rec.order_id.commitment_date
            if date_order and commitment_date:
                date_order = datetime.strptime(str(date_order),"%Y-%m-%d %H:%M:%S")
                commitment_date = datetime.strptime(str(commitment_date),"%Y-%m-%d %H:%M:%S")
                days = int((commitment_date - date_order).days)
                rec.delivery_days = days
        return


    @api.multi
    def _compute_mail_qty(self):
        for rec in self:
            qty = 0
            if rec.order_id.message_ids:
                for message in rec.order_id.message_ids:
                    if message.message_type in ('email','comment'):
                        qty += 1
                        rec.date_last_mail = message.date
                rec.mail_qty = qty
        return

    @api.multi
    def _compute_days_to_date(self):
        for rec in self:
            now = str(datetime.now())
            now = now.split('.')[0]
            now = datetime.strptime(str(now),"%Y-%m-%d %H:%M:%S")
            days_to_date = 0
            if rec.date_order:
                date_order = datetime.strptime(str(rec.date_order),"%Y-%m-%d")
                days = int((now - date_order).days)
                days_to_date = days
            rec.days_to_date = days_to_date
            if days_to_date > rec.delivery_days:
                rec.late = True
        return

    @api.multi
    def _compute_int_product_qty(self):
        for rec in self:
            rec.int_product_qty = rec.product_uom_qty
        return

    @api.multi
    @api.depends('product_uom_qty','qty_delivered')
    def _compute_order_delivered(self):
        for rec in self:
            delivered = False
            if rec.order_id:
                delivered = True
                for line in rec.order_id.order_line:
                    if not (line.product_uom_qty - line.qty_delivered) == 0:
                        print 'not delivered'
                        delivered = False
            rec.order_delivered = delivered
        return


    @api.depends('date_last_mail')
    @api.multi
    def _compute_date_last_mail(self):
        for record in self:
            if record.date_last_mail: record.formatted_date_last_mail = datetime.strptime(record.date_last_mail, '%Y-%m-%d %H:%M:%S').strftime('%d-%b')
        return

    @api.multi
    @api.depends('remaining_qty','order_id.pricelist_id', 'price_unit', 'product_uom_qty','order_id')
    def _get_price_order_line(self):
        #SaleOrder = self.env['sale.order']
        ProductPriceList = self.env['product.pricelist']
        ResCurrencyRate = self.env['res.currency.rate']
        tipo_de_cambio = ResCurrencyRate.search([('currency_id','=',3)], limit=1, order="name desc")
        if tipo_de_cambio:
            tipo_de_cambio = tipo_de_cambio[0].rate2
        for rec in self:
            remaining_price = rec.price_unit * rec.remaining_qty
            #price_list = SaleOrder.search([('id','=',rec.order_id.name[2:])])
            #if price_list:
            #price_list = price_list[0].pricelist_id.id
            price_list = rec.order_id.pricelist_id.id
            currency_id = ProductPriceList.search([('id','=',price_list)])
            if currency_id:
                currency_id = currency_id[0].currency_id.id
                if currency_id == 34:
                    rec.price_order_line = remaining_price
                    rec.price_order_line_usd = remaining_price/tipo_de_cambio
                elif currency_id == 3:
                    rec.price_order_line = remaining_price*tipo_de_cambio
                    rec.price_order_line_usd = remaining_price
                else:
                    rec.price_order_line = 0
                    rec.price_order_line_usd = -1
            else:
                rec.price_order_line = -1
                rec.price_order_line_usd = 0
            #else:
                #rec.price_order_line = -1
                #rec.price_order_line_usd = -1
        return

    price_order_line = fields.Integer('Price Order Line',compute='_get_price_order_line', store=True)
    price_order_line_usd = fields.Integer('Price Order Line USD',compute='_get_price_order_line', store=True)
    delivery_days = fields.Integer('Days',compute='_compute_delivery_days')
    date_last_mail = fields.Datetime('Date Last Mail',compute='_compute_mail_qty')
    formatted_date_last_mail = fields.Char('Date Last Mail',compute='_compute_date_last_mail')
    mail_qty = fields.Integer('Mail Qty',compute='_compute_mail_qty')
    client_order_ref = fields.Char('Client order ref', related='order_id.client_order_ref', readonly=True)
    days_to_date = fields.Integer('Days to Date',compute='_compute_days_to_date')
    late = fields.Boolean('Late',compute='_compute_days_to_date')
    int_product_qty = fields.Integer('Product qty',compute='_compute_int_product_qty')
