from odoo import api, fields, models, _



class PartnerMaster(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner Master Data'

    member = fields.Selection([('Y', 'is a member'), ('N', 'not a member')], string='Member')
    candidate_id = fields.Many2many('master.data', string='Candidate Id')