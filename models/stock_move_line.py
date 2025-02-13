# from odoo import models, fields, api
#
# class StockMoveLine(models.Model):
#     _inherit = 'stock.move.line'
#
#     custom_field = fields.Char(string="Custom Field")
#
#     @api.model
#     def create(self, values):
#         if 'move_id' in values:
#             move_id = values['move_id']
#             move_line = self.env['stock.move'].search([('id', '=', move_id)], limit=1)
#             if move_line:
#                 values['custom_field'] = move_line.custom_field
#         return super(StockMoveLine, self).create(values)
