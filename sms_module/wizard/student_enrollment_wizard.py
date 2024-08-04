from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentEnrollment(models.TransientModel):
    # region ---------------------- TODO[IMP]: Private Attributes --------------------------------

    _name = 'sms_module.student.enrollment.wizard'
    _description = 'Student Enrollment'
    # endregion

    # region ---------------------- TODO[IMP]:Default Methods ------------------------------------
    # endregion
    # region ---------------------- TODO[IMP]: Fields Declaration ---------------------------------

    # region  Basic
    student_ids = fields.Many2many('sms_module.student', required=True, string='Student')
    course_id = fields.Many2one('sms_module.course', required=True, string='Course')
    # endregion

    # region  Special
    # endregion

    # region  Relational
    # endregion

    # region  Computed
    # endregion

    # endregion


    # region ---------------------- TODO[IMP]: Compute methods ------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Constrains and Onchanges ---------------------------
    # endregion

    # region ---------------------- TODO[IMP]: CRUD Methods -------------------------------------
    # endregion

    # region ---------------------- TODO[IMP]: Action Methods -------------------------------------
    def action_enroll_student(self):
        enrollments=[]
        for student in self.student_ids:
            enrollments.append({
                'enrollment_date':fields.Date.today(),
                'student_id':student.id,
                'course_id':self.course_id.id
            })
        self.env['sms_module.enrollment'].create(enrollments)

    # endregion

    # region ---------------------- TODO[IMP]: Business Methods -------------------------------------
    # endregion
