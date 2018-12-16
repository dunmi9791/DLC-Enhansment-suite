# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Types(models.Model):
    _name = 'issues.types'

    name = fields.Char('Issue Type')
    report_recipient = fields.Char()
    resolution_recipient = fields.Char()
