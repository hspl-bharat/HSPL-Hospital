# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'HSPL Test Bharat',
    'version': '1.0.0',
    'summary': 'Test by HSPL',
    'sequence': 10,
    'description': """
                        Entry test by HSPL for fresher""",
    'category': 'Management',
    'depends': ['mail','product','base','sale','portal'],
    'data': [
        'security/ir.model.access.csv',
        'data/ranking_tag_data.xml',
        'data/ranking.tag.csv',
        'views/menu.xml',
        'views/candidates.xml',
        'views/tag_view.xml',
        'views/res_partner_inherit.xml',
        'views/sale_order_inherit.xml',
        'views/my_account_template.xml',
        'views/purchase_report_inherit.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
