from odoo import fields,models,api
class kopireport(models.TransientModel):
    _name = 'coffehouse.kopireport'
    _description = 'kopireport'

    pegawai_id = fields.Many2many(
        comodel_name='res.partner',
        String='Pegawai',
        required=False
    )
    
    def action_kopi_report(self):
        filter= []
        pegawai_id = self.pegawai_id

        if pegawai_id:
            filter += [('nama_pegawai', '=', pegawai_id.id)]


        kopi = self.env['coffehouse.kopi'].search_read(filter)
        print(kopi)
        data={
            'form': self.read()[0],
            'kopixx' : kopi
        }
        print(data)
        return self.env.ref('coffhouse.wizzard_kopireport_pdf').report_action(self, data=data)

    