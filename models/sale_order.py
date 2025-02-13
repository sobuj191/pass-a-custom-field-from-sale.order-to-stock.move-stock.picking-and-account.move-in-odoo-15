# models/sale_order.py
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_field = fields.Char(string='Custom Field')

    # def action_confirm(self):
    #     super(SaleOrder, self).action_confirm()
    #     self.custom_field = self.custom_field
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['custom_field'] = self.custom_field
        print("*"*100, invoice_vals)
        return invoice_vals