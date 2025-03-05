import frappe
from frappe import _

def before_file_delete(doc, method=None):
    if doc.doctype == "File" and doc.attached_to_doctype and doc.attached_to_name:
        docstatus = frappe.db.get_value(doc.attached_to_doctype, doc.attached_to_name, 'docstatus')
        if docstatus == 1 or docstatus == 2:      
            frappe.throw(_("Cannot delete file attached to a submitted or cancelled document."))
