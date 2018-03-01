# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dnk_sale_commercial_name(models.Model):
    _inherit = "sale.order"

    @api.multi
    @api.onchange('partner_id')
    def _compute_commercial_name(self):
         for rec in self:
                if rec.partner_id.id :
                    result_qry =   self._cr.execute("SELECT commercial_company_name FROM  res_partner WHERE id = %s LIMIT 1", (rec.partner_id.id,))
                    for comm_name in  self.env.cr.fetchall():
                        if comm_name:
                            rec.commercial_name = comm_name[0]


    commercial_name = fields.Char(String='Commercial Company Name', compute='_compute_commercial_name')
