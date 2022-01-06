form = document.getElementById('form');
guess = document.getElementById('guess');

form.addEventListener('submit', function(e) {
	e.preventDefault();
	guess.value = '';
});
