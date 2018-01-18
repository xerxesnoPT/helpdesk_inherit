# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Sale_Order",

    'summary': """
    associate helpdesk with sale_order
    """,
    'description': """
    """,
    'author': "Shine IT",
    'website': "http://www.odoo.com.cn",
    'category': 'helpdesk',
    'version': '0.1',
    'depends': ['helpdesk','sale'],
    'data': [
        'views/helpdesk.xml',
        'views/sale_order.xml',
    ],
    'currency': 'EUR',
    'price': 0,
    'images': ['static/description/helpdesk.jpg']
}
