# Copyright (c) 2023, 8848 and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns =  get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	column = [
		
		{"label":"Work Order","fieldname":"work_order","fieldtype":"Link","options":"Work Order","width":180},
		{"label":"Plant","fieldname":"plant","fieldtype":"Data","width":200},
		{"label":"Date","fieldname":"date","fieldtype":"Date","width":200},
		{"label":"Created By","fieldname":"owner","fieldtype":"Data","width":200},
		
		{"label":"Item Code","fieldname":"item_code","fieldtype":"Data","width":150},
		{"label":"Required QTY","fieldname":"required_qty","fieldtype":"Float","width":100},
		{"label":"Transferred QTY","fieldname":"transferred_qty","fieldtype":"Float","width":100},
		{"label":"Consumed QTY","fieldname":"consumed_qty","fieldtype":"Float","width":150},
		{"label":"Warehouse","fieldname":"warehouse","fieldtype":"Data","width":200},
		
	]
	return column

def get_conditions(filters):
	conditions = ""
	if filters.get("work_order"):
		if len(filters.get("work_order")) > 1:
			wo_list = tuple(filters.get("work_order"))
			conditions += "where name in {0}".format(wo_list)
		elif len(filters.get("work_order")) == 1:
			wo = filters.get("work_order")[0]
			conditions += "where name = '{0}' ".format(wo)
	return conditions
def get_data(filters):
	rows = []
	conditions = get_conditions(filters)
	wo = frappe.db.sql(f"""select name, custom_plant as plant, owner, date(creation) as date
					from `tabWork Order` {conditions}  """,as_dict=1)
	for data in wo:
		name_count = frappe.db.sql(f"""select count(name) as name_count  from `tabWork Order Item` 
							where transferred_qty!=required_qty and parent = '{data.name}' """,as_dict=1)
		if name_count[0].name_count > 0:
			rows.append({"work_order":data.name,"date":data.date,"owner":frappe.db.get_value("User",data.owner,'full_name'),"plant":data.plant})
		wo_items = frappe.db.sql(f"""select item_code,custom_unit as uom,source_warehouse,
						(select custom_plant from `tabWork Order` where name = '{data.name}') as plant,
						required_qty as qty,consumed_qty, transferred_qty from `tabWork Order Item` where transferred_qty!=required_qty and 
						parent = '{data.name}' """,as_dict=1)
		for i in wo_items:
			# if i.get("qty") > 0:
				rows.append({
					"item_code":i.get("item_code"),
					"uom":i.get("uom"),
					"required_qty":i.get("qty"),
					"transferred_qty":i.get("transferred_qty"),
					"consumed_qty":i.get("consumed_qty"),
					"warehouse":i.get("source_warehouse"),
					"indent":1
				})
	return rows
