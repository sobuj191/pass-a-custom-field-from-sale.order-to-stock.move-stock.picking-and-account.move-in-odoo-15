from odoo import models, fields


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'
    custom_field = fields.Char(string='Custom Field')


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_custom_move_fields(self):
        fields = super(StockRule, self)._get_custom_move_fields()
        fields += ['custom_field']
        return fields

    def _push_prepare_move_copy_values(self, move_to_copy, new_date):
        new_move_vals = super(StockRule, self)._push_prepare_move_copy_values(
            move_to_copy, new_date)
        new_move_vals.update({
            'custom_field': move_to_copy.custom_field
        })
        return new_move_vals

    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id,
                         name, origin, values, bom):
        new_vals = super(StockRule, self)._prepare_mo_vals(
            product_id, product_qty, product_uom, location_id, name, origin, values, bom)
        new_vals.update({
            'custom_field': values.get('custom_field', '')
        })
        return new_vals
