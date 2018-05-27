# -*- coding: utf-8 -*-
# by Juan Carlos Montoya <odooerpcloud@gmail.com>

{
    'name': "Library Management",

    'summary': """
        Library Management Module for Odoo 11
        """,

    'description': """
     Library Management Module for Odoo 11

    """,

    'author': "Odoo ERP Cloud",
    'website': "http://odooerpcloud.com",

    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        "views/book_view.xml",
    ],
    'application': True,
}