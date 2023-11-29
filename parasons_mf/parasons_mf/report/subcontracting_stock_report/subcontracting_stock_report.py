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
		{"label":"Plant","fieldname":"plant","fieldtype":"Data","width":150},
		{"label":"Item Code","fieldname":"item_code","fieldtype":"Data","width":100},
		{"label":"UOM","fieldname":"uom","fieldtype":"Data","width":100},
		{"label":"Stock Qty","fieldname":"qty","fieldtype":"Float","width":150},
		{"label":"Rate","fieldname":"rate","fieldtype":"Currency","width":150},
		{"label":"Total Value","fieldname":"amount","fieldtype":"Currency","width":150},
	]
	return column

def get_conditions(filters):
	conditions = ""
	plant = filters.get("plant")
	supplier = filters.get("supplier")
	if supplier and plant:
		conditions += f" where s.supplier = '{supplier}' and s.plant='{plant}' "
	if plant and not supplier: 
		conditions += f" where s.plant = '{plant}' "
	if supplier and not plant:
		conditions += f" where s.supplier = '{supplier}' "
	return conditions
def get_data(filters):
	rows = []
	grand_total = 0
	total_qty = 0
	conditions = get_conditions(filters)

	order_data = frappe.db.sql(f"""select si.item_code, si.item_name, s.supplier, si.stock_uom, 
							s.supplier_name, s.plant, si.qty, si.rate, si.amount, s.name from `tabSubcontracting Order` s 
							left join `tabSubcontracting Order Item` si on si.parent = s.name {conditions} """,as_dict=1)
	receipt_data = frappe.db.sql(f"""select si.item_code, si.item_name, s.supplier,si.stock_uom,
							s.supplier_name, s.plant, si.qty, si.rate, si.amount, s.subcontracting_order from `tabSubcontracting Receipt` s 
							left join `tabSubcontracting Receipt Item` si on si.parent = s.name {conditions} """,as_dict=1)
	for i in order_data:
		for j in receipt_data:
			if i.get("name") == j.get("subcontracting_order") and i.get("item_code") == j.get("item_code"):
				stock_qty=i.get("qty")-j.get("qty")
				if stock_qty > 0:
					rows.append({
						"supplier":i.get("supplier"),
						"supplier_name":i.get("supplier_name"),
						"plant":i.get("plant"),
						"item_code":i.get("item_code"),
						"uom":i.get("stock_uom"),
						"qty":stock_qty,
						"rate": i.get("rate"),
						"amount":stock_qty * i.get("rate")
					})
					grand_total += stock_qty * i.get("rate")
					total_qty += stock_qty
	if rows:
		rows.append({"supplier":"Grand Total","qty":total_qty,"amount":grand_total})
	return rows
