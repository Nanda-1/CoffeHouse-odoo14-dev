from odoo import api, fields, models


class Kopi(models.Model):
    _name = 'coffehouse.kopi'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    harga_beli = fields.Integer(string='Harga Modal',required=True)
    harga_jual = fields.Integer(string='Harga Jual',required=True)
    kelompokkopi_id = fields.Many2one(comodel_name='coffehouse.kelompokkopi', 
                                        string='Jenis Kopi',
                                        ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='coffehouse.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')