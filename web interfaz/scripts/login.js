var nombre = "";
var usuario = "";
var email = "";
var nacimiento = "";
var clave = "";
var reingreso_clave = "";
var direccion = "";

function mayorEdad(nacimiento){
    let añoActual = new Date().getFullYear();
    let año = new Date(nacimiento).getFullYear();
    if ((añoActual-año)>=13){
        console.log(nacimiento)}
    else{alert("Contraseña invalida")};


function verificarContraseña(clave){
    let regex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,18}$/;
    if (regex.test(clave)){
        console.log("clave valida")
    } else {
        console.log("Clave inválida. Debe tener al menos una mayúscula, un número y entre 6 y 18 caracteres.");
    }
};

        

function validarVaciosNulos(campo){
    if(campo === null || campo.length === 0){
        alert("Campo vacio")
    };
};

function guardarDatos(){
    console.log("paso");
    nombre = document.getElementById('nombre').value;
    usuario= document.getElementById('usuario').value;
    email = document.getElementById('email').value;
    nacimiento = document.getElementById('nacimiento').value;
    direccion = document.getElementById('direccion').value;
    clave = document.getElementById('clave').value;
    reingreso_clave = document.getElementById('reingreso_clave').value;
    
    validarVaciosNulos(nombre);

    if(clave != reingreso_clave){
        alert("Contraseña invalida")
    };
    console.log(nombre);
    console.log(usuario);
    console.log(email);
    console.log(nacimiento);
    console.log(direccion);
    console.log(clave);
    console.log(reingreso_clave);
};

