from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    custom_field = fields.Char(string='Custom Field')
    comment = fields.Char(string='Comment')
    def _get_new_picking_values(self):
        res = super(StockMove, self)._get_new_picking_values()
        res["custom_field"] = self.custom_field

        return res
    def _prepare_procurement_values(self):
        remark = "kdios"
        res = super(StockMove, self)._prepare_procurement_values()
        res['custom_field'] = self.custom_field
        res.update({'comment': remark})
        print("*" * 50, res)
        return res

    # def _action_confirm(self):
    #     res = super(StockMove, self)._action_confirm()
    #     res["custom_field"] = self.custom_field
    #     return res

    # @api.model
    # def create(self, vals):
    #     # Check if the custom field value is passed
    #     sale_order_custom_field = vals.get('sale_order_custom_field')
    #
    #     # If not passed, check in context (if passed from sale order)
    #     if not sale_order_custom_field:
    #         sale_order_custom_field = self._context.get('sale_order_custom_field', False)
    #
    #     if sale_order_custom_field:
    #         vals['sale_order_custom_field'] = sale_order_custom_field
    #
    #     return super(StockMove, self).create(vals)