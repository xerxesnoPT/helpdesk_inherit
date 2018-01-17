# -*- coding: utf-8 -*-
{
    'name': "Crm_lead Project Coding",

    'summary': """
    add Project.No in Crm_lead. when lead convert to sale-order. Project.No will be the name of SO.
    """,
    'description': """
    """,
    'author': "Shine IT",
    'website': "http://www.odoo.com.cn",
    'category': 'crm',
    'version': '0.1',
    'depends': ['crm','sale_crm'],
    'data': [
        'views/crm_lead.xml',
    ],
    'currency': 'EUR',
    'price': 0,
    'images': ['static/description/SO.jpg']
}
