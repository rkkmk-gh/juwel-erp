
async function embedDashboard (
	dashboardName,
	supersetDomain,
	mountPoint
) {
	const urlParamsString = "?standalone=true"

	if (supersetDomain.endsWith("/")) {
		supersetDomain = supersetDomain.slice(0, -1);
	}

	async function mountIframe () {
		const iframe = document.createElement('iframe');
		window.addEventListener('message', function (event) {
			// Check if the message is from the expected iframe origin
			//if (event.origin === 'https://jg-insights.keenconsults.com') {
			const { width, height } = event.data;

			// Use the dimensions to adjust the iframe size or other elements
			iframe.style.width = width + 'px';
			iframe.style.height = height + 'px';
			//}
		});


		iframe.src = `${supersetDomain}/superset/dashboard/${dashboardName}${urlParamsString}`;
		//iframe.title = iframeTitle;
		mountPoint.replaceChildren(iframe);
	}

	mountIframe();

}

frappe.pages['insight_dashboards'].on_page_load = function (wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Insights',
		single_column: true
	});

	embedDashboard("tar_due", "https://jg-insights.keenconsults.com", document.getElementById("body"))

}
