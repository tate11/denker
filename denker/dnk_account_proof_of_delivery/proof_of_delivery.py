
# -*- coding: utf-8 -*-
import openerp
from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
from odoo import api, fields, models, tools
from PIL import Image
from PIL import ImageEnhance
from random import randrange
from io import BytesIO
import cStringIO
import base64



class ProofOfDelivered(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def _get_image(self):
        return dict((p.id, tools.image_get_resized_images(p.img_tmp_proof_of_delivery)) for p in self)

    @api.one
    def _set_image(self):
        for record in self:
            if record.img_proof_of_delivery == record.img_tmp_proof_of_delivery: continue
            self.img_tmp_proof_of_delivery = tools.image_resize_image_big(self.img_proof_of_delivery)
            # self.image_medium = Image.open(BytesIO(self.image_medium))
            #print "#######################_______#################################"
            #print self.image
            #self.image.rotate(90, Image.BILINEAR, expand=True)
            # self.image = Image.open(base64.dencodestring(self.image)).rotate(90, expand=not, resample=Image.BILINEAR).save(self.image)
            # self.image = cStringIO.StringIO(self.image.decode('base64'))
            # self.image = base64.encodestring(self.image)
            self.img_proof_of_delivery = self.img_tmp_proof_of_delivery
        return

    img_tmp_proof_of_delivery = fields.Binary("Image",
                     help="This field holds the image for proof of delivery", store=False)
    img_proof_of_delivery = fields.Binary(string="Proof Of Delivery:", store=True, inverse="_set_image",
                            help="Medium-sized image of this field. It is automatically " \
                                 "resized, with aspect ratio preserved.")
