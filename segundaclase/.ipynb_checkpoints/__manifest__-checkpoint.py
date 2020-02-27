# -*- coding: utf-8 -*-
{
    'name': "academia",

    'summary': """
        modulo de registros academicos de estudiantes y trabajadores""",

    'description': """
        registros estudiantes y trabajadores
    """,

    'author': "robin vega",
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Educación',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/vista_academia.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
       # 'demo/demo.xml',
    ],
}
