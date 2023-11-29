from erpnext.manufacturing.doctype.bom.bom import (
	get_bom_items_as_dict,
)
import frappe
import json
def set_required_items(self, reset_only_qty=False):
    """set required_items for production to keep track of reserved qty"""
    if not reset_only_qty:
        self.required_items = []

    operation = None
    if self.get("operations") and len(self.operations) == 1:
        operation = self.operations[0].operation

    if self.bom_no and self.qty:
        item_dict = get_bom_items_as_dict(
            self.bom_no, self.company, qty=self.qty, fetch_exploded=self.use_multi_level_bom
        )

        if reset_only_qty:
            for d in self.get("required_items"):
                if item_dict.get(d.item_code):
                    d.required_qty = item_dict.get(d.item_code).get("qty")

                if not d.operation:
                    d.operation = operation
        else:
            for item in sorted(item_dict.values(), key=lambda d: d["idx"] or float("inf")):
                self.append(
                    "required_items",
                    {
                        "rate": item.rate,
                        "amount": item.rate * item.qty,
                        "operation": item.operation or operation,
                        "item_code": item.item_code,
                        "item_name": item.item_name,
                        "unit":item.stock_uom,
                        "description": item.description, 
                        "allow_alternative_item": item.allow_alternative_item,
                        "required_qty": item.qty,
                        "source_warehouse": item.source_warehouse or item.default_warehouse,
                        "include_item_in_manufacturing": item.include_item_in_manufacturing,
                    },
                )

                if not self.project:
                    self.project = item.get("project")

        self.set_available_qty()


@frappe.whitelist()
def get_warehouse(doc, plant,item_code=None):
    rows = []
    doc = json.loads(doc)
    if doc.get("doctype") == "Work Order":
        if doc.get("required_items"):
            for i in doc.get("required_items"):
                item_group = frappe.db.get_value("Item", i.get("item_code"),'item_group')
                warehouses = frappe.db.sql(f"select default_warehouse from `tabItem Default` where parent = '{item_group}'",as_dict=1)
                warehouse_list = [j.get("default_warehouse") for j in warehouses]
                child_warehouse = frappe.db.get_value("Warehouse",{'name':['in', warehouse_list],"plant":plant},'name')
                rows.append({"item_code":i.get("item_code"),"source_warehouse":child_warehouse})
        return rows
    if doc.get("doctype") == "Material Request":
        if item_code:
            if doc.get("items"):
                    item_group = frappe.db.get_value("Item",item_code,'item_group')
                    warehouses = frappe.db.sql(f"select default_warehouse from `tabItem Default` where parent = '{item_group}'",as_dict=1)
                    warehouse_list = [j.get("default_warehouse") for j in warehouses]
                    child_warehouse = frappe.db.get_value("Warehouse",{'name':['in', warehouse_list],"plant":plant},'name')
            return child_warehouse
        else:
            for i in doc.get("items"):
                item_group = frappe.db.get_value("Item", i.get("item_code"),'item_group')
                warehouses = frappe.db.sql(f"select default_warehouse from `tabItem Default` where parent = '{item_group}'",as_dict=1)
                warehouse_list = [j.get("default_warehouse") for j in warehouses]
                child_warehouse = frappe.db.get_value("Warehouse",{'name':['in', warehouse_list],"plant":plant},'name')
                rows.append({"item_code":i.get("item_code"),"warehouse":child_warehouse})
            return rows