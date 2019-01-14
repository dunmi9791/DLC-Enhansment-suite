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
    sms_template_ids = fields.One2many(comodel_name="send_sms", inverse_name="model_id", string="", required=False, )
    new_field_ids = fields.Many2many(comodel_name="send_sms", relation="", column1="", column2="", string="", )
    message = fields.Text(string="message", required=False, )

    def send_sms_link(self,sms_rendered_content,rendered_sms_to,record_id,model,gateway_url_id):
        sms_rendered_content = sms_rendered_content.encode('ascii', 'ignore')
        sms_rendered_content_msg = urllib.parse.quote_plus(sms_rendered_content)
        if rendered_sms_to:
            rendered_sms_to = re.sub(r' ', '', rendered_sms_to)
            if '+' in rendered_sms_to:
                rendered_sms_to = rendered_sms_to.replace('+', '')
            if '-' in rendered_sms_to:
                rendered_sms_to = rendered_sms_to.replace('-', '')


        if rendered_sms_to:
            send_url = gateway_url_id.gateway_url
            send_link = send_url.replace('{mobile}',rendered_sms_to).replace('{message}',sms_rendered_content_msg)
            try:
                response = requests.request("GET", url = send_link).text
                return response
            except Exception as e:
                return e


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





    @api.model
    def send_birthday(self, id):
        id = self.id
        active_model = 'dlc.customers'
        message = self.env['send_sms'].render_template(self.message, active_model, self.id)
        mobile_no = self.env['send_sms'].render_template(self.mobile_number, active_model, self.id)
        response = self.send_sms_link(message, mobile_no, self.id, active_model, self)
        raise Warning(response)



