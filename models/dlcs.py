# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from datetime import date
from odoo.exceptions import UserError
from odoo.tools.translate import _
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta



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
    dlc_cug = fields.Char(string="DLC CUG Number")
    today = fields.Date(default=date.today())
    period = fields.Date(compute='_last_seven', store=True)
    production_ids = fields.One2many(comodel_name="dlc.pdetails", inverse_name="workstation_id", string="Production", required=False, )
    sum_production_7days = fields.Integer(string="Production in Last 7 Days",  compute='_dlc_production', required=False,)
    production_id2s = fields.One2many(comodel_name="dlc.pdetails", inverse_name="workstation_id", string="Production",
                                     required=False, )
    production_id3 = fields.Many2many(comodel_name="dlc.pdetails", relation="workstation_id", column1="", column2="", string="", )




    @api.one
    @api.depends()
    def _total_dlc(self):
        total = self.env['dlc.workstation'].search_count()
        self.total_dlc = total

    @api.one
    @api.depends()
    def _last_seven(self):
        today = fields.Date.today()
        d = today - timedelta(days=7)
        self.period = d



    @api.one
    @api.depends()
    def _inactive_dlc(self):
        inactive = self.env['dlc.workstation'].search_count([('status', '=', 'inactive')])
        self.inactive_dlc = inactive
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
        pass
    @api.one
    @api.depends('production_ids.total', )
    def _dlc_production(self):
        self.sum_production_7days = sum(production.total for production in self.production_id2s)
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
        pass





    _sql_constraints = [
        ('name_unique', 'unique(name)', 'DLC Name must be unique')
        ]

