# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DashBoard(models.Model):
    _name = 'dlc.dashboard'
    _description = 'fields for the dash board'

    name = fields.Char()

    @api.multi
    def _get_count(self):
        openissues_count = self.env['dlc.issues'].search(
            [('resolution_status','=','open')])
        self.openissues_count = len(openissues_count)

    color = fields.Integer(string='color Index')
    name = fields.Char(string="Name")
    openissues_count = fields.Integer(compute='_get_count')