from odoo import models, fields, api

class objetive_years(models.Model):
    _name = "objetive_years"
    _description = "Report of initial state"

    name = fields.Char('Name')
    commercial_id = fields.Many2one('res.uers',string='Comercial',
                                    required=True)
    team_id = fields.Many2one('crm.team',string='Equipo de ventas')
    year = fields.Integer('Año',required=True)
    #objetive_team_id = fields.Many2one('',string='Obj. Equipo')
    note = fields.Text('Notas',description='Seguimiento al cambiar')
    responsable_id = fields.Many2one('res.users',string='Responsable',
                                     required=True)
    status_id = fields.Selection(string='Estado',selection=[('borrador',
                                                             'Borrador'),
                                                            ('activo','Activo'),('archivado','Archivado')])
    previus_cn_reached = fields.Float('Cumplido CN A-1(€)')
    previus_ca_reached = fields.Float('Cumplido Ca A-1(€)')
    total_reached = fields.Float(string='Total A-1',compute='_total_reached',
                                 readonly=True)
    objetive_ca = fields.Float(string='Objetivo CA',readonly=True)
    objetive_cn = fields.Float(string='Objetivo CN', readonly=True)
    sale_ca = fields.Float(string='Venta CA',readonly=True)
    sale_cn = fields.Float(string='Venta CN',readonly=True)

    got_ca_percent = fields.Float(string='Conseguido CA (%)',readonly=True)
    got_cn_percent = fields.Float(string='Conseguido CN (%)',readonly=True)
    got_ca_count = fields.Integer(string='Objetivo Ud. CA',readonly=True)
    got_cn_count = fields.Integer(string='Objetivo Ud. CN',readonly=True)
    won_ca_count = fields.Integer(string='Ganadas CA',readonly=True)
    wonn_cn_count = fields.Integer(string='Ganadas CN',readonly=True)

    got_ca_count_percent = fields.Float('Conseguido Ud CA (%)',readonly=True)
    got_cn_count_percent = fields.Float('Conseguido Ud CN (%)', readonly=True)

    total_objetive = fields.Float('Objetivo (€)', required=True)
    total_sale = fields.Float('Venta total (€)', required=True)
    percent_got = fields.Float('Objetivo de venta (%)',required=True)
    percent_count_got = fields.Float('Objetivo de cuentas (%)', required=True)

    #line_ids = fields.One2many('')
    #month_ids = fields.One2many('')

    active_op_count = fields.Integer('Op. activas',readonly=True)
    active_op = fields.Float('Op. activas (€)',readonly=True)
    #expired_op_count =
    #expired_act_count =
    #panned_act_count =
    #finished_act_count =




    @api.depends('previus_ca_reached','previus_cn_reached')
    def _total_reached(self):
        for record in self:
            record['total_reached']=record.previus_cn_reached + \
                                    record.previus_ca_reached