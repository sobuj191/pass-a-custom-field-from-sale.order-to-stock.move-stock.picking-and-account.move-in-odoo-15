from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    custom_field = fields.Char(string="Custom Field")
    comment = fields.Char(string='Comment')


    def action_confirm(self):
        res = super(StockPicking, self).action_confirm()
        if self.sale_id:
            for move in self.move_ids_without_package:
                move.custom_field = self.sale_id.custom_field
        return res