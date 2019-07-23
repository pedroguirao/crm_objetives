from odoo import models, fields, api

class res_partner_ex(models.Model):
    _inherit = 'res.partner'

    customer_type_id= fields.Many2one('customer_types')
