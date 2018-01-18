# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api, tools, _

_logger = logging.getLogger(__name__)
_test_logger = logging.getLogger('odoo.tests')

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    sale_order_id = fields.Many2one('sale.order', string='销售订单编号')

    @api.onchange('partner_id')
    def onchange_so_ids(self):
        res = {}
        res['domain'] = {'sale_order_id': ['&', ('partner_id', '=', self.partner_id.id), ('state', 'in', ['sent', 'done'])]}
        return res
    
