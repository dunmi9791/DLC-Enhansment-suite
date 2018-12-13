# -*- coding: utf-8 -*-

from odoo import models, fields, api


class States(models.Model):
    _name = 'states'

    name = fields.Char
