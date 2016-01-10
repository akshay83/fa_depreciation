# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint
from frappe.model.document import Document

class FixedAssetAccount(Document):
	def on_trash(self):
		if self.journal_ref:
			jv = frappe.get_doc("Journal Entry", self.journal_ref)
			jv.cancel()

	def validate(self):
		if ((not cint(self.new_purchase)) and (not self.depreciation)):
			frappe.throw("Pls Input Total Depreciation Provided Till Last Fiscal Year")

		for totaldepr in self.depreciation:
			count = 0
			for totaldepr_entries in self.depreciation:
				if totaldepr.fiscal_year == totaldepr_entries.fiscal_year:
					count = count + 1;
					if count >= 2:
						frappe.throw("Looks like Fiscal Year for Fixed Assets is Already Closed")

	def post_journal_entry(self):
		if self.journal_ref:
			frappe.throw("Journal Entry Already Posted: %s",self.journal_ref)

		if self.new_purchase == 1:
			return self.journal_entry_purchase()

	def journal_entry_purchase(self):
		jv = frappe.new_doc('Journal Entry')
		jv.voucher_type = 'Journal Entry'
		jv.company = self.company
		jv.posting_date = self.purchase_date
		jv.user_remark = 'Fixed Asset Purchase'


		td1 = jv.append("accounts");	
		from erpnext.accounts.party import get_party_account
		td1.account = get_party_account('Supplier', self.purchased_from, self.company)
		td1.party = self.purchased_from
		td1.party_type = 'Supplier'
		td1.set("debit_in_account_currency", self.gross_purchase_value)
		td1.set("is_advance", 'No')

		td2 = jv.append("accounts")
		td2.account = self.fixed_asset_account
		td2.set('credit_in_account_currency', self.gross_purchase_value)
		td2.set('is_advance', 'No')

		jv.insert()
		jv.submit()
		self.journal_ref = jv.name
		self.save()
		return jv

@frappe.whitelist()
def get_purchase_cost(account):
   val = frappe.get_doc("Fixed Asset Account", account).gross_purchase_value
   return val

@frappe.whitelist()
def validate_default_accounts(company):
	comp = frappe.get_doc("Company", company)
	if not comp.default_depreciation_expense_account:
		frappe.throw("Pls Set Company Default Depreciation Expense Account")
	if not comp.default_accumulated_depreciation_account:
		frappe.throw("Pls Set Company Default Accumulated Depreciation Account")


