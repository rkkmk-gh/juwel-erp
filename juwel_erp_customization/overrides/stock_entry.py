from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
import frappe
from frappe import _
from erpnext.stock import get_warehouse_account_map

class JGStockEntry(StockEntry):

    def get_gl_dict(self, args, account_currency=None, item=None):
        if item:
            item_code, warehouse = frappe.db.get_value('Stock Entry Detail',{"name":item.name},['item_code', 's_warehouse'])  
            stock_account = frappe.db.get_value('Item Default',{"parent":item_code, "company":self.company},'default_stock_account')
            
            if stock_account:
                warehouse_account = get_warehouse_account_map(self.company)[warehouse]["account"]
                if args["account"] == warehouse_account:
                    args["account"] = stock_account
                    account_currency = frappe.db.get_value('Account',stock_account,'account_currency')
                if args["against"] == warehouse_account: 
                    args["against"] = stock_account
        
        return super().get_gl_dict(args, account_currency, item)