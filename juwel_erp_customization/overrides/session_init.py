import frappe
from frappe import _

def set_session_defaults(login_manager):
    try:
        base_account = frappe.db.get_value('Company',frappe.defaults.get_user_default('Company') ,'default_base_account')
        print(frappe.defaults.get_user_default('Company'))
        print(base_account)
        if base_account:
            frappe.defaults.set_user_default('base_account', base_account)
    except:
        pass

    