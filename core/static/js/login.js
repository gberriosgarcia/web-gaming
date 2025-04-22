window.onload = function() {
    document.getElementById('btnGuardarDatos').setAttribute("disabled","disabled");
};

function verificarEmail(email) {
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!emailRegex.test(email)){
        alert("El formato del e-mail no es válido.");
    };
}

function validarCampos(){
    if(
        firstName.value === null || firstName.value.length === 0 
        || lastName.value === null || lastName.value.length === 0
        || username.value === null || username.value.length === 0
        || email.value === null || email.value.length === 0
        || password.value === null || password.value.length === 0
        || password2.value === null || password2.value.length === 0
    ){
        document.getElementById('btnGuardarDatos').setAttribute("disabled","disabled");
    }
    else{
        document.getElementById('btnGuardarDatos').removeAttribute("disabled");
        verificarEmail(email.value);
    }
};

function borrarDatosFormulario(){
    document.getElementById("formRegistro").reset();
}
