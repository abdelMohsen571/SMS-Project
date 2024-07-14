from odoo import fields, models


class StudentEnrollment(models.Model):
    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------
    _name = "sms_module.enrollment"
    _description = 'Enrollment'
    # endregion

    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------
    name = fields.Char(string='Name', required=True, tracking=True)
    enrollment_date = fields.Date(string="Enrollment Date", required=False, )
    # endregion

    # region  Relational----------------TODO[IMP]: Relational Fields Declaration----------------------
    student_id = fields.Many2one(comodel_name="sms_module.student", string="Student", required=False, )
    course_id = fields.Many2one(comodel_name="sms_module.course", string="Course", required=False, )
    # endregion


