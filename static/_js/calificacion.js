// JavaScript Document
let num=document.getElementById('numero').innerHTML;
let clase=document.getElementById('imagenes');
num=parseFloat(num);
let testClass = clase.className;

if(num >=0 && num <= 1.9){
	 clase.classList.remove(testClass);
	clase.classList.add('calificados1');
	
}else if(num>1.9 && num<=2.9 ){
	 clase.classList.remove(testClass);
	clase.classList.add('calificados2');
}else if(num>2.9 && num<=3.9 ){
	 clase.classList.remove(testClass);
	clase.classList.add('calificados3');
}else if(num>3.9 && num<=4.9 ){
	 clase.classList.remove(testClass);
	clase.classList.add('calificados4');
}else{
	 clase.classList.remove(testClass);
	clase.classList.add('calificados5');
}
	
//---------------------------------------------------------------------
    let abajo =document.getElementById('btn-abajo');
	let arriba =document.getElementById('btn-arriba');
	let caja=document.getElementById('cajacomentario');
	let numeroCajas = caja.getElementsByTagName('div').length;
	document.getElementById('contador').innerHTML='Total: '+numeroCajas;
	let contador=document.getElementById('contador').innerHTML;
	contador=contador.substring(6, 100);
	arriba.style.visibility = "hidden";
	
	
function correr(id){
	  if(id==0){
		arriba.style.visibility = "visible";
		if(contador>1){
			res=numeroCajas-contador;
			contador=contador-1;
			document.getElementById('contador').innerHTML='Total: '+contador;
			 caja.getElementsByTagName('div')[res].style.display ='none';
			}else{
				if(contador>0){
				res=numeroCajas-contador;
				contador=contador-1;
				document.getElementById('contador').innerHTML='Total: '+contador;
				 caja.getElementsByTagName('div')[res].style.display ='none';
				abajo.style.visibility = "hidden";
				};
	        };
	}else{
		if(contador<numeroCajas-1){
		contador=contador+1;
        res=numeroCajas-contador;
		abajo.style.visibility = "visible";
		document.getElementById('contador').innerHTML='Total: '+contador;
		 caja.getElementsByTagName('div')[res].style.display ='block';
		 }else{
			 contador=contador+1;
        res=numeroCajas-contador;
		abajo.style.visibility = "visible";
		document.getElementById('contador').innerHTML='Total: '+contador;
		 caja.getElementsByTagName('div')[res].style.display ='block';
			 arriba.style.visibility = "hidden";
		 };
	};
	
	
};


