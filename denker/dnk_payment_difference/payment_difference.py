
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.addons.account.models.account_payment import MAP_INVOICE_TYPE_PAYMENT_SIGN
from odoo.addons.account.models.account_payment import MAP_INVOICE_TYPE_PARTNER_TYPE


class PaymentDifference(models.TransientModel):
    _inherit = "account.register.payments"

    @api.one
    @api.depends('invoice_ids', 'amount', 'payment_date', 'currency_id')
    def _compute_payment_difference(self):
        context = dict(self._context or {})
        active_model = context.get('active_model')
        active_ids = context.get('active_ids')
        print('######################## COMPUTE PAYMENT DIFFERENCE DNK')
        self.invoice_ids = self.env[active_model].browse(active_ids)
        print(self.invoice_ids)
        if len(self.invoice_ids) == 0:
            print('############################## COMPUTE PAYMENT DIFFERENCE, if dnk')
            return
        print('############################## COMPUTE PAYMENT DIFFERENCE, continue if dnk')
        if self.invoice_ids[0].type in ['in_invoice', 'out_refund']:
            self.payment_difference = self.amount - self._compute_total_invoices_amount()
        else:
            self.payment_difference = self._compute_total_invoices_amount() - self.amount


    def create_payment(self):
        print('####################################### CREATE_PAYMENT VARIAS FACTURAS DNK')
        if not self.multiple_supplier:
            print('####################################### CREATE_PAYMENT VARIAS FACTURAS, if dnk')
            print('Payment Difference Handling DNK: '+str(self.payment_difference_handling))
            return super(PaymentDifference, self).create_payment()
        for partner in self.partner_ids:
            print('####################################### CREATE_PAYMENT VARIAS FACTURAS, for dnk')
            context = dict(self._context)
            payment = self.env['account.payment'].with_context(context).create(
                self.get_payment_vals_multi_vendor(partner.id))
            payment.post()
        return {'type': 'ir.actions.act_window_close'}

    def get_payment_vals(self):
        """ Hook for extension """
        print('################################ GET PAYMENT VALS DNK')
        print('################################ WRITEOFF DNK: '+str(self.writeoff_account_id.name))
        return {
            'journal_id': self.journal_id.id,
            'payment_method_id': self.payment_method_id.id,
            'payment_date': self.payment_date,
            'communication': self.communication,
            'invoice_ids': [(4, inv.id, None) for inv in self._get_invoices()],
            'payment_type': self.payment_type,
            'amount': self.amount,
            'currency_id': self.currency_id.id,
            'partner_id': self.partner_id.id,
            'partner_type': self.partner_type,
            'payment_difference_handling': self.payment_difference_handling,
            'writeoff_account_id': self.writeoff_account_id.id,
        }

    writeoff_account_id = fields.Many2one('account.account', string="Difference Account", domain=[('deprecated', '=', False)], copy=False)
    payment_difference = fields.Monetary(compute='_compute_payment_difference', readonly=True)
    payment_difference_handling = fields.Selection([('open', 'Keep open'), ('reconcile', 'Mark invoices as fully paid')], string="Payment Difference", store=True)
    multiple_supplier = fields.Boolean('Multiple Vendors')
    partner_ids = fields.Many2many('res.partner', 'partner_payment_rel', 'partner_id', 'payment_id', 'Partner')
    invoice_ids = fields.Many2many('account.invoice', 'account_invoice_payment_rel', 'payment_id', 'invoice_id', string="Invoices", copy=False, readonly=True)
