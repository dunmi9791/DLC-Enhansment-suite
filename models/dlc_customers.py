# -*- coding: utf-8 -*-

from odoo.exceptions import except_orm, UserError, Warning
import requests
import urllib
import re
import logging
_logger = logging.getLogger(__name__)
from datetime import datetime
from odoo import models, fields, api


class DlcCustomers(models.Model):
    _name = 'dlc.customers'
    _description = 'dlc customers'


    name = fields.Char("Name")
    dob = fields.Date(string="Date of Birth", required=False, )
    expiry_date = fields.Date(string="Expiry Date", required=False, )
    mobile_number = fields.Char(string="Mobile Number", required=False, )
    email = fields.Char(string="Email", required=False, )
    dl_number = fields.Char(string="license Number", required=False, )



    @api.multi
    def send_birthday_email(self):
        today_date = datetime.today().date()
        for customer in self.env['dlc.customers'].search([]):
            if customer.dob:
                cusday = datetime.strftime(customer.dob, '%Y-%m-%d')
                cus_birthdate = datetime.strptime(cusday, '%Y-%m-%d').date()
                if today_date.day == cus_birthdate.day and today_date.month == cus_birthdate.month:
                    template_id = self.env.ref('DLC-Enhansment-suite.email_birthday_wishes_customer_template')
                    template_id.send_mail(customer.id, force_send=True)





    @api.multi
    def send_birthday_sms(self,):
        today_date = datetime.today().date()
        for customer in self.env['dlc.customers'].search([]):
            if customer.dob:
                cusday = datetime.strftime(customer.dob, '%Y-%m-%d')
                cus_birthdate = datetime.strptime(cusday, '%Y-%m-%d').date()
                if today_date.day == cus_birthdate.day and today_date.month == cus_birthdate.month:
                    template_id = self.env.ref('DLC-Enhansment-suite.sms_birthday_wishes_customer_template')
                    template_id.send_sms(template_id, customer.id)




