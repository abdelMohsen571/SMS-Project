import json
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request


class StudentApi(http.Controller):
    # this controller for create student by api (provide api to create student

    @http.route(['/v1/student'], type="http", auth="none", methods=["POST"], csrf=False)
    def example(self):

        args = request.httprequest.data.decode()  # reuquest data from body
        vals = json.loads(args)  # convert data thar return from json  to dictionary to use it while creation
        if not vals.get('name'):  # check name is send in body if not it will response error
            return request.make_json_response({
                'error': 'name is required'
            }, status=400)
        try:
            res = request.env['sms_module.student'].sudo().create(
                vals)  # create student with vals that get from request
            print(res)
            if res:
                return request.make_json_response(
                    {  # response for user to identify them data is created or error happen
                        "message": "student created succisfuly",
                        'id': res.id,
                        'name': res.name}, status=201)
        except Exception as error:
            return request.make_json_response(
                {
                    'message': error
                }, status=400
            )

    @http.route(['/v1/student/json'], type="json", auth="none", methods=["POST"], csrf=False)
    def example2(self):
        # reuquest data from body
        args = request.httprequest.data.decode()
        print("json===>", type(args))
        # convert data thar return from json  to dictionary to use it while creation
        vals = json.loads(args)
        print("json====>", type(vals))
        res = request.env['sms_module.student'].sudo().create(vals)
        print(res)
        # return response to user
        if res:
            return [{
                'message': 'object with json is created'
            }]

    @http.route(['/v1/student/<int:student_id>'], type="http", auth="none", methods=["PUT"], csrf=False)
    def update_student(self, student_id):
        student_id = request.env['sms_module.student'].sudo().search(
            [('id', '=', student_id)])  # search if user found else raise error
        if not student_id:
            return request.make_json_response(
                {
                    'error': "Student not found",
                }, status=400
            )
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        try:
            student_id.write(vals)  # Update user with vals which send in request
            return request.make_json_response({
                "message": "student Updated successfully",
                'id': student_id.id,
                'name': student_id.name}, status=201)
        except Exception as error:
            return request.make_json_response(
                {
                    'message': error
                }, status=400
            )

    @http.route(['/v1/student/<int:student_id>'], type="http", auth="none", methods=["GET"], csrf=False)
    def get_student(self, student_id):
        student_id = request.env['sms_module.student'].sudo().search([('id', '=', student_id)])
        try:
            if not student_id:
                return request.make_json_response(
                    {
                        'error': "Student not found",
                    }, status=400
                )
            return request.make_json_response({
                'id': student_id.id,
                'name': student_id.name,
                'student_level': student_id.student_level,
                'date_of_birth': student_id.date_of_birth,
                'contact_details': student_id.contact_details,

            }, status=200)
        except Exception as error:
            return request.make_json_response(
                {
                    'message': error
                }, status=400
            )


    @http.route(['/v1/students'], type="http", auth="none", methods=["GET"], csrf=False)
    def get_students_list(self):
        try:
            # import parse_query_string
            params=parse_qs(request.httprequest.query_string.decode('utf-8'))
            print(params)
            student_domain=[]
            if params.get('student_level'):
                student_domain+=[('student_level','=',int(params.get('student_level')[0]))]
                print(student_domain)
            student_ids = request.env['sms_module.student'].sudo().search(student_domain)
            if not student_ids:
                return request.make_json_response(
                    {
                        'error': "NO Student Found",
                    }, status=400
                )
            return request.make_json_response([{
                'id': student_id.id,
                'name': student_id.name,
                'student_level': student_id.student_level,
                'date_of_birth': student_id.date_of_birth,
                'contact_details': student_id.contact_details,
            }for student_id in student_ids], status=200)
        except Exception as error:
            return request.make_json_response(
                {
                    'message': error
                }, status=400
            )


@http.route(['/v1/student/<int:student_id>'], type="http", auth="none", methods=["DELETE"], csrf=False)
def delete_student(self, student_id):
    student_id = request.env['sms_module.student'].sudo().search([('id', '=', student_id)])
    try:
        if not student_id:
            return request.make_json_response(
                {
                    'error': "Student not found",
                }, status=400
            )
        else:
            print('fadsf')
            student_id.unlink()
            return request.make_json_response({
                "message": "Student is deleted",
                'id': student_id.id,
                'name': student_id.name,
            }, status=200)
    except Exception as error:
        return request.make_json_response(
            {
                'message': error
            }, status=400
        )
