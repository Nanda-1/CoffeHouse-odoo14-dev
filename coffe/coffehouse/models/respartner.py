from odoo import models,fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_pegawai= fields.Boolean(
        string='is_pegawai'
    )

    is_customer = fields.Boolean(
        string='is_customer',
    )

    id_member = fields.Char(
        string='Id Member',
        required=False,
        domain="[('is_customer', '=', True)]")
    
    
    