from odoo import http
from odoo.http import request

from odoo import http
from odoo.http import request


class CustomerPromotion(http.Controller):

    @http.route('/customers/promotion', type='http', auth="public", website=True)
    def customer_promotion(self, **kwargs):
        search_term = kwargs.get('search', '').lower()
        domain = ['|', '|', '|',
                  ('name', 'ilike', search_term),
                  ('facebook_url', 'ilike', search_term),
                  ('linkedin_url', 'ilike', search_term),
                  ('twitter_url', 'ilike', search_term)]
        customers = request.env['res.partner'].search(domain)
        return request.render("crm_extension.customer_promotion_template", {'customers': customers})
