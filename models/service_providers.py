# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ServiceProviders(models.Model):
    _name = 'service.providers'
    _inherit = 'res.partner'

    name = fields.Char()
