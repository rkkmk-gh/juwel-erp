import frappe
from frappe import _
from erpnext.stock import get_warehouse_account_map

def update_gl_dict(args, account_currency=None, item=None, company=None, warehouse_account=None):

    if args["remarks"] != "Rounding gain/loss Entry for Stock Transfer":
        if item:
            stock_account = frappe.db.get_value('Item Default',{"parent":item.item_code, "company":company},'default_stock_account')
            if stock_account:
                warehouse_account = get_warehouse_account_map(company)[item.warehouse]["account"]
                if args["account"] == warehouse_account:
                    args["account"] = stock_account
                    account_currency = frappe.db.get_value('Account',stock_account,'account_currency')
                if args["against"] == warehouse_account: 
                    args["against"] = stock_account