from odoo import models, fields, api


class Noteable(models.AbstractModel):
    _name = 'noteable'
    _description = 'noteable'


    notes = fields.Text(string='Notes')

    def add_note(self, note):
        self.notes += '\n' + note
