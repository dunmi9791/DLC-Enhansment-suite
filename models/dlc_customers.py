# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DlcCustomers(models.Model):
    _name = 'dlc.customers'
    _description = 'dlc customers'

    name = fields.Char("Name")
