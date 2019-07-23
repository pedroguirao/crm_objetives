from odoo import models, fields, api

class customer_types(models.Model):
    _name = "customer_types"
    _description = "check partner as new account"

    name = fields.Char('Name')
    is_new_account = fields.Boolean('Es cuenta nueva')