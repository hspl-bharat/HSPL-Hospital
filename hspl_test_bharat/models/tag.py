from odoo import api, fields, models

class RankingTag(models.Model):
    _name ='ranking.tag'
    _description = 'Ranking Tags'

    name = fields.Char('Name')
    tag_color = fields.Boolean('Active')
    color = fields.Char(string='color')
    active = fields.Boolean('Active')
    master_id = fields.Many2one('master.data', string='Master Id')
