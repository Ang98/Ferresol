function ocultar(){
    document.getElementById('mostrarOcultar').style.display="none";
}

function mostrar(){
    document.getElementById('mostrarOcultar').style.display="block";

}


function changeColor(obj) {
    if (obj.style.color == 'orange') {
        obj.style.color = 'black';
    } else {
        obj.style.color = 'orange';
    }
}
 
function changeBgColor(obj, colorName) {
    obj.style.backgroundColor = colorName;
}
 
function changeText(obj, text) {
    obj.innerText = text;
}
 
function scaleUp(obj, size) {
    obj.style.fontSize = size;
}
 


function showSixnew() {
    var element = document.getElementById("six");
     
    if(element.style.visibility == "collapse"){
        //element.style.display = "block";
        element.style.visibility = "visible";
    } else if(element.style.visibility == "visible"){
        //element.style.display = "none";
        element.style.visibility = "collapse";
    }  else{
        element.style.visibility = "hidden";
    }  
}



function hiddenSix(){
    document.getElementById('mostrarOcultars').style.display="none";
}

function showSixneww(){
    document.getElementById('mostrarOcultars').style.display="block";
}


function showSix() {
    var element = document.getElementById("six");

    if(element.style.visibility == "collapse"){
        //element.style.display = "block";
        element.style.visibility = "visible";
        document.getElementById('mostrarOcultars').style.display="block";
    } else if(element.style.visibility == "visible"){
        //element.style.display = "none";
        element.style.visibility = "collapse";
        document.getElementById('mostrarOcultars').style.display="none";
    }
}


function  evaluarCantidad(form){
    if(form.cantidad.value<1){
        form.cantidad.value=1;
        alert("solo se puede comprar minimo 1 producto")
    }
    if(form.cantidad.value>5){
        form.cantidad.value=5;
        alert("la cantida maxima a comprar es de 5")
    }

}


function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
  }
  
function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
}












































































































