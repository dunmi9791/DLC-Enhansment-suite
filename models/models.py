# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, time

class Issues(models.Model):
    _name = 'dlc.issues'
    _description = 'dlc issues'
    _inherit = ['mail.thread']

    issue_id = fields.Many2one("issues.types", required=True)
    dlc_id = fields.Many2one("dlc.workstation", required=True)
    dlc_status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')])
    date_report = fields.Date('Date Reported')
    resolution_status = fields.Selection([
        ('open', 'Open'),
        ('reported', 'Reported'),
        ('resolved', 'Resolved')
    ], default='open',track_visibility='onchange',)
    date_resolved = fields.Date('Date Resolved')
    notes = fields.Text('Notes')
    open_issues = fields.Integer(compute='open',store=True)
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], related="dlc_id.status")




    @api.multi
    def report_issue(self):
        self.resolution_status = 'reported'

    @api.multi
    def resolve_issue(self):
        self.resolution_status = 'resolved'
        self.dlc_status = 'active'
        self.date_resolved = datetime.today()

    @api.multi
    @api.depends('resolution_status')
    def open(self):
        count = self.env['dlc.issues'].search_count([('resolution_status','=','open')])
        self.open_issues = count


    @api.multi
    def write(self, values):
        res = super(Issues, self).write(values)
        self.ensure_one()
        value = {}
        #value['id'] = self.dlc_id.id
        if 'dlc_status' in values:
            value['status'] = values['dlc_status']
            dlc_obj = self.env['dlc.workstation'].search([('id','=',self.dlc_id.id)])
            dlc_obj.write(value)
        return res

    @api.model
    def create(self, values):
        res = super(Issues, self).create(values)
        dlcst = {}
        if res.dlc_status == 'inactive':
            dlcst['status'] = res.dlc_status
            dlc_st = self.env['dlc.workstation'].search([('id', '=', values.get('dlc_id'))])
            dlc_st.write(dlcst)
        return res




    @api.model
    def sendmail_action_method(self):
         active_ids = self._context.get('active_ids')
         for active_id in active_ids:
             self.env['dlc.issues'].browse(active_id).name = 'name'
         return True 
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