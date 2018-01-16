# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api, tools, _

_logger = logging.getLogger(__name__)
_test_logger = logging.getLogger('odoo.tests')

class Crm_lead(models.Model):
    _inherit = 'crm.lead'
    project_coding = fields.Text(string='项目编号')

    @api.model
    def create(self,vals):
        vals['project_coding'] = self.env['ir.sequence'].next_by_code('project_coding.sequence')
        return super(Crm_lead,self).create(vals)
    
