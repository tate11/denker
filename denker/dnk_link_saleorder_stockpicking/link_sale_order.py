
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
import pytz


class SaleOrderLine(models.Model):
    _inherit = "sale.order"

    @api.multi
    def _get_stock_picking_id(self):
        StockPicking = self.env['stock.picking']
        for rec in self:
            group_id = rec.procurement_group_id.id and rec.procurement_group_id.id or 0
            # stockpicking_array = StockPicking.search([('group_id', '=', self.procurement_group_id.id)])
            rec.stockpicking_id = StockPicking.search([('group_id', '=', group_id)]).id
        return

    stockpicking_id = fields.One2many('stock.picking', 'saleorder_id', compute="_get_stock_picking_id", store=True)
