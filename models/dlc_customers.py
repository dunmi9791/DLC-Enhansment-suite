# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DlcCustomers(models.Model):
    _name = 'dlc.customers'
    _description = 'dlc customers'

    name = fields.Char("Name")
    dob = fields.Date(string="Date of Birth", required=False, )
    expiry_date = fields.Date(string="Expiry Date", required=False, )
    mobile_number = fields.Char(string="Mobile Number", required=False, )
    email = fields.Char(string="Email", required=False, )
