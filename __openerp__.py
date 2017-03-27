# -*- coding: utf-8 -*-
{
    'name': "hr_rules",

    'description': """
        Add a tab private with tue rules of work
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr',],

    # always loaded
    'data': [
        'security/hr_rules_access.xml',
        'security/ir.model.access.csv',
        'views/hr_rules.xml',
    ],

}
