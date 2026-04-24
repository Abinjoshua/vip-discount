# -*- coding: utf-8 -*-
{
    'name': "Vip Discount",
    'version': "1.0",
    'licence': "LGPL-3",
    'author': "Cybrosys",
    'website': "http://www.cybrosys.com",
    'sequence': 1,
    'application': True,
    'depends': ['sale_management','contacts'],
    'data': ['views/sale_order_view.xml',
             'views/res_partner_view.xml',
             'views/res_config_settings_views.xml'
           ],
    'auto_install': True,
}
