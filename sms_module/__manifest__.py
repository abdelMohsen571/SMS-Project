# -*- coding: utf-8 -*-radio
{
    'name': 'Student Management System',
    'category': '',
    'summary': ' Manage Student, Courses, Enrollment, Grade and Attendance ',
    'description': """
    """
    ,
    'author': 'Laplace Technologies',
    'website': 'https://laplace.com/',
    'depends': [
        'base','mail'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menuitems.xml',
        'views/student_views.xml',
        'views/course_views.xml',
        'views/enrollment_views.xml',
        'views/grade_views.xml',
        'views/attendance_views.xml',

    ],
    'external_dependencies': {  
        'python': [],
        'bin': [],
    },
    'application': False,
    'installable': True,
    'license': 'LGPL-3',
    'sequence':-9999
}
