# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Types(models.Model):
    _name = 'issues.types'

    name = fields.Char('Issue Type')
    report = fields.Char()
    resolution = fields.Char()
