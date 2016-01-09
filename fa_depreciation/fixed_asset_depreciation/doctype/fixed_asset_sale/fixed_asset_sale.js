cur_frm.cscript.fixed_asset_account = function (doc,dt,dn) {
	if (doc.fixed_asset_account) {
		return frappe.call({
			method: "fa_depreciation.fixed_asset_depreciation.doctype.fixed_asset_account.fixed_asset_account.get_purchase_cost",
			args: {account: doc.fixed_asset_account},
			callback: function(r) {
				doc.asset_purchase_cost = Math.abs(r.message);
				refresh_field('asset_purchase_cost');
			}
		});
	}
}

cur_frm.cscript.sales_amount = function (doc,dt,dn) {
	if (doc.sales_amount) {
		return frappe.call({
			method: "fa_depreciation.fixed_asset_depreciation.doctype.fixed_asset_account.depreciation_report.get_written_down_when_selling_fixed_asset",
			args: {fixed_asset: doc.fixed_asset_account, saledate: doc.posting_date, company: doc.company, saleamount: doc.asset_purchase_cost},
			callback: function(r) {
				doc.accumulated_depreciation = Math.abs(r.message);
				refresh_field('accumulated_depreciation');
				if (parseFloat(doc.asset_purchase_cost) - parseFloat(doc.accumulated_depreciation) > parseFloat(doc.sales_amount)) {
				doc.profit_or_loss = "Loss";
				} else {
					doc.profit_or_loss = "Profit";
				}
				doc.difference = Math.abs(parseFloat(doc.asset_purchase_cost) - parseFloat(doc.accumulated_depreciation) - parseFloat(doc.sales_amount));
				refresh_field('profit_or_loss');
				cur_frm.refresh();
				
			}
		});
	}
}
// Make Journal Entry
frappe.ui.form.on("Fixed Asset Sale", "post_journal_entry", function(frm) {

	return  frappe.call({
		method: 'post_journal_entry',
		doc: frm.doc,
		callback: function(r) {
			frm.fields_dict.post_journal_entry.$input.addClass("btn-primary");
			var doclist = frappe.model.sync(r.message);
			frappe.set_route("Form", doclist[0].doctype, doclist[0].name);
		}
	});
});
cur_frm.cscript.company = function (doc,dt,dn) {
	if (doc.company) {
		return frappe.call({
			method: "fa_depreciation.fixed_asset_depreciation.doctype.fixed_asset_account.fixed_asset_account.validate_default_accounts",
			args: {company: doc.company}		
		});
	}
}

