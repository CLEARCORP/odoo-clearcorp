# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Addons modules by CLEARCORP S.A.
#    Copyright (C) 2009-TODAY CLEARCORP S.A. (<http://clearcorp.co.cr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Partner Balance Report',
    'version': '1.0',
    'author': 'ClearCorp',
    'category': 'Accounting & Finance',
    'description': """
Partner Balance Report.
==========================
This module modifies the Partner Balance Report. Add Qweb report support""",
    'website': 'http://clearcorp.co.cr',
    'depends': [
                'res_currency_priority',
                'account_report_lib',
                ],
    'data': [
             'report/report.xml',
             'views/report_partner_balance.xml',
            ],
    'active': False,
    'installable': False,    
    'license': 'AGPL-3',
}