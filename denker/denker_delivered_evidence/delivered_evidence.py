
# -*- coding: utf-8 -*-
import openerp
from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
from odoo import api, fields, models, tools


class DeliveredEvidence(models.Model):
    _inherit = "stock.picking"

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

    @api.multi
    def do_new_transfer(self):
        if (self.picking_type_id.code == 'outgoing' or self.picking_type_id.code == 'internal') and self.pack_operation_ids:
            for operation in self.pack_operation_ids:
                if operation.qty_done > operation.product_qty:
                    raise ValidationError(_('No se puede entregar más de lo que está establecido'))
        #if not self.image_medium and self.location_dest_id.id == 9:
        #    raise ValidationError(_('Please, first attach an image as delivered evidence to continue'))
        return super(DeliveredEvidence,self).do_new_transfer()

    image = fields.Binary("Image",
                     help="This field holds the image used as avatar for this student, limited to 1024x1024px", store=False)
    image_medium = fields.Binary(string="Evidencia de Entrega:", store=True, inverse="_set_image",
                            help="Medium-sized image of this contact. It is automatically " \
                                 "resized as a 128x128px image, with aspect ratio preserved. " \
                                 "Use this field in form views or some kanban views.")
