# -*- coding: utf-8 -*-
# © 2016 ClearCorp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock Account Move Line',
    'summary': 'Unit price on journal items',
    'version': '9.0.1.0',
    'category': 'Technical Settings',
    'website': 'http://clearcorp.cr',
    'author': 'ClearCorp',
    'license': 'AGPL-3',
    'sequence': 10,
    'application': False,
    'installable': False,
    'auto_install': False,
    'depends': [
        'stock_account',
        'purchase',
    ],
    'data': [
        'views/account_move_line_view.xml',
    ]
}
