from odoo import api, fields, models, tools
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, timedelta, date
import pytz
from openerp.osv import orm


class InvoiceUndelivered(models.Model):
    _name = "denker.invoice.undelivered.orders"
    _auto = False
    _order = "sale_order asc"

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'denker_invoice_undelivered_orders')
        self._cr.execute("""
            CREATE VIEW denker_invoice_undelivered_orders AS (
                SELECT
                    row_number() over (order by SO.id) AS id,
                    SO.name AS sale_order,
                    AI.invoices AS invoices, AI.last_invoice_date, SO.date_order::date AS date_order,
                    PCP.name AS product_family, SOL.name AS sol_product_name,
                    SOL.state AS sale_order_line_state,
                    SOL.product_uom_qty AS order_line_qty, SOL.qty_invoiced, SOL.qty_delivered,
                    SOL.price_reduce AS product_price,
                    CUR.name AS currency_name,
                    SOL.company_id AS company_id, C.name AS company_name,
                    SO.user_id, RP.name AS user_name,
                    SO.team_id, TEAM.name AS team_name
                    FROM sale_order SO
                    LEFT JOIN sale_order_line SOL ON  SO.id = SOL.order_id
                    INNER JOIN
                        (SELECT origin, string_agg(number, ' | ') AS invoices, MAX(date_invoice) AS last_invoice_date
                            FROM account_invoice
                            WHERE type IN ('out_invoice') AND state IN ('paid', 'open') GROUP BY origin)
                    AS AI ON AI.origin = SO.name
                    INNER JOIN product_product PP ON PP.id = SOL.product_id
                    INNER JOIN product_template PT ON PT.id = PP.product_tmpl_id
                    INNER JOIN product_category PC ON PT.categ_id =  PC.id
                    INNER JOIN product_category PCP ON PCP.id = PC.parent_id
                    INNER JOIN product_pricelist PL ON PL.id = SO.pricelist_id
                    INNER JOIN res_currency CUR ON CUR.id = PL.currency_id
                    INNER JOIN res_company C ON C.id = SOL.company_id
                    LEFT JOIN res_users U ON U.id = SO.user_id
                    LEFT JOIN res_partner RP ON RP.id = U.partner_id
                    LEFT JOIN crm_team TEAM ON TEAM.id = SO.team_id
                    WHERE SOL.qty_invoiced  <> SOL.qty_delivered
                    AND SO.state NOT IN ('cancel','done')
            )""")
    sale_order = fields.Char("SO", readonly=True)
    date_order = fields.Date("Date Order", readonly=True)
    invoices = fields.Char("Invoices", readonly=True)
    last_invoice_date = fields.Date("Last Invoice Date", readonly=True)
    product_family = fields.Char("Product Family", readonly=True)
    order_line_qty = fields.Integer("To Invoice", readonly=True)
    qty_invoiced = fields.Integer("Invoiced", readonly=True)
    qty_delivered = fields.Integer("Delivered", readonly=True)
    product_price = fields.Float("Product Price", readonly=True)
    sol_product_name = fields.Char("Product", readonly=True)
    currency_name = fields.Char("Currency", readonly=True)
    company_id = fields.Char("Company Id", readonly=True)
    company_name = fields.Char("Company", readonly=True)
    user_id = fields.Many2one('res.users', string='User Id', readonly=True)
    user_name = fields.Char("Salesperson", readonly=True)
    team_id = fields.Many2one('crm.team', string='Sales Team', readonly=True)
    team_name = fields.Char("Sales Team", readonly=True)
