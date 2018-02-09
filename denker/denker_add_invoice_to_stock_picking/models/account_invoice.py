# -*- coding: utf-8 -*-
from odoo import models, fields, api


class addto_account_invoice_tracking_reference(models.Model):
    _inherit = ['account.invoice']

    @api.multi
    def _compute_tracking_ref(self):
        print "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
        for rec in self:
            print rec
            print rec.id
            M_stock_picking = self.env['stock.picking']
            stock_picking = M_stock_picking.search([('invoice_id', '=', rec.id)])
            rec.carrier_tracking_ref = ""
            if stock_picking:
                for reg in stock_picking:
                    rec.carrier_tracking_ref += reg.carrier_id.name + '-' + reg.carrier_tracking_ref + ' <br>'
                print rec.carrier_tracking_ref
        return

    carrier_tracking_ref = fields.Html('Trackin Ref.', compute='_compute_tracking_ref')
