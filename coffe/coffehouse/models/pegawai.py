from odoo import api, fields, models




class Pegawai(models.Model):
    _name = 'coffehouse.pegawai'
    _description = 'Data Pegawai'


    
    id_pegawai = fields.Integer(
        string='id_pegawai'
    )
    
    name = fields.Char(string='Nama Pegawai')
    
    
    no_tlp = fields.Integer(
        string='no_tlp',
    )
    
    alamat = fields.Text(
        string='alamat',
    )
    
    
    
