from odoo import fields, models


class Student(models.Model):
    _name = "sms.student"
    _description = 'student'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_id=fields.Char('Student ID')
    name = fields.Char(string='Student Name', required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of birth", required=False, )
    contact_details = fields.Char(string="Contact Details", required=False, )
    address = fields.Char(string="Address", required=False, )
    guardian_details = fields.Char(string="Address", required=False, )
    enrollments_ids = fields.One2many(comodel_name="sms.enrollment", inverse_name="student_id", string="Enrollments", required=False, )
    grades_ids = fields.One2many(comodel_name="sms.grade", inverse_name="student_id", string="Grades", required=False, )
    attendance_ids = fields.One2many(comodel_name="sms.attendance", inverse_name="student_id", string="Attendance", required=False, )

    def create(self, vals_list):
        vals_list['student_id'] = self.env['ir.sequence'].next_by_code('student')
        return super(Student, self).create(vals_list)



