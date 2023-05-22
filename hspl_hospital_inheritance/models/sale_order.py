from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'sale.order'


    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')

    def action_confirm(self):
        print('success...........')
        super(SaleOrder, self).action_confirm()