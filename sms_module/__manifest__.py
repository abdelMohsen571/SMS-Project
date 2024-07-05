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
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml'
    ],
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'application': False,
    'installable': True,
    'license': 'LGPL-3',
}
