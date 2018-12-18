# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lga(models.Model):
    _name = 'dlc.lga'

    name = fields.Char('name')
    state = fields.Many2one('dlc.states')
