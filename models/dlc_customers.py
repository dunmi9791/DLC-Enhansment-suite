# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customers(models.Model):
    _name = 'dlc.customers'

    name = fields.Char('Name')
    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    date_of_birth = fields.Date('DOB')
    expiry_date = fields.Date('Expiry')
