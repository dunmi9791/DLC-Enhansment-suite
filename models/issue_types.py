# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Types(models.Model):
    _name = 'issues.types'
    _description = 'types of issues'

    name = fields.Char('Issue Type')
    report_contact = fields.Char(string="Contact to Report", required=False,)
    resolution_contact = fields.Char(string="Resolution Contact")
    provider = fields.Many2one(comodel_name="service.providers", string="Service Provider", required=False, )