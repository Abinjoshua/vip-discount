# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    vip_discount = fields.Float(string="Vip Discount")
    res_value = fields.Boolean(string="Res Value", compute="_compute_res_value")
    min_quantity = fields.Integer(string="Minimum Quantity")

    @api.depends('partner_id', 'vip_discount')
    def _compute_res_value(self):
        vip_value = self.env['ir.config_parameter'].sudo().get_param('vip_discount.is_vip')
        if vip_value and self.partner_id.is_vip:
            self.res_value = True
            dis = self.order_line.filtered(
                lambda x: x.product_uom_qty >= self.min_quantity
            )
            dis.write({'discount': self.vip_discount})
        else:
            self.res_value = False
