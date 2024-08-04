from odoo import fields, models


class Course(models.Model):
    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "sms_module.course"
    _description = 'Course'
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    name = fields.Char(string='Student Name', required=True, tracking=True)
    description = fields.Html(string="Description", required=False, )
    syllabus = fields.Char(string="Syllabus", required=False, )
    duration = fields.Integer(string='Duration', required=False, )
    prerequisites = fields.Text(string="Prerequisites", required=False, )
    course_level = fields.Integer(required=True)
    # endregion

    # region  Relational----------------TODO[IMP]: Relational Fields Declaration----------------------
    enrollments_ids = fields.One2many(comodel_name="sms_module.enrollment", inverse_name="course_id", string="Enrollments",
                                      required=False, )
    grades_ids = fields.One2many(comodel_name="sms_module.grade", inverse_name="course_id", string="Grades", required=False, )
    attendance_ids = fields.One2many(comodel_name="sms_module.attendance", inverse_name="course_id", string="Attendance",
                                     required=False, )
    # endregion




