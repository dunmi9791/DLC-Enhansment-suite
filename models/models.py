# -*- coding: utf-8 -*-

from odoo import models, fields, api

class issues(models.Model):
    _name = 'dlc.issues'

    issue_id = fields.Many2one("issue.types", required=True)
    dlc_id = fields.Many2one("dlc.workstation", required=True)
    dlc_status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')])
    date_report = fields.Date('Date Reported')
    resolution_status = fields.Selection([
        ('open', 'Open'),
        ('resolved', 'Resolved')
    ], default='open')
    date_resolved = fields.Date('Date Resolved')

# class dlc__enhansment__suite(models.Model):
#     _name = 'dlc__enhansment__suite.dlc__enhansment__suite'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100