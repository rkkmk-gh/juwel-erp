from erpnext.stock.doctype.purchase_receipt.purchase_receipt import PurchaseReceipt
from .gl_utils import update_gl_dict

class JGPurchaseReceipt(PurchaseReceipt):

    def get_gl_dict(self, args, account_currency=None, item=None):

        update_gl_dict(args, account_currency, item, self.company)        
        return super().get_gl_dict(args, account_currency, item)