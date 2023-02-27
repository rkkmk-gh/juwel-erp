import frappe
from frappe import _
from erpnext.stock.doctype.delivery_note.delivery_note import DeliveryNote


class JGDeliveryNote(DeliveryNote):

    def get_gl_dict(self, args, account_currency=None, item=None):

        if args["remarks"] != "Rounding gain/loss Entry for Stock Transfer":
            if item:
                stock_account = frappe.db.get_value('Item Default',{"parent":item.item_code, "company":self.company},'default_stock_account')
                if stock_account:
                    account_currency = frappe.db.get_value('Account',stock_account,'account_currency')
                    if args["debit"] < 0:
                        args["against"] = stock_account
                    else: 
                        args["account"] = stock_account
        
        return super().get_gl_dict(args, account_currency, item)
