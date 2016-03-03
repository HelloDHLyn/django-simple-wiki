function onClickMenu() {
	$('.ui.sidebar')
	  .sidebar('setting', 'transition', 'overlay')
	  .sidebar('toggle')
	;
}

document.addEventListener('keydown', function(event) {
	if(event.keyCode == 65) {
		window.location.href = '/wiki/random';
	}
});