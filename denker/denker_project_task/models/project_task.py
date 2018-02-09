# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

# Prioridad, Atraso, Fecha Creación, Qué, Quién se Encarga, Quién Pidió, Para cuando, Evidencia, Fecha Real Entrega, Etapa
# Priority, Delay, Creation Date, Task Title, Assigned to, Requestor, Deadline, Evidence, Real End Date, Stage


class project_task(models.Model):
    _inherit = 'project.task'

    requestor = fields.Many2one('res.users', string='Requestor')
    evidence = fields.Char(string='Evidence')
    real_end_date = fields.Datetime(string='Real End Date', copy=False)
