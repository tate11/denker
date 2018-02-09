# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Maintainer: Cybrosys Technologies (<https://www.cybrosys.com>)
##############################################################################

from odoo import api, models, fields, _
from odoo.exceptions import UserError

from odoo.addons.mrp.models.mrp_production import MrpProduction as mp


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('planned', 'Planned'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string='State',
        copy=False, default='draft', track_visibility='onchange')

    @api.model
    def create(self, values):
        if not values.get('name', False) or values['name'] == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code('mrp.production.draft') or _('New')
        production = super(mp, self).create(values)
        return production

    @api.multi
    def unlink(self):
        if any(production.state not in ['draft', 'cancel'] for production in self):
            raise UserError(_('Cannot delete a manufacturing order not in draft or cancel state'))
        return super(MrpProduction, self).unlink()

    @api.multi
    def action_confirm(self):
        if self.picking_type_id:
            self.draft_name = self.name
            self.name = self.picking_type_id.sequence_id.next_by_id()
        if not self.procurement_group_id:
            self.procurement_group_id = self.env["procurement.group"].create({'name': self.name}).id
        self._generate_moves()
        self.state = 'confirmed'

    @api.onchange('bom_id')
    @api.multi
    def onchange_bom(self):
        for rec in self:
            rec.picking_type_id = rec.bom_id.picking_type_id.id
        return

    draft_name = fields.Char('Draft Name', readonly=True)

    _sql_constraints = [
        ('name_uniq', 'check (1 != 1)', 'Reference must be unique per Company!'),
        ('qty_positive', 'check (product_qty > 0)', 'The quantity to produce must be positive!'),
    ]
