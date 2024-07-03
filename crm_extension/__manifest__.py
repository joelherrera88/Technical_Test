# -*- coding: utf-8 -*-
{
    'name': "crm_extension",
    'summary': "Follow next instructions to accomplish the test.",
    'description': """
       Implement an extension for the CRM module that:
        (1)Allows registering the url of the following social accounts for each customer[ Facebook,LinkedIn,Twitter]
        (2)Shows social networks in a separate tab in the customer profile, each one with the corresponding icon.
        (3)If for a customer we have all the social networks, we say that it is a “completed profile” and then we show an image with a checkmark “Profile complete”. 
           Show this info from all of the customers' views.
        (4)Add a filter that shows the “Profile incomplete” customers.
        (5)Add in the Website a page dedicated to promoting my customers, showing a list of them containing brief information 
           about each one that includes their social accounts data.
        (6)Make search available for that page in order to find Customers by name and social accounts.
    """,
    'author': "Joel Herrera Bravo",
    'website': "https://www.yourcompany.com",
    'category': 'Sales/CRM',
    'sequence': -1,
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['crm','website_crm'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/customer_promotion_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
