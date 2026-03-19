# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    silae_code = fields.Char(string='Code Silae', copy=False, tracking=True)

    _sql_constraints = [
        ('silae_code_uniq', 'unique (silae_code)', 'Ce Code Silae est déjà utilisé par un autre contact !')
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('silae_code') and not self.env.user.has_group('partner_silae.group_partner_silae_manager'):
                raise UserError(_('Seuls les Managers Silae peuvent définir le Code Silae.'))
        return super(ResPartner, self).create(vals_list)

    def write(self, vals):
        if 'silae_code' in vals and not self.env.user.has_group('partner_silae.group_partner_silae_manager'):
            raise UserError(_('Seuls les Managers Silae peuvent modifier le Code Silae.'))
        return super(ResPartner, self).write(vals)
