
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
from functions import add_business_days
import pytz


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def _compute_delivery_days(self):
        for rec in self:
            date_order = rec.order_id.date_order
            commitment_date = rec.order_id.commitment_date
            if date_order and commitment_date:
                date_order = datetime.strptime(str(date_order), "%Y-%m-%d %H:%M:%S")
                commitment_date = datetime.strptime(str(commitment_date), "%Y-%m-%d %H:%M:%S")
                days = int((commitment_date - date_order).days)
                rec.delivery_days = days
        return

    @api.multi
    def _compute_mail_qty(self):
        for rec in self:
            qty = 0
            if rec.order_id.message_ids:
                for message in rec.order_id.message_ids:
                    if message.message_type in ('email', 'comment'):
                        qty += 1
                        rec.date_last_mail = message.date
                rec.mail_qty = qty
        return

    @api.multi
    def _get_commitment_date(self):
        for rec in self:
            if rec.order_id.commitment_date:
                rec.commitment_date = rec.order_id.commitment_date
        return

    @api.multi
    @api.depends('product_uom_qty', 'qty_delivered')
    def _compute_remaining_qty(self):
        for rec in self:
            remaining_qty = 0
            remaining_qty = rec.product_uom_qty - rec.qty_delivered
            rec.remaining_qty = remaining_qty
        return

    @api.multi
    def _compute_manufacturing_order2(self):
        MrpProduction = self.env['mrp.production']
        for rec in self:
            mrparray = MrpProduction.search([('origin','=',rec.order_id.name)])
            if mrparray:
                for elem in mrparray:
                    if elem.product_id.id == rec.product_id.id:
                        rec.route_order = elem.routing_id.name
                        rec.manufacturing_order = elem.id
        return

    @api.multi
    def _compute_mo_stock_diff(self):
        for rec in self:
            res = rec.product_id._compute_quantities_dict\
                (self._context.get('lot_id'), self._context.get('owner_id'), self._context.get('package_id'),\
                 self._context.get('from_date'), self._context.get('to_date'))
            rec.mo_stock_diff = res[rec.product_id.id]['qty_available'] - rec.product_uom_qty
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
    @api.depends('product_uom_qty', 'qty_delivered')
    def _compute_order_delivered(self):
        for rec in self:
            delivered = False
            if rec.order_id:
                delivered = True
                for line in rec.order_id.order_line:
                    if not (line.product_uom_qty - line.qty_delivered) == 0:
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
    @api.depends('product_id')
    def _compute_commitment_date(self):
        for record in self:
            if record.date_order and not record.product_delivery_date:
                fechaped = datetime.strptime(record.date_order, '%Y-%m-%d')
                fechaconf = add_business_days(fechaped,record.delivery_days)
                equivodeventa = record.order_id.team_id.name
                dias = 0
                if equivodeventa == "Guadalajara": dias = 1
                elif equivodeventa == "Chihuahua": dias = 3
                elif equivodeventa == "Ciudad Juárez": dias = 3
                elif equivodeventa == "Tijuana": dias = 4
                elif equivodeventa == "Reynosa": dias = 3
                elif equivodeventa == "Estado de México": dias = 4
                elif equivodeventa == "Aguascalientes": dias = 2
                elif equivodeventa == "Monterrey": dias = 3
                elif equivodeventa == "Nogales": dias = 3
                elif equivodeventa == "Querétaro": dias = 2
                elif equivodeventa == "Sudámerica": dias = 0
                fechaconf = add_business_days(fechaconf,dias)
                record.product_delivery_date = fechaconf
        return

    @api.multi
    @api.depends('product_id')
    def _compute_days_fabrication(self):
        for rec in self:
            if rec.date_order:
                res = rec.product_id.produce_delay
                fechaped = datetime.strptime(rec.date_order, '%Y-%m-%d')
                fechafab = add_business_days(fechaped,res)
                rec.fabrication_date = fechafab
        return

    @api.multi
    @api.depends('product_id')
    def _get_sales_team(self):
        for rec in self:
            rec.sales_team = rec.order_id.team_id.name
        return

    @api.multi
    @api.depends('product_id')
    def _get_product_family(self):
        for rec in self:
            rec.product_family = rec.product_id.categ_id.parent_id.name
        return

    @api.multi
    @api.depends('order_id.date_order')
    def _get_date_order(self):
        for rec in self:
            rec.date_order = datetime.strptime(rec.order_id.date_order, '%Y-%m-%d %H:%M:%S')
        return

    product_delivery_date = fields.Date("Fecha de Entrega", compute='_compute_commitment_date', store=True)
    delivery_days = fields.Integer('Days', compute='_compute_delivery_days')
    date_last_mail = fields.Datetime('Date Last Mail', compute='_compute_mail_qty')
    formatted_date_last_mail = fields.Char('Date Last Mail', compute='_compute_date_last_mail')
    mail_qty = fields.Integer('Mail Qty', compute='_compute_mail_qty')
    date_order = fields.Date('Date Order', compute='_get_date_order', readonly=True, store=True)
    sales_team = fields.Char('Sales Team', compute='_get_sales_team', store=True)
    product_family = fields.Char('Product Family', compute='_get_product_family', readonly=True, store=True)
    order_delivered = fields.Boolean('Order delivered', compute='_compute_order_delivered', readonly=True)
    commitment_date = fields.Datetime('Commitment Date', compute='_get_commitment_date')
    #commitment_date2 = fields.Datetime('Commitment Date2', compute='_compute_commitment_date', readonly=True, store=True)
    client_order_ref = fields.Char('Client order ref', related='order_id.client_order_ref', readonly=True)
    remaining_qty = fields.Integer('Remaining Qty', compute='_compute_remaining_qty', readonly=True, store=True)
    manufacturing_order = fields.Many2one('mrp.production', 'Manufacturing Order', compute='_compute_manufacturing_order2', readonly=True)
    route_order = fields.Char('Routing Production', compute='_compute_manufacturing_order2')
    mo_date_start = fields.Date('MO Date Start', compute='_compute_manufacturing_order2', readonly=True)
    mo_date_end = fields.Date('MO Date Finished', compute='_compute_manufacturing_order2', readonly=True)
    mo_stock_diff = fields.Integer('Stock Difference', compute='_compute_mo_stock_diff', readonly=True)
    days_to_date = fields.Integer('Days to Date', compute='_compute_days_to_date')
    late = fields.Boolean('Late', compute='_compute_days_to_date')
    int_product_qty = fields.Integer('Product qty', compute='_compute_int_product_qty')
    fabrication_date = fields.Date('Fabrication Date', compute='_compute_days_fabrication', readonly=True, store=True)
    delivery_status = fields.Char('Delivery Status', related='order_id.delivery_status', store=True)
    text_color = fields.Char('Text Color', related='order_id.text_color', store=False)
    text_bold = fields.Boolean('Text Style', related='order_id.text_bold', store=False)
    supply_filter = fields.Boolean('Supply Filter', related='order_id.supply_filter', store=True)
