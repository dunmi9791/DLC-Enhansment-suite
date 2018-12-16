# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Dlcs(models.Model):
    _name = 'dlc'

    name = fields.Char
    dlc_operator = fields.Many2one('dlc.personnel')
    dlc_operator2 = fields.Manay2one('dlc.personnel')
    lga = fields.Many2one('lga')
    state = fields.Many2one('states')
    dlc_supervisor = fields.Many2one('dlc.personnel')