# -*- coding: utf-8 -*-

from odoo import models, fields, api


class States(models.Model):
    _name = 'dlc.states'

    name = fields.Char()
