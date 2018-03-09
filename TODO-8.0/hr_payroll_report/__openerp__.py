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
    'name': 'Hr Payroll Report',
    'version': '1.0',
    'url': 'http://launchpad.net/openerp-ccorp-addons',
    'author': 'ClearCorp S.A.',
    'website': 'http://clearcorp.co.cr',
    'category': 'Human Resources',
    'complexity': 'normal',
    'description': """This module modifies the payslip report
    """,
    'depends': [
        'hr_payroll',
        'report_webkit_lib',
    ],
    'init_xml': [],
    'demo_xml': [],
    'update_xml': [
                    'hr_payroll_report_report.xml',
                    'hr_payroll_report_view.xml',
                ],
    'license': 'AGPL-3',
    'installable': False,
    'active': False,
}
