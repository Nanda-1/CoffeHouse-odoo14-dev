from odoo import api, fields, models

class kelompokkopi(models.Model):
    _name = 'coffehouse.kelompokkopi'
    _description = 'New Description'

    name = fields.Selection([
        ('arabika', 'Arabika'),
        ('robusta', 'Robusta')
    ], string='Jenis Kopi',
    required=True)

    id_kopi = fields.Char(
        string='id_kopi'
    )
    
    @api.onchange('name')
    def _onchange_id_kopi(self):
        if(self.name == 'arabika'):
            self.id_kopi = 'Kop01'
        elif(self.name == 'robusta'):
            self.id_kopi = 'Kop02'

    kopi_ids = fields.One2many(comodel_name='coffehouse.kopi', 
                                inverse_name='kelompokkopi_id', 
                                string='Daftar Kopi')

    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('kopi_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['coffehouse.kopi'].search([('kelompokkopi_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')
    
