// JavaScript Document
function redirigeIndex(){
	location.href="/index";
}

function myFunction(titulo='',img0="",img1="",img2="",des="no han ingresado descipción") {

	//var img=id.src;
	// var url=img.slice(41);
	// document.getElementById("modalImg").style.backgroundImage = "url('"+url+"')";
	// document.getElementById("modalImg").style.backgroundSize = "100% 100%";
	//document.getElementById("modalImg").style.backgroundRepeat = 'no-repeat'
	document.getElementById("modalImg").style.display = "block";
	document.getElementById("modalImg").style.top = '25%';
	document.getElementById("modalImg").style.transform = "translateY(0)";
    document.getElementById('imprime').innerHTML=titulo;
    document.getElementById('imgenes1').src =img0;
    document.getElementById('imgenes2').src =img1;
    document.getElementById('imgenes3').src =img2;
    document.getElementById('des').innerHTML =des;

}



