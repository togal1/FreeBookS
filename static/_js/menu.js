// JavaScript Document
let estado1 = document.getElementById('menu1');
let estado2 = document.getElementById('menu2');
estado1.style.display = 'none';
estado2.style.display = 'none';

function menu(id) {

	if (id == 1) {
		if (estado1.style.display == 'none') {
			estado1.style.display = 'block';
			document.getElementsByTagName('span')[0].innerHTML = '🔻';
		} else {
			estado1.style.display = 'none';
			document.getElementsByTagName('span')[0].innerHTML = '🔺';
		}

	}
	if (id == 2) {

		if (estado2.style.display == 'none') {
			estado2.style.display = 'block';
			document.getElementsByTagName('span')[1].innerHTML = '🔻';
		} else {
			estado2.style.display = 'none';
			document.getElementsByTagName('span')[1].innerHTML = '🔺';
		}

	}
}

//----------------------------------------------------------------------
function menuBar() {
	let clase = document.getElementById('caja-contenedora');
	let texto = document.getElementsByClassName('menu-bar')[0];
	let estado1 = document.getElementById('menu1');
	let estado2 = document.getElementById('menu2');
	if (clase.classList.contains('abrir')) {
		clase.classList.remove('abrir');
		texto.innerHTML = '☑';
		document.getElementsByTagName('span')[0].innerHTML = '🔺';
		document.getElementsByTagName('span')[1].innerHTML = '🔺';

	} else {
		clase.classList.add('abrir');
		texto.innerHTML = '☐';
		estado1.style.display = 'none';
		estado2.style.display = 'none';


	}
}


