frappe.ui.form.on("Work Order",{
before_save(frm){
    set_warehouse(frm)
},
plant(frm){
    set_warehouse(frm)
}
})
function set_warehouse(frm){
    if (frm.doc.required_items.length){
        frappe.db.get_value("Warehouse",{"plant":frm.doc.plant},"name").then((r) => {
            console.log(r.message.name)
            frm.doc.required_items.forEach(i => {
                i.source_warehouse = r.message.name
            })
            frm.refresh_field("required_items")
        })
        
        
    }
}