import frappe
from frappe import _

def update_gl_dict(args, account_currency=None, item=None, company=None):

    if args["remarks"] != "Rounding gain/loss Entry for Stock Transfer":
        if item:
            stock_account = frappe.db.get_value('Item Default',{"parent":item.item_code, "company":company},'default_stock_account')
            if stock_account:
                account_currency = frappe.db.get_value('Account',stock_account,'account_currency')
                if args["debit"] < 0:
                    args["account"] = stock_account
                else: 
                    args["against"] = stock_account