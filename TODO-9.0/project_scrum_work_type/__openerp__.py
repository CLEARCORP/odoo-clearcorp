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
    "name" : 'Project scrum work type',
    "version" : '1.0',
    "author" : 'ClearCorp',
    "category": 'Project Management',
    "sequence": 10,
    "website" : "http://clearcorp.cr",
    "depends" : [
                   'project_scrum_method',
                   'project_work_type',
                   'hr',
                 ],
    "data" : [
              'view/view.xml',
              'security/ir.model.access.csv',
              ],
    "demo_xml" : [],
    "test" : [],
    "auto_install": False,
    "application": False,
    "installable": False,
    'license': 'AGPL-3',
}
