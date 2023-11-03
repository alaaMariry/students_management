# -*- coding: utf-8 -*-
{
    'name': "student management",

    'summary': """
        student school management""",

    'description': """
        Long description of module's purpose
    """,
    'sequence': -100,

    'author': "Alaa",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/student_fees_wizard.xml',
        'views/views.xml',
        'views/result.xml',
        'views/subject.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
