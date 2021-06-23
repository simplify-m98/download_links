from odoo import http, _
from odoo.http import request


class DownloadOnForms(http.Controller):
    routes = ['/forms/hello', '/forms/goodbye']

    @http.route([i for i in routes], type='http', auth="user", website=True)
    def route_hello(self):
        print(request.httprequest.base_url)
        return f"<h1> Hello! {request.httprequest.base_url} </h1>"
