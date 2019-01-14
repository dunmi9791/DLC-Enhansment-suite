# -*- coding: utf-8 -*-

import logging
_logger = logging.getLogger(__name__)

from odoo import models, fields, api

class Customers(models.Model):
    _name = 'new_module.new_module'
    _inherit = 'new_module.new_module'

    name = fields.Char()



sms_template_id = fields.Many2one(comodel_name="send_sms", string="sms templste", required=False, )