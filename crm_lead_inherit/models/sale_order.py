from odoo import fields, models, api 

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        name = self._context.get('default_name', '')
        if name.startswith('PPA'):
            vals['name'] = name
        return super(SaleOrder, self).create(vals)
            

