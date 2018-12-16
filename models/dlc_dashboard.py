# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DashBoard(models.Model):
    _name = 'dlc.dashboard'
    _description = 'fields for the dash board'

    name = fields.Char()
