# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class AccountAccount(models.Model):

    _inherit = 'account.account'

    afip_activity_id = fields.Many2one(
        'afip.activity',
        'AFIP Activity',
        help='AFIP activity, used for IVA f2002 report',
        auto_join=True,
    )
