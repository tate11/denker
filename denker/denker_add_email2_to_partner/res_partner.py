
# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date


class ResPartner(models.Model):
    _inherit = "res.partner"

    email2 = fields.Char('Email2', help='Correo electrónico para enviar los estados de cuenta')
