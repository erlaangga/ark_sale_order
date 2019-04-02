from odoo import models, fields, api


class Sale(models.Model):
    _inherit = "sale.order"
    
    
    uniq_code = fields.Char("Unique Code") #, compute="_compute_uniq_code", store=True)#related="partner_id.uniq_code")
    
    @api.onchange('partner_id')
    def onchange_partner(self):
        if self.partner_id:
            self.uniq_code = self.partner_id.uniq_code
    
  # kita dapat menggunakan salah api.multi atau depends untuk field compute
  # 
  #   @api.multi
  #   @api.depends('partner_id')
  #   def _compute_uniq_code(self):
  #       if self.partner_id:
  #           self.uniq_code = self.partner_id.uniq_code
            
    @api.multi
    def action_invoice_create(self, grouped=False, final=False):
        res = super(Sale, self). \
                action_invoice_create(grouped=grouped, final=final)
        invoice_id = self.env['account.invoice']\
                         .browse(res)
        invoice_id.uniq_code = self.uniq_code
        # statement di atas sama dengan di bawah
        # invoice_id.write({'uniq_code': self.uniq_code}) # sama dengan yang di atas
        return res