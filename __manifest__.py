# -*- coding: utf-8 -*-
{
    'name': "DLC_Enhansment_Suite",

    'summary': """
        An app design for the management of DLC issues""",

    'description': """
        The purpose of this app is to manage data from issues emarnating from DLCs 
    """,

    'author': "Secteur Network Solutions",
    'website': "http://www.secteurnetworks.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/actions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}