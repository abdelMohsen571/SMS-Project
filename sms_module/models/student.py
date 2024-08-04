from odoo import fields, models,api
import json


class Student(models.Model):
    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "sms_module.student"
    _description = 'Student'

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    student_id=fields.Char('Student ID')
    name = fields.Char(string='Student Name', required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of birth", required=False, )
    contact_details = fields.Char(string="Contact Details", required=False, )
    address = fields.Char(string="Address", required=False, )
    guardian_details = fields.Char(string="Guardian Details", required=False, )
    student_level = fields.Integer(required=True)
    preferred_course_domin=fields.Image(compute='compute_course_domain')
    preferred_course_id = fields.Many2one(comodel_name="sms_module.course" ,)
    # endregion

    # region  Relational
    enrollments_ids = fields.One2many(comodel_name="sms_module.enrollment", inverse_name="student_id", string="Enrollments", required=False, )
    grades_ids = fields.One2many(comodel_name="sms_module.grade", inverse_name="student_id", string="Grades", required=False, )
    attendance_ids = fields.One2many(comodel_name="sms_module.attendance", inverse_name="student_id", string="Attendance", required=False, )
    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    def create(self, vals_list):
        vals_list['student_id'] = self.env['ir.sequence'].next_by_code('student')
        return super(Student, self).create(vals_list)
    # endregion


    @api.onchange('student_level')
    def compute_course_domain(self):
        for rec in self:
            if rec.student_level == 0:
               rec.preferred_course_domin=[]

            else:
                rec.preferred_course_domin=[('course_level', '=', self.student_level)]




