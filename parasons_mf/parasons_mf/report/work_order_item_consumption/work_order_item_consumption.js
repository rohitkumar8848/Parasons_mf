// Copyright (c) 2023, 8848 and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Work Order Item Consumption"] = {
	"filters": [
		{
			"fieldname":"work_order",
			"lable":"Work Order",
			"fieldtype":"MultiSelectList",
			get_data: function(txt) {
				return frappe.db.get_link_options('Work Order', txt, {
					// project: frappe.query_report.get_filter_value("wor_order")

				});
			}
			
		}
	]
};
