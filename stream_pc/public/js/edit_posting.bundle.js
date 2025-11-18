

$(document).on("form-refresh", function (event, frm) {  
    console.log("FROM STREAM PC")
    if (frappe.meta.has_field(frm.doc.doctype, "set_posting_time") && frm.is_new()) {
            console.log("--------has field-----------")
            setTimeout(() => {
				frm.doc.set_posting_time = 1;
                frm.refresh_field("set_posting_time");
            }, 500);
        }
})