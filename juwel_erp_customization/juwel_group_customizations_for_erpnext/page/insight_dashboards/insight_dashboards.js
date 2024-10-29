async function embedDashboard (
	dashboardName,
	supersetDomain,
	mountPoint
) {
	const urlParamsString = "?standalone=true"
	console.log("superset domain", supersetDomain)
	if (supersetDomain.endsWith("/")) {
		supersetDomain = supersetDomain.slice(0, -1);
	}

	async function mountIframe () {
		const iframe = document.createElement('iframe');

		// add the event listener before setting src, to be 100% sure that we capture the load event
		iframe.addEventListener('load', () => {
			// MessageChannel allows us to send and receive messages smoothly between our window and the iframe
			// See https://developer.mozilla.org/en-US/docs/Web/API/Channel_Messaging_API
			const commsChannel = new MessageChannel();
			const ourPort = commsChannel.port1;
			const theirPort = commsChannel.port2;

			ourPort.onmessage = onMessage;

			// Send one of the message channel ports to the iframe to initialize embedded comms
			// See https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage
			// we know the content window isn't null because we are in the load event handler.
			iframe.contentWindow.postMessage(
				{ type: "__embedded_comms__", handshake: "port transfer" },
				supersetDomain,
				[theirPort],
			);
		});

		iframe.src = `${supersetDomain}/superset/dashboard/${dashboardName}${urlParamsString}`;
		//iframe.title = iframeTitle;
		mountPoint.replaceChildren(iframe);
	}

	const [ourPort] = await Promise.all([
		mountIframe(),
	]);

	function unmount () {
		mountPoint.replaceChildren();
	}

	const getScrollSize = () => ourPort.get('getScrollSize');

	function onMessage (e) {
		console.log(e.data);
	}

	return {
		getScrollSize,
		unmount,
	};
}

frappe.pages['insight_dashboards'].on_page_load = function (wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Insights',
		single_column: true
	});

	document.querySelector('.page-head').remove();
	//page.main.append('<iframe id="myIframe" scrolling="no" src="https://jg-insights.keenconsults.com/superset/dashboard/' + dashboard + '/?standalone=true"></iframe>');

	page.main.append('<script type="module" src="https://unpkg.com/@superset-ui/switchboard@0.20.2/lib/switchboard.js"></script>');
	embedDashboard("tar_due", "https://jg-insights.keenconsults.com", document.getElementById("body"))

}
