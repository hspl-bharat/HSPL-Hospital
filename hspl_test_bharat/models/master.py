from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class MembershipLevel(models.Model):
    _name = 'master.data'
    _description = 'Master Data'

    name = fields.Char('Name', tracking=True)
    ranking = fields.Integer('Ranking')
    display_name = fields.Char('Display Name' ,store = True, compute = '_compute_display_name')
    # ,store = True, compute = '_compute_display_name'
    color_ids = fields.One2many('ranking.tag', 'master_id', string='Color')

    _sql_constraints = [
        ('ranking_unique', 'unique (ranking)', "Rank already exists !"),
    ]

    @api.onchange('ranking')
    def _check_max_record(self):
        if self.ranking > 9:
            raise ValidationError(_("Cannot enter more than 10 record "))

    @api.depends('color_ids','ranking')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = str(rec.ranking) +':'+ str(rec.color_ids.name)

