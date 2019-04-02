from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    uniq_code = fields.Char("Unique Code", readonly=True)
    
    