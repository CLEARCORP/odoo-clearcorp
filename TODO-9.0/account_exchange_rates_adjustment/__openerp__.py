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
    "name" : 'Account Exchange Rates Adjustment',
    "version" : '1.0',
    "category": 'Accounting & Finance',
    'summary': 'Adjust the amount of currency at the exchange rate on a specified day',
    "author" : 'ClearCorp',
    'website': 'http://clearcorp.co.cr',
    "depends" : [
                 "account_report_lib",
                 "account_reconcile_forced_partner",
                 "currency_second_rate_BCCR",
                 "res_currency_priority",
                ],

    "data" : [
              "wizard/account_exchange_rates_adjustment.xml",
              "account_exchange_rates_adjustment.xml",
              ],
    'installable': False,
    'auto_install': False,
    'license': 'AGPL-3',
}
