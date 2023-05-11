# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management Testing',
    'version': '1.0.0',
    'summary': 'Management of Patients',
    'sequence': 10,
    'description': """
Staff and Patients
Manage the staff for giving better services to patients with the help of our software""",
    'category': 'Management',
    'depends': ['mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'mail_templates/birthdays_wishes.xml',
        'data/ir_cron_for_scheduling.xml',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/male_patient.xml',
        'views/female_patient.xml',
        'views/appointment.xml',
        'views/tag_view.xml',
        'views/draft_view.xml',
        'views/settings_view.xml',
        'views/patient_template_view.xml',
        'reports/patient_report.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
