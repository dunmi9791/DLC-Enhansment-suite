# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Dlcpersonnel(models.Model):
    _name = 'dlc.personnel'

    name = fields.Char(string="Name", compute="fullname", required=False)
    email = fields.Char(string="Email", required=False)
    dlc_id = fields.Many2one('dlc.workstation', string="DLC")
    phone = fields.Char(string="Mobile Number", required=False)
    supervisor = fields.Boolean(string="Is a Supervisor", default=False)
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")


    @api.one
    @api.depends('first_name', 'last_name')
    def fullname(self):
        for record in self:
            record['name'] = (record.first_name or '') + ' ' + (record.last_name or '')
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
