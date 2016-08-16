function onClickMenu() {
	$("#main-sidebar")
		.sidebar('setting', 'transition', 'overlay')
		.sidebar('toggle');
}

$(document).ready(function() {
	$("#table-of-contents").toc({
		'selectors': 'h1,h2,h3',
		'prefix': 'toc'
	});

	$("#toggle-toc").on('click', function() {
		$("#toc-sidebar")
			.sidebar('setting', 'transition', 'overlay')
			.sidebar('toggle');
	});

	$("#table-of-contents a").on('click', function() {
		$("#toc-sidebar").sidebar('toggle');
	});
});