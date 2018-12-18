# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WorkStation(models.Model):
    _name = 'dlc.workstation'
    _description = 'list of work station'

    name = fields.Char()
    dlc_operator = fields.Many2one("dlc.personnel")
    dlc_operator2 = fields.Many2one('dlc.personnel')
    lga = fields.Many2one('dlc.lga')
    state = fields.Many2one('dlc.states')
    dlc_supervisor = fields.Many2one('dlc.personnel')
