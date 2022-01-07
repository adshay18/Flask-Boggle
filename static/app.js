form = document.getElementById('form');
$guess = $('#guess');

function displayMessage(msg) {
	$('.msg').text(msg);
}

form.addEventListener('submit', async function(e) {
	e.preventDefault();
	let word = $guess.val();
	const res = await axios.get('/validate-word', { params: { word: word } });

	if (res.data.result === 'not-word') {
		displayMessage(`'${word}' is not a real word.`);
	}
	if (res.data.result === 'not-on-board') {
		displayMessage(`'${word}' is not on this board.`);
	}
	if (res.data.result === 'ok') {
		displayMessage(`'${word}' was accepted.`);
	}
	guess.value = '';
});
