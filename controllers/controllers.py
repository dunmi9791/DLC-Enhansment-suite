# -*- coding: utf-8 -*-
from odoo import http

# class DlcEnhansmentSuite(http.Controller):
#     @http.route('/dlc__enhansment__suite/dlc__enhansment__suite/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dlc__enhansment__suite/dlc__enhansment__suite/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dlc__enhansment__suite.listing', {
#             'root': '/dlc__enhansment__suite/dlc__enhansment__suite',
#             'objects': http.request.env['dlc__enhansment__suite.dlc__enhansment__suite'].search([]),
#         })

#     @http.route('/dlc__enhansment__suite/dlc__enhansment__suite/objects/<model("dlc__enhansment__suite.dlc__enhansment__suite"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dlc__enhansment__suite.object', {
#             'object': obj
#         })