# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DLCs(models.Model):
    _name = dlc.pesonnel

    name = fields.Char
    email = fields.Char
    dlc_id = fields.Many2one('dlc')
    phone = fields.Char
    supervisor = fields.Boolean
    first_name = fields.Char
    last_name = fields.Char
