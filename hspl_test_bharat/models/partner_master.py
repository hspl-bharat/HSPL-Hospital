from odoo import api, fields, models, _



class PartnerMaster(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner Master Data'

    is_a_member = fields.Boolean('is a member')
    master_id = fields.Many2one('master.data', string='Master Id')