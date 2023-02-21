from erpnext.stock.doctype.delivery_note import DeliveryNote

class JGDeliveryNote(DeliveryNote):
    def get_gl_dict(self, args, account_currency=None, item=None):
        if item and item.stock_account:
            args.account = item.stock_account
        
        super.get_gl_doct(self, args, account_currency, item)