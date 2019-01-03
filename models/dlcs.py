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
