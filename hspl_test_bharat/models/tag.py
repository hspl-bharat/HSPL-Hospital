from odoo import api, fields, models

class RankingTag(models.Model):
    _name ='ranking.tag'
    _description = 'Ranking Tags'

    name = fields.Char('Name', required=True, tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    color = fields.Text(string='color')
    sequence = fields.Integer(string='Sequence')
