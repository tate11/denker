
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
import pytz


class SaleOrderCorrections(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_validate(self):
        for order in self:
            if order.order_corrections and order.state == 'fix':
                raise ValidationError(_("El pedido tiene correcciones por realizar, revise el campo 'Corregir En Pedido', \
                una vez hechas las correcciones solicitadas, por favor borre los elementos del campo."))
            if not order.order_line:
                raise ValidationError(_("No hay lineas de pedido capturadas."))
            order.state = 'validate'
        return True

    @api.multi
    def action_fix(self):
        for order in self:
            if not order.order_corrections:
                raise ValidationError(_("Para mover el pedido a 'Corregir Pedido' es necesario indicar los elementos a \
                corregir en el campo 'Corregir En Pedido'"))
            order.state = 'fix'
        return True
    def action_to_draft(self):
        for order in self:
            order.state = 'draft'
        return True

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
        current_userid = self.env.user.id
        OrderCorrectionsModel = self.env['dnk.sale.order.corrections.model']
        correcto = OrderCorrectionsModel.search([('id', '=', 1)])
        companys = [(1)] #07 Marzo 2018 - Las compañias que aplicarían sería Antiestática (1) y Empaques MPK (4)
        # 09 Marzo 2018 Siempre no va a aplicar para Empaques MPK
        for order in self:
            if current_userid == order.create_uid.id and order.company_id.id in companys:
                raise ValidationError(_("El pedido no puede ser Confirmado por el mismo usuario que lo genera"))
            order.state = 'sale'
            order.order_corrections = correcto
            order.confirmation_date = fields.Datetime.now()
            if self.env.context.get('send_email'):
                self.force_quotation_send()
            order.order_line._action_procurement_create()
        if self.env['ir.values'].get_default('sale.config.settings', 'auto_done_setting'):
            self.action_done()
        return True

    @api.onchange('customer_purchase_order_file')
    @api.depends('customer_purchase_order_file')
    def _get_client_order_ref(self):
        if self.filename:
            nombre = self.filename.lower().replace('.pdf', '')
            self.client_order_ref = nombre.upper()
        return

    @api.multi
    def _get_current_company(self):
        for order in self:
            self.current_company = self.env['res.company']._company_default_get('sale.order')
        return

    # CREA LOS NUEVOS ESTADOS 'to fix' Y 'validate' EN EL MODELO SALE ORDER
    current_company = fields.Integer(string='Current Company', compute='_get_current_company', store=False)
    #current_company = fields.Many2one('res.company', string='Company',
    #default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get('sale.order')))
    client_order_ref = fields.Char(string='Customer Reference', compute='_get_client_order_ref', copy=False, required=False, store=True)
    order_corrections = fields.Many2many(comodel_name='dnk.sale.order.corrections.model', relation='dnk_sale_order_correction_data', string='Corregir En Pedido')
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('fix', 'Fix Order'),
        ('validate', 'Validate Order'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')


class SaleOrderLineCorrections(models.Model):
    _inherit = "sale.order.line"

    # CREA LOS NUEVOS ESTADOS 'to fix' Y 'validate' EN EL MODELO SALE ORDER
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('fix', 'Fix Order'),
        ('validate', 'Validate Order'),
        ('sale', 'Sale Order'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], related='order_id.state', string='Order Status', readonly=True, copy=False, store=True, default='draft')
