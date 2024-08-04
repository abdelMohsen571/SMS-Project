from odoo import http
from odoo.http import request



class TesApi(http.Controller):

    @http.route("/api/test",methods=["GET"],type="http",auth="none",csrf=False)
    def test_endpoint(self):
        print('test ')
