# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api


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
