# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dnk_account_payment_solution(models.Model):
    _name = "dnk.account.payment.solution"
    _rec_name = 'name'
    _order = 'sequence,name'
    name = fields.Char('Name')
    sequence = fields.Integer('Sequence')


class dnk_account_promise_of_payment(models.Model):
    _inherit = "account.invoice"
    promise_to_pay = fields.Date(string="Promise To Pay", help="Promise To Pay")
    payment_solution = fields.Many2many(
        comodel_name='dnk.account.payment.solution',
        relation='dnk_account_payment_solution_rel',
        string="Payment Solution",)
