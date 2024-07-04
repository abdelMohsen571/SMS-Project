from odoo import fields, models


class StudentEnrollment(models.Model):
    _name = "sms.enrollment"
    _description = 'enrollment'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    enrollment_date = fields.Date(string="Enrollment Date", required=False, )
    student_id = fields.Many2one(comodel_name="sms.student", string="Student", required=False, )
    course_id = fields.Many2one(comodel_name="sms.course", string="Course", required=False, )
