from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
from .gl_utils import update_gl_dict

class JGStockEntry(StockEntry):

    def get_gl_dict(self, args, account_currency=None, item=None):
        update_gl_dict(args, account_currency, item, self.company)        
        return super().get_gl_dict(args, account_currency, item)