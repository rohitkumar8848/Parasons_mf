# Copyright (c) 2023, Extension and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns =  get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	column = [
		
		{"label":"Supplier","fieldname":"supplier","fieldtype":"Link","options":"Supplier","width":180},
		{"label":"Supplier Name","fieldname":"supplier_name","fieldtype":"Data","width":200},
		{"label":"Plant","fieldname":"plant","fieldtype":"Data","width":80},
		{"label":"Item Code","fieldname":"item_code","fieldtype":"Data","width":100},
		{"label":"UOM","fieldname":"uom","fieldtype":"Data","width":100},
		{"label":"Rate","fieldname":"rate","fieldtype":"Currency","width":80},
		{"label":"Stock Qty","fieldname":"qty","fieldtype":"Float","width":80},
		{"label":"Total Value","fieldname":"amount","fieldtype":"Currency","width":100},
	]
	return column

def get_conditions(filters):
	conditions = ""
	if filters.get("supplier"):
		conditions += f"where s.supplier = '{filters.get('supplier')}' "
	if filters.get("plant"):
		conditions += f" and s.plant = '{filters.get('plant')}' "
	
def get_data(filters):
	rows = []
	conditions = get_conditions(filters)

	order_data = frappe.db.sql(f"""select si.item_code,si.item_name, s.supplier,si.stock_uom, 
							s.supplier_name, s.plant, si.qty, si.rate, si.amount, s.name from `tabSubcontracting Order` s 
							left join `tabSubcontracting Order Item` si on si.parent = s.name {conditions}""",as_dict=1)
	receipt_data = frappe.db.sql(f"""select si.item_code, si.item_name, s.supplier,si.stock_uom,
							s.supplier_name, s.plant, si.qty, si.rate, si.amount, s.subcontracting_order from `tabSubcontracting Receipt` s 
							left join `tabSubcontracting Receipt Item` si on si.parent = s.name {conditions}""",as_dict=1)
	for i in order_data:
		for j in receipt_data:
			if i.get("name") == j.get("subcontracing_name") and i.get("item_code") == j.get("item_code"):
				rows.append({
					"supplier":i.get("supplier"),
					"supplier_name":i.get("supplier_name"),
					"plant":i.get("plant"),
					"item_code":i.get("item_code"),
					"uom":i.get("uom"),
					"qty":i.get("qty")-j.get("qty"),
					"rate": i.get("rate"),
					"amount":(i.get("qty")-j.get("qty")) * i.get("rate")
				})
	
	return rows
