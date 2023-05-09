from erpnext.stock.doctype.stock_reconciliation.stock_reconciliation import StockReconciliation
from .gl_utils import update_gl_dict

class JGStockReconciliation(StockReconciliation):

    def get_gl_dict(self, args, account_currency=None, item=None):
        if item:
            update_gl_dict(args, account_currency, item, self.company)        
            return super().get_gl_dict(args, account_currency, item)