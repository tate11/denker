# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
from functions import sub_business_days
# import pytz


class mrp_production_planned_end(models.Model):
    _inherit = "mrp.production"

    @api.depends('origin')
    @api.multi
    def _compute_sale_order_data(self):
        SaleOrder = self.env['sale.order']
        for rec in self:
            listSalesOrder = SaleOrder.search([('name', '=', rec.origin)])
            if listSalesOrder:
                if rec.create_date:
                    rec.capture_days = (datetime.strptime(rec.create_date, "%Y-%m-%d %H:%M:%S") - datetime.strptime(listSalesOrder[0].create_date, "%Y-%m-%d %H:%M:%S")).days

                rec.sale_order_create_date = datetime.strptime(listSalesOrder[0].create_date, "%Y-%m-%d %H:%M:%S")
                rec.sale_order_delivery_date = datetime.strptime(listSalesOrder[0].create_date, "%Y-%m-%d %H:%M:%S") + timedelta(days=(rec.product_id.sale_delay - listSalesOrder[0].team_id.transit_days))
                rec.customer = listSalesOrder[0].partner_id.name
                rec.sales_team = listSalesOrder[0].team_id.abbreviation

                #if rec.production_planned_end is None:
                #    rec.production_planned_end = datetime.strptime(listSalesOrder[0].create_date, "%Y-%m-%d %H:%M:%S") - timedelta(days=(rec.product_id.produce_delay - listSalesOrder[0].team_id.transit_days))

                # Buscar la línea del pedido que corresponde al product
                for OrderLine in listSalesOrder[0].order_line:
                    if OrderLine.product_id.id == rec.product_id.id:
                        rec.comments = OrderLine.comments
                        rec.embroidery = OrderLine.embroidery
                        rec.sale_order_line_delivery_date = OrderLine.product_delivery_date
                        if (rec.sale_order_line_delivery_date):
                            rec.sale_calculated_production_date = datetime.strptime(OrderLine.product_delivery_date, "%Y-%m-%d") - timedelta(days=(listSalesOrder[0].team_id.transit_days))
                            rec.sale_calculated_production_date = sub_business_days(datetime.strptime(rec.sale_calculated_production_date, "%Y-%m-%d"))
                            # if rec.production_planned_end is None and rec.origin != 'STOCK':
                        if rec.origin.upper() != 'STOCK' and rec.production_planned_end == False:
                            rec.production_planned_end = OrderLine.product_delivery_date

        return

    @api.multi
    def _compute_production_planned_end(self):
        for rec in self:
            if rec.origin and not rec.production_planned_end:
                if rec.origin.upper() == 'STOCK' and rec.production_planned_end == False:
                    rec.production_planned_end = datetime.strptime(rec.create_date, "%Y-%m-%d %H:%M:%S") - timedelta(days=(rec.product_id.produce_delay))
        return

    @api.depends('qty_produced')
    @api.multi
    def _compute_pending_produce_qty(self):
        for rec in self:
            rec.pending_produce_qty = rec.product_qty - rec.qty_produced
        return

    # Fecha Entrega Operaciones
    product_default_code = fields.Char(
                    string='Product',
		    related='product_id.default_code', readonly=True,

                    help='Product Default Code')
    # Fecha Entrega Operaciones
    production_planned_end = fields.Date(
                    compute='_compute_production_planned_end',
                    string='Production Planned End', readonly=False,
                    help='Production Planned End', store=True)
    # Fecha Entrega Pedido
    sale_order_line_delivery_date = fields.Date(
                    string='Sale Line Delivery Date',
                    compute='_compute_sale_order_data', readonly=True,
                    help='Sale Line Delivery Date')
    # Fecha Producción Pedido
    sale_calculated_production_date = fields.Date(
                    string='Calculated Production Date',
                    compute='_compute_sale_order_data', readonly=True,
                    help='Calculated Production Date')
    capture_days = fields.Float(
                    string="Capture Days",
                    compute='_compute_sale_order_data', readonly=True,
                    help='Capture Days')
    sale_order_create_date = fields.Datetime(
                    string="Sale Order Create Date",
                    compute='_compute_sale_order_data', readonly=True,
                    help='Sale Order Create Date')
    sale_order_delivery_date = fields.Datetime(
                    string="Sale Order Delivery Date",
                    compute='_compute_sale_order_data', readonly=True,
                    help='Sale Order Delivery Date')
    customer = fields.Char(
                    string="Customer",
                    compute='_compute_sale_order_data', readonly=True,
                    help='Customer')
    comments = fields.Char(
                    string='Comments',
                    compute='_compute_sale_order_data', readonly=True,
                    help='Comments')
    embroidery = fields.Char(
                    string='Embroidery',
                    compute='_compute_sale_order_data', readonly=True,
                    help='Embroidery')
    product_family = fields.Many2one(
                    string='Product Family', readonly=True,
                    related='product_id.categ_id.parent_id', store=True)
    # Mostrar qty_produced
    pending_produce_qty = fields.Float(
                    string='Pending Qty',
                    compute='_compute_pending_produce_qty', readonly=True,
                    help='Pending Quantity to Produce', store=True)
    sales_team = fields.Char(
                    string='Sales Team',
                    compute='_compute_sale_order_data', readonly=True,
                    help='Sales Team')
