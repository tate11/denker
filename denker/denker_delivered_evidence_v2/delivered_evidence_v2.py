
# -*- coding: utf-8 -*-
import openerp
import time
from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
from odoo import api, fields, models, tools
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class DeliveredEvidence(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def _create_backorder(self, backorder_moves=[]):
        """ Move all non-done lines into a new backorder picking. If the key 'do_only_split' is given in the context, then move all lines not in context.get('split', []) instead of all non-done lines.
        """
        # TDE note: o2o conversion, todo multi
        backorders = self.env['stock.picking']
        for picking in self:
            backorder_moves = backorder_moves or picking.move_lines
            if self._context.get('do_only_split'):
                not_done_bo_moves = backorder_moves.filtered(lambda move: move.id not in self._context.get('split', []))
            else:
                not_done_bo_moves = backorder_moves.filtered(lambda move: move.state not in ('done', 'cancel'))
            if not not_done_bo_moves:
                continue
            backorder_picking = picking.copy({
                'name': '/',
                'move_lines': [],
                'pack_operation_ids': [],
                'backorder_id': picking.id,
                'image_medium': None
            })
            picking.message_post(body=_("Back order <em>%s</em> <b>created</b>.") % (backorder_picking.name))
            not_done_bo_moves.write({'picking_id': backorder_picking.id})
            if not picking.date_done:
                picking.write({'date_done': time.strftime(DEFAULT_SERVER_DATETIME_FORMAT)})
            backorder_picking.action_confirm()
            backorder_picking.action_assign()
            backorders |= backorder_picking
        return backorders

    @api.multi
    def do_new_transfer(self):
        if (self.picking_type_id.code == 'outgoing' or self.picking_type_id.code == 'internal') and self.pack_operation_ids:
            for operation in self.pack_operation_ids:
                if operation.qty_done > operation.product_qty:
                    raise ValidationError(_('No se puede entregar más de lo que está establecido'))
        # if not self.image_medium and (self.location_dest_id.id == 9 or self.location_dest_bool):
            if not self.image_medium and (self.location_dest_id.id == 9):
            raise ValidationError(_('Please, first attach an image as delivered evidence to continue'))
        return super(DeliveredEvidence,self).do_new_transfer()

    @api.multi
    def _get_location_dest_bool(self):
        for record in self:
            record.location_dest_bool = False
            location = record.location_dest_id.name
            location = location.replace("á", "a")
            location = location.lower()
            if location.find("transito") != -1:
                record.location_dest_bool = True
            print('################################## LOCATION DEST: '+location)
        return

    location_dest_bool = fields.Boolean("Location Dest Bool", compute="_get_location_dest_bool", store=False)
