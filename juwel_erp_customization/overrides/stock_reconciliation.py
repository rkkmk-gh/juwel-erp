from erpnext.stock.doctype.stock_reconciliation.stock_reconciliation import StockReconciliation
import frappe
from frappe import _
from .gl_utils import update_gl_dict

class JGStockReconciliation(StockReconciliation):

    def get_gl_dict(self, args, account_currency=None, item=None):
        if item:
            item_code = frappe.db.get_value('Stock Reconciliation Item',{"name":item.name},'item_code')
            stock_account = frappe.db.get_value('Item Default',{"parent":item_code, "company":self.company},'default_stock_account')

            if stock_account:
                if args.get('credit') > 0:
                    args['account'] = stock_account
                else:
                    args['against'] = stock_account
                    
        return super().get_gl_dict(args, account_currency, item)