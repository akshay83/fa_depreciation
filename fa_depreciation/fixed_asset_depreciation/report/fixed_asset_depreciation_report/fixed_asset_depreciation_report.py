# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from erpnext.accounts.utils import get_fiscal_year
from fa_depreciation.fixed_asset_depreciation.doctype.fixed_asset_account.depreciation_report \
		import get_report_data, get_report_columns


def execute(filters=None):
    finyrfrom, finyrto = get_fiscal_year(fiscal_year = filters["fiscal_year"])[1:]
    data = get_report_data(financial_year_from = str(finyrfrom), \
		financial_year_to = str(finyrto), company = filters["company"], expand_levels=filters.expand_levels)
    columns = get_report_columns(financial_year_from = finyrfrom, financial_year_to = finyrto)

    return columns, data
