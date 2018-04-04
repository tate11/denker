# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dnk_sale_theoretical_cost_db(models.Model):

    _inherit = "product.template"
    theoretical_cost = fields.Float(String="Theoretical Cost", store=True)

class dnk_sale_theoretical_cost_product_db(models.Model):

    _inherit = "product.product"
    theoretical_cost = fields.Float(String="Theoretical Cost", store=True)
