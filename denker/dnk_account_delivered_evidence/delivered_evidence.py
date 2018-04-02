
# -*- coding: utf-8 -*-
import openerp
from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
from odoo import api, fields, models, tools


class DeliveredEvidence(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def _get_image(self):
        return dict((p.id, tools.image_get_resized_images(p.image)) for p in self)

    @api.one
    def _set_image(self):
        for record in self:
            if record.image_medium == record.image: continue
            self.image = tools.image_resize_image_big(self.image_medium)
            self.image_medium = self.image
        return

    image = fields.Binary("Image",
                     help="This field holds the image for delivery evidence", store=False)
    image_medium = fields.Binary(string="Delivery Evidence:", store=True, inverse="_set_image",
                            help="Medium-sized image of this field. It is automatically " \
                                 "resized, with aspect ratio preserved.")
