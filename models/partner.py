from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"
    
    uniq_code = fields.Char("Unique Code")