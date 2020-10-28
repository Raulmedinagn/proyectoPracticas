var frase = "";

document.querySelector('#boton-buscar').addEventListener('click',guardarFrase,false);

function guardarFrase(){
    frase = document.querySelector('#barra-buscar').value;
    console.log(frase);
    mostrarFrase();
}
function mostrarFrase(){
    var label = document.querySelector('#mostrar-frase');
    label.innerHTML = '';
    label.innerHTML = frase;
}



