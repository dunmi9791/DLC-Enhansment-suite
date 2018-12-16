# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lga(models.Model):
    _name = 'lga'

    name = fields.Char('name')
    state = fields.Many2one('states')
