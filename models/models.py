# -*- coding: utf-8 -*-

from odoo import models, fields, api

class issues(models.Model):
    _name = 'dlc.issues'
    _description = 'dlc issues'
    _inherit = ['mail.thread']

    issue_id = fields.Many2one("issues.types", required=True)
    dlc_id = fields.Many2one("dlc.workstation", required=True)
    dlc_status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')])
    date_report = fields.Date('Date Reported')
    resolution_status = fields.Selection([
        ('open', 'Open'),
        ('reported', 'Reported')
        ('resolved', 'Resolved')
    ], default='open',track_visibility= 'onchange',)
    date_resolved = fields.Date('Date Resolved')
    notes = fields.Text('Notes')

    @api.multi
    def report_issue(self):
        self.resolution_status = 'reported'

    @api.multi
    def resolve_issue(self):
        self.resolution_status = 'resolved'

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