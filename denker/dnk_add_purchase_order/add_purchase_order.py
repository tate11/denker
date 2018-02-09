
# -*- coding: utf-8 -*-
import openerp
from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
from odoo import api, fields, models, tools
import sys


class CustomPurchaseOrder(models.Model):
    _inherit = ['sale.order']

    @api.multi
    def action_confirm(self):
        zero_price = [x.product_id.name
                      for x in self.order_line if not x.price_unit]
        if zero_price:
            message = _("Please specify unit price for "
                        "the following products:") + '\n'
            message += '\n'.join(map(str, zero_price))
            raise Warning(message.rstrip())
        if not self.customer_purchase_order_file and self.customer_purchase_order_bool:
            raise ValidationError(_("Please, first attach the customer purchase order to continue"))
        return super(CustomPurchaseOrder, self).action_confirm()

    @api.multi
    @api.depends('partner_id.customer_purchase_order_bool')
    def get_customer_purchase_order_bool(self):
        ResPartner = self.env['res.partner']
        for rec in self:
            if rec.partner_id.id:
                resarray = ResPartner.search([('id','=',rec.partner_id.id)])
                for res in resarray:
                    rec.customer_purchase_order_bool = res.customer_purchase_order_bool
        return

    @api.one
    @api.constrains('filename')
    def _check_filename(self):
        if self.customer_purchase_order_file:
            if not self.filename:
                raise ValidationError(_("There is no file"))
            else:
                filesize = int (sys.getsizeof(self.customer_purchase_order_file)*0.74028)
                nombre = self.filename.split('.')
                ext = nombre[len(nombre)-1]
                if ext.lower() != 'pdf':
                    raise ValidationError(_("The file must be a PDF file"))
                if filesize > 1048576:
                    raise ValidationError(_("The PDF exceeds the maximun size (1MB)"))
        return

    filename = fields.Char()
    customer_purchase_order_file = fields.Binary("Purchase Order Document", attachment=True, store=True)
    customer_purchase_order_bool = fields.Boolean("Purchase Order Boolean", compute="get_customer_purchase_order_bool", default=True, store=True)
