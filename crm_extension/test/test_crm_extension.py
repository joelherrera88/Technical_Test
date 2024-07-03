from odoo.tests.common import TransactionCase


class TestCustomerPromotionTemplate(TransactionCase):

    def setUp(self):
        super(TestCustomerPromotionTemplate, self).setUp()
        # Set up test data
        self.Partner = self.env['res.partner']
        self.partner1 = self.Partner.create({
            'name': 'Test Customer 1',
            'facebook_url': 'http://www.facebook.com/testcustomer1',
            'linkedin_url': 'http://www.linkedin.com/testcustomer1',
            'twitter_url': 'http://www.twitter.com/testcustomer1',
        })

    def test_customer_promotion_template_rendering(self):
        # Render the customer_promotion_template
        rendered_template = self.env['ir.ui.view'].render_template('crm_extension.customer_promotion_template', values={'customers': self.Partner.search([])})
        # Check if the rendered template contains the expected content
        self.assertIn('Test Customer 1', str(rendered_template))
        self.assertIn('http://www.facebook.com/testcustomer1', str(rendered_template))
        self.assertIn('http://www.linkedin.com/testcustomer1', str(rendered_template))
        self.assertIn('http://www.twitter.com/testcustomer1', str(rendered_template))

    def test_search_functionality(self):
        # Create additional test customers
        self.partner2 = self.Partner.create({
            'name': 'Test Customer 2',
            'facebook_url': 'http://www.facebook.com/testcustomer2',
            'linkedin_url': 'http://www.linkedin.com/testcustomer2',
            'twitter_url': 'http://www.twitter.com/testcustomer2',
        })
        search_result = self.Partner.search([('name', 'ilike', '1')])
        self.assertEqual(len(search_result), 1)
        self.assertEqual(search_result.name, 'Test Customer 1')

    def test_customer_information_display(self):
        # Render the template with a specific customer
        rendered_template = self.env['ir.ui.view'].render_template(
            'crm_extension.customer_promotion_template',
            values={'customers': self.Partner.search([('name', '=', 'Test Customer 1')])}
        )