# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models


class sale_order_line_comments(models.Model):
    _inherit = "sale.order.line"

    comments = fields.Char('Comments')
    embroidery = fields.Char('Embroidery')
