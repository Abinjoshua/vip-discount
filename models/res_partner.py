# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_vip = fields.Boolean(string="Vip")
    vip_value = fields.Boolean(string="Vip Value",compute="_compute_vip_value")

    def _compute_vip_value(self):
        vip_value = self.env['ir.config_parameter'].sudo().get_param('vip_discount.is_vip')
        self.vip_value = vip_value

