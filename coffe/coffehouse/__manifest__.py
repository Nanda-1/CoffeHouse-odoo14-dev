# -*- coding: utf-8 -*-
{
    'name': "coffehouse",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "CoffeHouse",
    'website': "http://www.CoffeHouse.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/kelompok_kopi.xml',
        'views/menu.xml',
        'views/kopi.xml',
        'views/order.xml',
        'views/ispegawai.xml',
        'views/supplier.xml',
        'views/customer.xml',
        'report/report.xml',
        'report/orderpdf.xml',
        'report/kopi_report.xml',
        'report/w_orderreport.xml',
        'report/wizzard_kopireport.xml',
        'wizzard/report_kopi.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
