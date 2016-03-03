document.addEventListener('keydown', function(event) {
	if (!$('input').is(':focus')) {
		if(event.keyCode == 65) {
			window.location.href = '/wiki/random';
		}
	}
});