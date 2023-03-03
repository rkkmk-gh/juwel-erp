from erpnext.stock.doctype.delivery_note.delivery_note import DeliveryNote
from .gl_utils import update_gl_dict

class JGDeliveryNote(DeliveryNote):

    def get_gl_dict(self, args, account_currency=None, item=None):
        if item:
            update_gl_dict(args, account_currency, item, self.company)        
            return super().get_gl_dict(args, account_currency, item)