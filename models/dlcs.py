# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WorkStation(models.Model):
    _name = 'dlc.workstation'
    _description = 'list of work station'

    name = fields.Char()
    dlc_operator = fields.Many2many("dlc.personnel",string="DLC Personnel")
    lga = fields.Many2one('dlc.lga')
    state = fields.Many2one('dlc.states')
    dlc_supervisor = fields.Many2one('dlc.personnel')
    issues_ids = fields.One2many(comodel_name="dlc.issues", inverse_name="dlc_id", string="Issues", required=False, )
    status = fields.Selection(string="DLC Status", selection=[('active', 'Active'), ('inactive', 'Inactive'), ], required=False, default= 'active' )
    total_dlc = fields.Integer(string="Total DLCs", required=False, compute='_total_dlc')
    inactive_dlc = fields.Integer(string="Inactive DLCs", required=False, compute='_inactive_dlc')


    @api.one
    @api.depends()
    def _total_dlc(self):
        total = self.env['dlc.workstation'].search_count()
        self.total_dlc = total

    @api.one
    @api.depends()
    def _inactive_dlc(self):
        inactive = self.env['dlc.workstation'].search_count([('status', '=', 'inactive')])
        self.inactive_dlc = inactive
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
        pass

