# models/sale_order.py
from odoo import models, fields, api
from odoo.tools import float_compare


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    custom_field = fields.Char(string='Custom Field')

    comment = fields.Char(string='Comment')

    # def _prepare_procurement_values(self, group_id=False):
    #     remark = "kdios"
    #     res = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
    #     res['custom_field'] = self.order_id.custom_field
    #     res.update({'comment':remark})
    #     print("*"*50,res)
    #     return res
    #
    #
    # def _action_launch_stock_rule(self, previous_product_uom_qty=False):
    #     """
    #     Launch procurement group run method with required/custom fields genrated by a
    #     sale order line. procurement group will launch '_run_pull', '_run_buy' or '_run_manufacture'
    #     depending on the sale order line product rule.
    #     """
    #     precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
    #     procurements = []
    #     for line in self:
    #         if line.state != 'sale' or not line.product_id.type in ('consu', 'product'):
    #             continue
    #         qty = line._get_qty_procurement(previous_product_uom_qty)
    #         if float_compare(qty, line.product_uom_qty, precision_digits=precision) >= 0:
    #             continue
    #
    #         group_id = line._get_procurement_group()
    #         if not group_id:
    #             group_id = self.env['procurement.group'].create(line._prepare_procurement_group_vals())
    #             line.order_id.procurement_group_id = group_id
    #         else:
    #             # In case the procurement group is already created and the order was
    #             # cancelled, we need to update certain values of the group.
    #             updated_vals = {}
    #             if group_id.partner_id != line.order_id.partner_shipping_id:
    #                 updated_vals.update({'partner_id': line.order_id.partner_shipping_id.id})
    #             if group_id.move_type != line.order_id.picking_policy:
    #                 updated_vals.update({'move_type': line.order_id.picking_policy})
    #             if updated_vals:
    #                 group_id.write(updated_vals)
    #
    #         values = line._prepare_procurement_values(group_id=group_id)
    #         values.update({'custom_field': line.order_id.custom_field})
    #         product_qty = line.product_uom_qty - qty
    #
    #         line_uom = line.product_uom
    #         quant_uom = line.product_id.uom_id
    #         product_qty, procurement_uom = line_uom._adjust_uom_quantities(product_qty, quant_uom)
    #         procurements.append(self.env['procurement.group'].Procurement(
    #             line.product_id, product_qty, procurement_uom,
    #             line.order_id.partner_shipping_id.property_stock_customer,
    #             line.name, line.order_id.name, line.order_id.company_id, values))
    #     if procurements:
    #         self.env['procurement.group'].run(procurements)
    #     return True