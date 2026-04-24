# -*- coding: utf-8 -*-
from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    is_vip = fields.Boolean(string="Vip",
                            config_parameter='vip_discount.is_vip')