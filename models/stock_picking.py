from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    custom_field = fields.Char(string="Custom Field")
    comment = fields.Char(string='Comment')
