
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
import pytz


class SaleOrderLine(models.Model):
    _inherit = "sale.order"

    @api.multi
    @api.depends('stockpicking_id.state','stockpicking_id.location_dest_id','stockpicking_id.picking_type_id')
    def _get_delivery_status(self):
        print('############################ _GET_DELIVERY_STATUS')
        StockPicking = self.env['stock.picking']
        for rec in self:
            rec.delivery_status = 'Pending'
            rec.text_color = ''
            rec.text_bold = False
            rec.supply_filter = False
            procurement_id = rec.procurement_group_id.id
            stockpicking_array = StockPicking.search([('group_id', '=', procurement_id)], order='id desc')
            if stockpicking_array:
                temp_status = ''
                color = ''
                bold = False
                supply = False
                for stockp in stockpicking_array:
                    ubicacion_id = stockp.location_dest_id.id
                    albaran_id = stockp.picking_type_id.id
                    estado = stockp.state
                    name = stockp.name
                    total_partially = 0
                    # SUPPLY FILTERS
                    if name.find('SURTIDO') != -1 and estado == 'done':
                        supply = True
                    # UBICACION = CLIENTE; ALBARAN = ORDEN DE ENTREGA; ESTADO != DONE EN AL MENOS UNA LINEA
                    if ubicacion_id == 9 and albaran_id in (4, 10, 16, 22, 28):
                        if estado != 'done' and temp_status == '':
                            temp_status = 'Pending'
                            # color = 'gray'; NO ES NECESARIO YA QUE EL TEXTO ORIGINAL ES COLOR GRIS
                            bold = True
                    # UBICACION = SALIDA; ALBARAN = SURTIR; EN CUALQUIER LINEA
                    if ubicacion_id in (23, 30, 37, 44, 65, 71, 77, 83, 89, 115) and albaran_id in (3, 15, 34, 40, 46, 52, 58, 73):
                        if estado == 'done' and temp_status == '':
                            temp_status = 'Ready To Invoice'
                            color = 'blue'
                            bold = True
                        if estado == 'partially_available' and temp_status == '':
                            temp_status = 'Supply Partially To Customer'
                            total_partially += 1
                            color = 'black'
                            bold = True
                    # UBICACION = TRANSITO DE SUCURSAL; ALBARAN = ORDEN DE ENTREGA;
                    if ubicacion_id in (31, 59, 91, 92, 93, 94) and albaran_id in (4, 10, 16, 22, 28):
                        if estado == 'done' and temp_status == '':
                            temp_status = 'Transit Of Branch'
                            color = 'orange'
                            bold = True
                    # UBICACION = SALIDA DE SUCURSAL; ALBARAN = SURTIR
                    if ubicacion_id in (127, 132, 133, 134, 135) and albaran_id in (3, 15, 34, 40, 46, 52, 58, 73):
                        if estado == 'done' and temp_status == '':
                            temp_status = 'Send To Branch'
                        if (estado == 'assigned' or estado == 'partially_available') and (temp_status == ''):
                            temp_status = 'Supply Branch'
                # EN TODAS LAS LINEAS DEL PEDIDO TOTAL PARTIALLY
                if len(stockpicking_array) == total_partially:
                    color = 'green'
                rec.delivery_status = temp_status or 'Pending'
                rec.text_color = color
                rec.text_bold = bold
                rec.supply_filter = supply
                if rec.delivery_status != 'Pending':
                    print('Linea de pedido... Delivery Status: '+rec.delivery_status+', Text Color: '+rec.text_color+', Bold: '+str(rec.text_bold))
        return

    delivery_status = fields.Char('Delivery Status', compute='_get_delivery_status', store=True)
    text_color = fields.Char('Text Color', compute='_get_delivery_status', store=True)
    text_bold = fields.Boolean('Text Style', compute='_get_delivery_status', store=True)
    supply_filter = fields.Boolean('Supply Filter', compute='_get_delivery_status', store=True)
