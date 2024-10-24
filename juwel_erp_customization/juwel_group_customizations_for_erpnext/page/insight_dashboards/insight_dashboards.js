frappe.pages['insight_dashboards'].on_page_load = function (wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Insights',
		single_column: true
	});

	let vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0)
	let vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)
	const queryString = window.location.search;
	const urlParams = new URLSearchParams(queryString);
	const dashboard = urlParams.get("dashboard");

	document.querySelector('.page-head').remove();
	page.main.append('<iframe scrolling="no" style="width: ' + vw + 'px; border: none;margin: 0;padding: 0;overflow: hidden;z-index: 999999;height: ' + vh + 'px;" src="https://jg-insights.keenconsults.com/superset/dashboard/' + dashboard + '/?standalone=true"></iframe>');
	//document.getElementByClassName("page-head-content").remove();
}
