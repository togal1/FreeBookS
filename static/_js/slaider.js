//--------------variables------------------------------
let silder = document.getElementById('slaider');
let numero = silder.getElementsByTagName('img').length;
let next = document.getElementById('btn-next');
let prev = document.getElementById('btn-prev');
let imagenes = new Array(numero)
let b = 0;
let num = 0;
//cuento las imagenes y despúes modifico el css para lograr el porcentaje necesario-----------------------
silder.style.width = numero + "00%";
//-------------le doy un valor a cada imagen multiplo de 100----------------------
for (i = 0; i < numero; i++) {
	imagenes[i] = b;
	b += 100;
}


//-------detecta que navegador tengo-------------------------
function navegador() {
	let agente = window.navigator.userAgent;
	let navegadores = ["Chrome", "Firefox", "Safari", "Opera", "Trident", "MSIE", "Edge"];
	for (let i in navegadores) {
		if (agente.indexOf(navegadores[i]) != -1) {
			return navegadores[i];
		}
	}
}
let browser = document.getElementById("navegador");
window.onload = function () {
	if (navegador() == "Trident") {
		document.getElementsByTagName('header')[0].style.backgroundColor = "#8A4A87";
	}
}


//---------boton izquierdo ---------------------- 
function botonPrev() {
	num -= 1;
	silder.style.marginLeft = '-' + imagenes[num] + '%';

	if (num <= 0) {
		prev.style.visibility = "hidden";

	} else {
		next.style.visibility = "visible";

	}

	return num;

}

//------------boton derecho------------------------------

function botonNext() {
	num += 1;
	silder.style.marginLeft = '-' + imagenes[num] + '%';

	if (num >= imagenes.length) {
		next.style.visibility = "hidden";

	} else {
		prev.style.visibility = "visible";

	}
	return num;

}

//------------------------------------------------




function cerrar() {
	document.getElementById("modalImg").style.display = "none";
}

//****************modalImagne----------------------------

function MasLibros(id) {
	if (id == 1) {
		document.getElementById("subirLibros").style.display = "block";
	} else {
		document.getElementById("subirLibros").style.display = "none";
		
	}
}
