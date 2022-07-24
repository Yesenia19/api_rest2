function crearUsuario(){
    var user = document.getElementById("email");
    var pass1 = document.getElementById("pass1");
    var pass2 = document.getElementById("pass2");
    var cantidad = pass1.value.length;
    if (user.value != "" && cantidad >= 8 && pass1.value == pass2.value){ 
        var user = document.getElementById("email");
        var pass1 = document.getElementById("pass1");
        var pass2 = document.getElementById("pass2");
        var datos = {
            "email": user.value,
            "password": pass2.value
        }
        var request = new XMLHttpRequest();
        request.open('POST', 'https://8000-yesenia19-apirest2-bisfphn4p0y.ws-us54.gitpod.io/user/', true);
        request.setRequestHeader("Accept", "application/json");
        request.setRequestHeader("Content-Type", "application/json");
        request.onload = () => {
                // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
                const response = request.responseText;
                const json = JSON.parse(response);

                if (request.status == 403  ) {
                    alert(json.detail);
                    
                }
                if(request.status == 401 ){
                    swal("Oops!", "El usuario ya existe, intenta con otro", "error"); 
                }

                if (request.status == 202){
                    const response = request.responseText;
                    const json = JSON.parse(response);
                    if (request.status == 202){
                        alert("Felicidades! Tu usuario a sido agregado con exito. Ya puedes iniciar sesión!");
                        window.location = "/templates/";

                    }
                }
                
        };
        request.send(JSON.stringify(datos));
    }
    else {
            swal("Oops!", "Revisa tus datos", "error");
        
        }
        if (pass1.value != pass2.value){
            swal("Oops!", "Tus passwords no coinciden", "error");
        }
};

