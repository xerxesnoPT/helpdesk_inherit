import logging
from odoo import models, fields, api, tools

_logger = logging.getLogger(__name__)
_test_logger = logging.getLogger('odoo.tests')

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    helpdesk_ids = fields.One2many('helpdesk.ticket', 'sale_order_id', string='Helpdesk.No')
