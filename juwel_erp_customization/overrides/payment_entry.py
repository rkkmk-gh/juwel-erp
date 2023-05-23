from erpnext.accounts.doctype.payment_entry.payment_entry import PaymentEntry
from frappe.utils import flt

class JGPaymentEntry(PaymentEntry):
	def __init__(self, *args, **kwargs):
		super(JGPaymentEntry, self).__init__(*args, **kwargs)

	#def calculate_taxes(self):
	#	super().calculate_taxes()
	#	#tax is always in company currency
	#	self.total_taxes_and_charges = self.base_total_taxes_and_charges

	def set_amounts_after_tax(self):
		applicable_tax = 0
		base_applicable_tax = 0
		for tax in self.get("taxes"):
			if not tax.included_in_paid_amount:
				amount = -1 * tax.tax_amount if tax.add_deduct_tax == "Deduct" else tax.tax_amount
				base_amount = (
					-1 * tax.base_tax_amount if tax.add_deduct_tax == "Deduct" else tax.base_tax_amount
				)

				applicable_tax += amount
				base_applicable_tax += base_amount

		self.paid_amount_after_tax = flt(
			flt(self.paid_amount) + flt(applicable_tax), self.precision("paid_amount_after_tax")
		)

		self.base_paid_amount_after_tax = flt(
			flt(self.paid_amount_after_tax) * flt(self.source_exchange_rate),
			self.precision("base_paid_amount_after_tax"),
		)

		self.received_amount_after_tax = flt(
					flt(self.received_amount) + flt(applicable_tax), self.precision("paid_amount_after_tax")
					)
		
		self.base_received_amount_after_tax = flt(
			flt(self.received_amount_after_tax) * flt(self.target_exchange_rate),
			self.precision("base_paid_amount_after_tax"),
		)

		payment_account_currency = self.paid_to_account_currency if self.payment_type == "Pay" else self.paid_from_account_currency

		#tax is always in company currency
		if self.company_currency != payment_account_currency:
			self.paid_amount_after_tax = flt(
				flt(self.paid_amount) + flt(applicable_tax / self.source_exchange_rate), self.precision("paid_amount_after_tax")
			)

			self.received_amount_after_tax = flt(
				flt(self.received_amount) + flt(applicable_tax / self.target_exchange_rate), self.precision("received_amount_after_tax")
			)			
				
			self.base_paid_amount_after_tax = flt(
				flt(self.paid_amount_after_tax) * flt(self.source_exchange_rate),
					self.precision("base_paid_amount_after_tax"),
				)
				
			self.base_received_amount_after_tax = flt(
				flt(self.received_amount_after_tax) * flt(self.target_exchange_rate),
				self.precision("base_paid_amount_after_tax"),
				)
		
				