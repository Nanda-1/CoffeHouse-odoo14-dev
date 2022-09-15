# -*- coding: utf-8 -*-
from odoo.http import request
from odoo import http
import json

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


class Coffehouse(http.Controller):
    """ The summary line for a class docstring should fit on one line.

        Routes:
          /some_url: url description
    """

    @http.route('/coffehouse/kopi', type='http', auth='none')
    def some_url(self, **kw):
        kopi = request.env['coffehouse.kopi'].search([])
        list = []
        for x in kopi :
            list.append({
                'nama_kopi' : x.name,
                'harga_beli' : x.harga_beli,
                'harga_jual'  : x.harga_jual,
                'stok'          : x.stok
            })
        return json.dumps(list)
