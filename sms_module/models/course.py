from odoo import fields, models


class Course(models.Model):
    _name = "sms.course"
    _description = 'Course'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Student Name', required=True, tracking=True)
    description = fields.Text(string="Description", required=False, )
    syllabus = fields.Char(string="Syllabus", required=False, )
    duration = fields.Integer(string='Duration', required=False, )
    prerequisites = fields.Text(string="Prerequisites", required=False, )
    enrollments_ids = fields.One2many(comodel_name="sms.enrollment", inverse_name="course_id", string="Enrollments",
                                      required=False, )
    grades_ids = fields.One2many(comodel_name="sms.grade", inverse_name="course_id", string="Grades", required=False, )
    attendance_ids = fields.One2many(comodel_name="sms.attendance", inverse_name="course_id", string="Attendance",
                                     required=False, )




