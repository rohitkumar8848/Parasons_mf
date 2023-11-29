import frappe

@frappe.whitelist()
def get_items(work_order):
	items = frappe.db.sql(f"""select item_code,unit as uom,source_warehouse,
						(select plant from `tabWork Order` where name = '{work_order}') as plant,
						(required_qty-transferred_qty) as qty from `tabWork Order Item` where transferred_qty!=required_qty and parent = '{work_order}' """,as_dict=1)
	return items

def on_submit(self, method=None):
	if self.work_order and self.purpose == "Material Consumption for Manufacture":
		wo = frappe.get_doc("Work Order", self.work_order)
		for i in self.items:
			frappe.db.set_value("Work Order Item",{"item_code":i.item_code,"parent":wo.get("name")},"transferred_qty",i.qty)

def on_cancel(self, method=None):
	if self.work_order and self.purpose == "Material Consumption for Manufacture":
		wo = frappe.get_doc("Work Order", self.work_order)
		for i in self.items:
			frappe.db.set_value("Work Order Item",{"item_code":i.item_code,"parent":wo.get("name")},"transferred_qty",0)
		
