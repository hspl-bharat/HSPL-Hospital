from odoo import models, fields, api


class Employee(models.Model):
    _name = 'employee'
    # _inherit = 'noteable'
    _description = 'employee'


    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    department_id = fields.Many2one('department', string='Department')

    # employee = self.env['employee'].browse(employee_id)
    # employee.add_note('Employee hired on 01-01-2022')


class Department(models.Model):
    _name = 'department'
    # _inherit = 'noteable'
    _description = 'department'


    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    employee_ids = fields.One2many('employee', 'department_id', string='Employees')

