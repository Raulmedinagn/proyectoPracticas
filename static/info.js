alert("JSON cargado");
var frase = "";

document.querySelector('#boton-buscar').addEventListener('click',guardarFrase);

function guardarFrase(){
    frase = documentquerySelector('#barra-buscar').value;

    console.log(frase);
}



