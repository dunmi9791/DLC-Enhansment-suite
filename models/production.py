# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Production(models.Model):
    _name = 'dlc.production'

    name = fields.Char()
