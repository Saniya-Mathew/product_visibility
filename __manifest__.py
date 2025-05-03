{
        'name': "Product Visibility",
        'version': '1.0',
        'type': 'module',
        'depends': ['base', 'contacts', 'website','website_sale'],
        'author': "San",
        'category': 'Category',
        'description': """ Manage the product visibility on website """,

        # data files always loaded at installation
    'data': [
        'views/res_partner_form_customized.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    'sequence': 2,

}
