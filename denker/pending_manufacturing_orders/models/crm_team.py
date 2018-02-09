# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
# import pytz


class crm_team_transit_days(models.Model):
    _inherit = "crm.team"

    @api.onchange('abbreviation')
    def _upper_abbreviation(self):
        if self.abbreviation:
            self.abbreviation = self.abbreviation.upper()

    abbreviation = fields.Char(
                    string='Abbreviation',
                    help='Abbreviation', size=2)

    transit_days = fields.Integer(
                    string='Transit Days',
                    help='Days elapsed when the package arrives at the branch',
                    default=3)
