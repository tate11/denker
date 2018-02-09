# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from lxml import etree


class CRMLead(models.Model):
    _inherit = "crm.lead"

    family_id = fields.Many2one('product.category', 'Family', required=False)
