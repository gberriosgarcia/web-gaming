window.onload = function() {
    document.getElementById('btnGuardarDatos').setAttribute("disabled","disabled");
};

function verificarEdad(nacimiento){
    let añoActual = new Date().getFullYear();
    let año = new Date(nacimiento).getFullYear();
    if ((añoActual-año)<13){
        alert("Debes tener al menos 13 años para registrarte en el sitio.")
    };
};

function verificarContraseña(clave, reingreso_clave){
    if(clave != reingreso_clave){
        alert("Las contraseñas no son iguales.")
    }
    else{
        let regex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,18}$/;
        if (!regex.test(clave)){
            console.log("Clave inválida. Debe tener al menos una mayúscula, un número y entre 6 y 18 caracteres.");
        }
    }
};

function validarVaciosNulos(){
    if(
        nombre.value === null || nombre.value.length === 0 
        || usuario.value === null || usuario.value.length === 0
        || email.value === null || email.value.length === 0
        || clave.value === null || clave.value.length === 0
        || reingreso_clave.value === null || reingreso_clave.value.length === 0
    ){
        document.getElementById('btnGuardarDatos').setAttribute("disabled","disabled");
    }
    else{
        document.getElementById('btnGuardarDatos').removeAttribute("disabled");
    }
};

function verificarEmail(email) {
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!emailRegex.test(email)){
        alert("El formato del e-mail no es válido.");
    };
 }

function guardarDatos(){
    verificarEdad(nacimiento.value);
    verificarEmail(email.value);
    verificarContraseña(clave.value, reingreso_clave.value);
};

function borrarDatosFormulario(){
    document.getElementById("formRegistro").reset();
}