# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Picking(models.Model):
    _inherit = "stock.picking"

    location_src_sequence = fields.Integer(
        'Sequence', help="Source Location Sequence", store=True,
        readonly=True, related='location_id.sequence')
