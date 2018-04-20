
# -*- coding: utf-8 -*-
import openerp
from openerp import addons
from openerp import models, fields, api, _


class reinvoicingRel(models.Model):
    _inherit = "account.invoice"

    @api.multi
    @api.depends('journal_id')
    @api.onchange('journal_id')
    def _get_bool_reinvoincing_onchange(self):
        for rec in self:
            if self.journal_id and self.journal_id.name.find("REFACT") >= 0 :
                rec.reinvoicing = True
            else :
                rec.reinvoicing = False
                rec.reinvoicing_id = False


    reinvoicing = fields.Boolean('Re-invoicing?', compute='_get_bool_reinvoincing_onchange', store=True)
    rel_origin = fields.Char(related='reinvoicing_id.origin', readonly=False)
    reinvoicing_id = fields.Many2one('account.invoice', string='Re-Invoicing', ondelete='cascade')
    rel_proof_of_delivery = fields.Binary(related='reinvoicing_id.img_proof_of_delivery')
