from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Order(models.Model):
    _name = 'coffehouse.order'
    description = 'New Description'

    id_order = fields.Char(string='No. Nota')
    sequence = fields.Char('Order Reference', default='New')
    nama_pembeli = fields.Many2one(comodel_name="res.partner", string='Nama Pembeli')
    id_member = fields.Char(
        compute="_compute_id_member",
        string='Id_member',
        required=False)
    tgl_order = fields.Datetime(string='Tgl. Transaksi', default=fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailorder_ids = fields.One2many(
        comodel_name='coffehouse.detailorder',
        inverse_name='order_id',
        string='Detail order')
    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancelled', 'Cancelled'),
                   ],
        required=True, readonly=True, default='draft')

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('coffehouse.order')
        return super(Order,self).create(vals)

    @api.depends('nama_pembeli')
    def _compute_id_member(self):
        for rec in self:
            rec.id_member = rec.nama_pembeli.id_member

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('detailorder_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['coffehouse.detailorder'].search([('order_id', '=', rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    # @api.ondelete(at_uninstall=False)
    # def __ondelete_order(self):
    #     if self.detailorder_ids:
    #         a=[]
    #         for rec in self:
    #             a = self.env['coffehouse.detailorder'].search([('order_id','=',rec.id)])
    #             print(a)
    #         for ob in a:
    #             print(str(ob.barang_id.name) + ' ' + str(ob.qty))
    #             ob.barang_id.stok += ob.qty

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise UserError("Tdak dapat menghapus jika status BUKAN DRAFT")
        else:
            if self.detailorder_ids:
                a = []
                for rec in self:
                    a = self.env['coffehouse.detailorder'].search([('order_id', '=', rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.barang_id.name) + ' ' + str(ob.qty))
                    ob.barang_id.stok += ob.qty
        record = super(Order, self).unlink()

    def write(self, vals):
        for rec in self:
            a = self.env['coffehouse.detailorder'].search([('order_id', '=', rec.id)])
            print(a)
            for data in a:
                print(str(data.barang_id.name) + ' ' + str(data.qty) + ' ' + str(data.barang_id.stok))
                data.barang_id.stok += data.qty
        record = super(Order, self).write(vals)
        for rec in self:
            b = self.env['coffehouse.detailorder'].search([('order_id', '=', rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.barang_id.name) + ' ' + str(databaru.qty) + ' ' + str(databaru.barang_id.stok))
                    databaru.barang_id.stok -= databaru.qty
                else:
                    pass
        return record

    _sql_constraints = [
        ('no_nota_unik', 'unique (name)', 'Nomor Nota tidak boleh sama !!!')
    ]




class Detailorder(models.Model):
    _name = 'coffehouse.detailorder'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    order_id = fields.Many2one(comodel_name='coffehouse.order', string='Detail order')
    kopi_id = fields.Many2one(comodel_name='coffehouse.kopi', string='List kopi')
    item_price = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('point')
    def _compute_point(self):
            for record in self:
                record.point = record.subtotal / 1000 


    @api.depends('item_price','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.item_price
    
    @api.onchange('kopi_id')
    def _onchange_kopi_id(self):
        if (self.kopi_id.harga_jual):
            self.item_price = self.kopi_id.harga_jual
    
    @api.model
    def create(self,vals):
        record = super(Detailorder,self).create(vals)
        if record.qty:
            self.env['coffehouse.kopi'].search([('id','=',record.kopi_id.id)]).write({'stok' : record.kopi_id.stok - record.qty})
        return record


    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Minimal Pembelian 1 ".format(rec.kopi_id.name))
            elif (rec.kopi_id.stok < rec.qty):
                raise ValidationError('Stok {} tidak mencukupi, hanya tersedia {}'.format(rec.kopi_id.name,rec.kopi_id.stok))


    class member(models.Model):
        _name = 'coffehouse.pelanggan'
        _description = 'Member'
    
        
        member_id = fields.Many2one(
            string='id_member',
            comodel_name='coffehouse.order',
        )
        
        name = fields.Char(string='Name')
        
        no_tlpn = fields.Integer(
            string='no_tlpn',
        )
        
        point = fields.Integer(
            compute='_compute_point' )
        
        @api.depends('point')
        def _compute_point(self):
             for rec in self:
                rec.point = rec.subtotal / 1000 
        
    
