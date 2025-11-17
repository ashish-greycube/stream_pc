import frappe
from frappe import _

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