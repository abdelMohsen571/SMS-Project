from odoo import fields, models


class StudentAttendance(models.Model):
    _name = "sms.attendance"
    _description = 'Attendance'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    date = fields.Date(string="Date", required=False, )
    student_id = fields.Many2one(comodel_name="sms.student", string="Student", required=False, )
    course_id = fields.Many2one(comodel_name="sms.course", string="Course", required=False, )
