from odoo import api, fields, models, _
from odoo.exceptions import ValidationError



class Master(models.Model):
    _name = 'master.data'
    _description = 'Master Data'

    name = fields.Char('Name', required=True, tracking=True)
    ranking = fields.Integer('Ranking')
    tag_ids = fields.Many2many('ranking.tag', string='Tags')
    display_name = fields.Char('Display Name')


    _sql_constraints = [
        ('ranking_uniq', 'unique (ranking)', "Rank already exists !"),
    ]

    @api.onchange('ranking')
    def _check_max_record(self):
        if self.ranking > 9:
            raise ValidationError(_("Cannot enter more than 10 record "))


    def name_get(self):
        candiate_lst = []
        for rec in self:
            name = rec.name + '  ' + '[' + rec.ranking + ']'
            candiate_lst.append((rec.id, name))
        return candiate_lst