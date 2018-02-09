# -*- coding: utf-8 -*-
from odoo import models, fields, api


class account_invoice_to_stock_piking(models.Model):
    _inherit = ['stock.picking']

    # Obtengo el nombre del grupo, para filtrar en el domain del XML
    @api.multi
    def _compute_origin(self):
        for rec in self:
            M_groups = self.env['procurement.group']
            group_name = M_groups.search([('id', '=', rec.group_id.id)]).name
            if group_name:
                rec.group_name = group_name
        return
    # group_name no se muestra en el XML, sólo lo utilizo para que filtre sólo las facturas
    # que están relacionadas a ese Sale Order.
    group_name = fields.Char('Group', compute='_compute_origin')
