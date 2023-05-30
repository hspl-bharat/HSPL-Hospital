from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order Inherit'

    is_member = fields.Boolean('is a member', related='partner_id.is_a_member')
    active = fields.Boolean('Active', default=True, tracking=True)


    @api.constrains('date_order')
    def _check_date_order(self):
        for rec in self:
            if rec.date_order and rec.date_order.date() < fields.date.today():
                raise ValidationError(_("The entered date of quatation is not accepted"))

    @api.constrains('validity_date')
    def _check_expiry_date(self):
        for rec in self:
            if rec.validity_date and (rec.validity_date - rec.date_order.date()).days <= 5 :
                raise ValidationError(_("Expiry Date must be atleast greater than 5 days"))

    @api.model_create_multi
    def create(self, vals_list):
        res = super(SaleOrderInherit, self).create(vals_list)
        if res.client_order_ref:
            var = res.client_order_ref
            sema = 1
            nl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            i = 0
            var2 = str()
            while i <= len(var):
                while sema == 1:
                    if var[i] not in nl:
                        var2 += var[i]
                        i += 1
                        if i == len(var):
                            sema = 3
                    else:
                        var2 += '-'
                        sema = 0
                while sema == 0:
                    if var[i] in nl:
                        var2 += var[i]
                        i += 1
                        if i == len(var):
                            sema = 3
                    else:
                        var2 += '-'
                        sema = 1
                if i == len(var):
                    break
            res.client_order_ref = var2
        return res

