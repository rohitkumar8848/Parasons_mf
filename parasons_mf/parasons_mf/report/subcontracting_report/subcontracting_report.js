// Copyright (c) 2023, 8848 and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Subcontracting Report"] = {
	"filters": [
		{
			"fieldname":"plant",
			"label": __("Plant"),
			"fieldtype": "Link",
			"options":"Plant",
			"width": "80",
	},
	{
		"fieldname":"supplier",
		"label": __("Supplier"),
		"fieldtype": "Link",
		"options":"Supplier",
		"reqd":1,
		"width": "80",
},
	]
};
