
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
import pytz


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def _get_sale_order_id(self):
        SaleOrder = self.env['sale.order']
        for rec in self:
            group_id = rec.group_id.id and rec.group_id.id or 0
            # stockpicking_array = StockPicking.search([('group_id', '=', self.procurement_group_id.id)])
            # stockpicking_array = self.env['stock.picking'].search([('group_id', '=', self.procurement_group_id.id)]).id
            rec.saleorder_id = SaleOrder.search([('procurement_group_id.id', '=', group_id)]).id
            # print('############################### Sale Order Array: '+str(rec.saleorder_id))
        return

    saleorder_id = fields.Many2one('sale.oder', compute="_get_sale_order_id", store=True)
