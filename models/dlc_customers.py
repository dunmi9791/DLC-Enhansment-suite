# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customers(models.Model):
    _name = dlc.customers

    name = fields.Char
    first_name = fields.Char
    last_name = fields.Char
    date_of_birth = fields.Date
    expiry_date = fields.Date
