import frappe
from frappe import _

def update_payment_type_in_so(doc, method):
    print("Updating Payment Type in Sales Order based on Delivery Note update...")
    if doc.custom_payment_type == "Bank":
        
        for row in doc.items:
            if row.against_sales_order:
                sales_order = frappe.get_doc("Sales Order", row.against_sales_order)
                sales_order.custom_payment_type = "Bank"
                sales_order.save(ignore_permissions=True)
                frappe.msgprint(_("Sales Order {0} is updated with Payment Type 'Bank'.".format(sales_order.name)),alert=1)
                
def payment_type_allow_on_submit(doc, method):
    print("FROM STREAM PC HOOK ---------------------------------------------------")
    payment_type_field_in_dn = frappe.db.exists(
					"Custom Field", {"fieldname": "custom_payment_type", "dt": "Delivery Note"}
				)
    if payment_type_field_in_dn:
        frappe.db.set_value(
            "Custom Field",
            payment_type_field_in_dn,
            "allow_on_submit",
            1
        )
        
    payment_type_field_in_so = frappe.db.exists(
                    "Custom Field", {"fieldname": "custom_payment_type", "dt": "Sales Order"}
                )
    if payment_type_field_in_so:
        frappe.db.set_value(
            "Custom Field",
            payment_type_field_in_so,
            "allow_on_submit",
            1
        )

    payment_type_field_in_si = frappe.db.exists(
                    "Custom Field", {"fieldname": "custom_payment_type", "dt": "Sales Invoice"}
                )
    if payment_type_field_in_si:
        frappe.db.set_value(
            "Custom Field",
            payment_type_field_in_si,
            "reqd",
            1
        )
    
    payment_type_field_in_pi = frappe.db.exists(
                    "Custom Field", {"fieldname": "custom_payment_type", "dt": "Purchase Invoice"}
                )
    if payment_type_field_in_pi:
        frappe.db.set_value(
            "Custom Field",
            payment_type_field_in_pi,
            "reqd",
            1
        )
    
    payment_type_field_in_pe = frappe.db.exists(
                    "Custom Field", {"fieldname": "custom_payment_type", "dt": "Payment Entry"}
                )
    if payment_type_field_in_pe:
        frappe.db.set_value(
            "Custom Field",
            payment_type_field_in_pe,
            "reqd",
            1
        )
    
    print("Migration to allow 'custom_payment_type' field on submit and make mandatory.")