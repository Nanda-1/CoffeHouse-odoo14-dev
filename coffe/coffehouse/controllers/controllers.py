# -*- coding: utf-8 -*-
# from odoo import http


# class Coffehouse(http.Controller):
#     @http.route('/coffehouse/coffehouse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coffehouse/coffehouse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coffehouse.listing', {
#             'root': '/coffehouse/coffehouse',
#             'objects': http.request.env['coffehouse.coffehouse'].search([]),
#         })

#     @http.route('/coffehouse/coffehouse/objects/<model("coffehouse.coffehouse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coffehouse.object', {
#             'object': obj
#         })
