# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import date

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
    production_details_ids = fields.One2many(comodel_name="dlc.pdetails", inverse_name="production_data_id", string="Production Details", required=False, )
    state = fields.Selection(string="", selection=[('unprocessed', 'Unprocessed'), ('Processed', 'Processed')],
                             required=False, default='unprocessed',
                             track_visibility='onchange', )
    _sql_constraints = [
        ('start_unique', 'unique(start_date)', 'Production Data for this date has already been entered')
    ]

    _sql_constraints = [
        ('end_unique', 'unique(end_date)', 'Production Data for this date has already been entered')
    ]
    @api.multi
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('unprocessed', 'Processed'),
                    ]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for cash in self:
            if cash.is_allowed_transition(cash.state, new_state):
                cash.state = new_state
            else:
                msg = _('Moving from %s to %s is not allowed') % (cash.state, new_state)
                raise UserError(msg)

    @api.multi
    def diff(self):
        workstation = self.env['dlc.workstation']
        dlc = [workstation.search([])]
        pdlc = self.env['dlc.pdetails']
        domain = [('production_data_id', '=', self.id)]
        pdlct = pdlc.search(domain)

        dlcb = [set([a.workstation_id.ids[0] for a in pdlct if a.workstation_id.ids])]
        nowork2 = [x for x in dlc + dlcb if x not in dlcb]
        return nowork2




    @api.multi
    @api.model_create_multi
    def process_data(self, values):
        self.change_state('Processed')
        workstation = self.env['dlc.workstation']
        dlc = set([workstation.search([])])
        pdlc = self.env['dlc.pdetails']
        domain = [('production_data_id', '=', self.id)]
        pdlct = pdlc.search(domain)

        dlcb = [set([a.workstation_id.ids[0] for a in pdlct if a.workstation_id.ids])]


        nowork2 = dlcb.difference(dlc)
        for line in nowork2:
            values = {
                        'workstation_id': line.id,
                        'production_data_id': self.id,
                        'card_type': 'Office Total',
                        'cdl': 0,
                        'gdl': 0,
                        'msl': 0,
                        'pdl': 0,
                        'sdl': 0,
                        'ddl': 0,
                        'total': 0,
                    }

            self.env['dlc.pdetails'].create(values)


class ProductionDetails(models.Model):
    _name = 'dlc.pdetails'
    _rec_name = 'workstation_id'

    workstation_id = fields.Many2one(comodel_name="dlc.workstation", string="DLC", required=False, )
    production_data_id = fields.Many2one(comodel_name="dlc.pdata", string="Production", required=False, )
    card_type = fields.Selection(string="Card Type",
                                 selection=[('Temporary', 'Temporary'), ('Office Total', 'Office Total'),
                                            ('Permanent', 'Permanent')], required=False, )
    date = fields.Date(string="Date", required=False, related='production_data_id.start_date')
    cdl = fields.Integer(string="CDL", required=False, )
    gdl = fields.Integer(string="GDL", required=False, )
    msl = fields.Integer(string="MSL", required=False, )
    pdl = fields.Integer(string="PDL", required=False, )
    sdl = fields.Integer(string="SDL", required=False, )
    ddl = fields.Integer(string="DDL", required=False, )
    total = fields.Integer(string="TOTAL", required=False, )



