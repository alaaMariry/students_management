# -*- coding: utf-8 -*-
# from odoo import http


# class Alaa(http.Controller):
#     @http.route('/alaa/alaa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alaa/alaa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alaa.listing', {
#             'root': '/alaa/alaa',
#             'objects': http.request.env['alaa.alaa'].search([]),
#         })

#     @http.route('/alaa/alaa/objects/<model("alaa.alaa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alaa.object', {
#             'object': obj
#         })
