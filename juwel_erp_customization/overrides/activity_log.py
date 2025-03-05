import frappe
from frappe import _

from frappe.desk.query_report import run
from frappe.core.doctype.access_log.access_log import make_access_log

@frappe.whitelist()
@frappe.read_only()
def recorded_report_run(
	report_name,
	filters=None,
	user=None,
	ignore_prepared_report=False,
	custom_columns=None,
	is_tree=False,
	parent_field=None,
	are_default_filters=True,
):
    result = run(report_name, filters, user, ignore_prepared_report, custom_columns, is_tree, parent_field, are_default_filters)
    make_access_log(method='frappe.desk.query_report.run', report_name=report_name, filters=filters)
    return result
