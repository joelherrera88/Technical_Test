# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    facebook_url = fields.Char(string='Facebook URL')
    linkedin_url = fields.Char(string='LinkedIn URL')
    twitter_url = fields.Char(string='Twitter URL')

    is_profile_complete = fields.Boolean(string='Profile Complete', compute='_compute_is_profile_complete', store=True)

    @api.depends('facebook_url', 'linkedin_url', 'twitter_url')
    def _compute_is_profile_complete(self):
        for record in self:
            record.is_profile_complete = all([record.facebook_url, record.linkedin_url, record.twitter_url])
