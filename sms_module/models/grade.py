from odoo import fields, models


class StudentGrade(models.Model):
    _name = "sms.grade"
    _description = 'grade'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Grade', required=True, tracking=True)
    date = fields.Date(string="Date", required=False, )
    student_id = fields.Many2one(comodel_name="sms.student", string="Student", required=False, )
    course_id    = fields.Many2one(comodel_name="sms.course", string="Course", required=False, )
