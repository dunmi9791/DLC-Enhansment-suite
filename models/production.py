# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import date
from odoo.exceptions import ValidationError

class Production(models.Model):
    _name = 'dlc.production'


    name = fields.Char()
    workstation_id = fields.Many2one(comodel_name="dlc.workstation", string="Office Location", required=False, )
    date = fields.Date(string="Date", required=False, )
    card_type = fields.Selection(string="Card Type", selection=[('Temporary', 'Temporary'), ('Office Total', 'Office Total'), ('Permanent', 'Permanent') ], required=False, )
    cdl = fields.Integer(string="CDL", required=False, )
    gdl = fields.Integer(string="GDL", required=False, )
    msl = fields.Integer(string="MSL", required=False, )
    pdl = fields.Integer(string="PDL", required=False, )
    sdl = fields.Integer(string="SDL", required=False, )
    ddl = fields.Integer(string="DDL", required=False, )
    total = fields.Integer(string="TOTAL", required=False, )


    @api.model
    def add_production_date(self):
        date = datetime.today()
        self.date = date


class ProductionData(models.Model):
    _name = 'dlc.pdata'
    _rec_name = 'start_date'
    _description = 'New Description'

    name = fields.Char()
    start_date = fields.Date(string="From", required=False, )
    end_date = fields.Date(string="To", required=False,)
    production_details_ids = fields.One2many(comodel_name="dlc.pdetails", inverse_name="production_data_id",
                                             string="Production Details", required=False, )

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        if self.filtered(lambda leave: leave.start_date > leave.end_date):
            raise ValidationError(_('The start date of production must be earlier end date.'))

    _sql_constraints = [
        ('end_unique', 'unique(end_date)', 'Production Data for this date has already been entered')
    ]


class ProductionDetails(models.Model):
    _name = 'dlc.pdetails'
    _rec_name = 'workstation_id'

    workstation_id = fields.Many2one(comodel_name="dlc.workstation", string="DLC", required=False, )
    production_data_id = fields.Many2one(comodel_name="dlc.pdata", string="Production", required=False, )
    card_type = fields.Selection(string="Card Type",
                                 selection=[('Temporary', 'Temporary'), ('Office Total', 'Office Total'),
                                            ('Permanent', 'Permanent')], required=False, )
    date = fields.Date(string="Date", required=False, related='production_data_id.end_date')
    cdl = fields.Integer(string="CDL", required=False, )
    gdl = fields.Integer(string="GDL", required=False, )
    msl = fields.Integer(string="MSL", required=False, )
    pdl = fields.Integer(string="PDL", required=False, )
    sdl = fields.Integer(string="SDL", required=False, )
    ddl = fields.Integer(string="DDL", required=False, )
    total = fields.Integer(string="TOTAL", required=False, )



