// JavaScript Document

function previsulizar(id) {
    let leer = new FileReader();
    leer.readAsDataURL(document.getElementById('img'+id).files[0]);
    leer.onload = function (e) {
        document.getElementById('cargar'+id).src = e.target.result;
    };
}
//---------------------------------------------------------------------
function marcar(master, cn) {
	var clase = document.getElementsByClassName(cn);
	for (i = 0; i < clase.length; i++) {
		let cd = document.getElementById(clase[i].id);
		cd.checked = master.checked;

	}
}

//---------------------------------------------------------------------
function borrarUno(id){
	let checkBox = document.getElementById(id);
	let numero=id.substring(4, 100);
// If the checkbox is checked, display the output text
  if (checkBox.checked == true){
       location.href="/delete/"+numero;
  } else {

  }

}

function borrarDos(id){
	let checkBox = document.getElementById(id);
	let numero=id.substring(4, 100);
// If the checkbox is checked, display the output text
  if (checkBox.checked == true){
       location.href="/delete2/"+numero;
  } else {

  }

}
let img=document.getElementById('img0');
let nom=document.getElementById('nom1');
let nom2=document.getElementById('nom2');
let ape1=document.getElementById('ape1');
let ape2=document.getElementById('ape2');
let cumple=document.getElementById('cumple');
let pais=document.getElementById('pais');
let dep=document.getElementById('dep');
let loc =document.getElementById('loc');
let dir=document.getElementById('dir');
let num=document.getElementById('num');
let apto=document.getElementById('apto');
let cp=document.getElementById('cp');
let prefijo=document.getElementById('prefijo');
let cel1=document.getElementById('cel1');
let cel2=document.getElementById('cel2');
let email=document.getElementById('email');

function validacion(){
	let error=document.getElementById('error');
	let bandera=1;

if (img.value=='' && nom2.value=='' && ape2.value=='' && cumple.value=='' && pais.value=='' && dep.value=='' && loc.value=='' &&
	    dir.value=='' && num.value=='' && apto.value=='' && cp.value=='' && prefijo.value=='' && cel1.value=='' && cel2.value=='' && email.value=='' ){
		 bandera=0;
	}
 switch(bandera){
	 case 0:
	         error.innerHTML="No ingresó ningún dato";
	         return false;
	 break;
	 case 1:
	        return true;
	 break;
 }


}

