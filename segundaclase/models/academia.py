# -*- coding: utf-8 -*-

from odoo import models, fields


class academia(models.Model):
     _name = 'academia.usuarios'
     _description = 'Registros de la academia'

     name = fields.Char()
     apellido = fields.Char()
     apellido2 = fields.Integer()
     matricula = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

        state = fields.Selection(selection=[
        ('draft', 'New'),
        ('approve', 'Approved'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),], string='State', default='draft')
        
        location_id = fields.Many2one(comodel_name='res.partner', ondelete='restrict',)     
        
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
