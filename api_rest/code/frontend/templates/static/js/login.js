function inicioSesion(){
    var user = document.getElementById("email");
    var pass = document.getElementById("pass");
    var cantidad = pass.value.length;
    if (user.value != "" && cantidad >= 8 && pass.value != ""){ 
        var user = document.getElementById("email");
        var pass = document.getElementById("pass");
       
        
        var request = new XMLHttpRequest();
        request.open('GET', 'https://8000-yesenia19-apirest2-bisfphn4p0y.ws-us54.gitpod.io/user/validate', true);
        request.setRequestHeader("Accept", "application/json");
        request.setRequestHeader("Authorization", "Basic " + btoa(email.value + ":" + pass.value));
        request.setRequestHeader("Content-Type", "application/json");
        request.onload = () => {
                // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
                const response = request.responseText;
                const json = JSON.parse(response);

                if (request.status == 401 || request.status == 403  ) {
                    alert(json.detail);
                    
                }
                

                if (request.status == 202){
                    const response = request.responseText;
                    const json = JSON.parse(response);
                    if (request.status == 202){
                        sessionStorage.setItem("token", json.token);
                        mensaje = "Bienvenid@  " + email.value;
                        alert(mensaje);
                        window.location = "/templates/bienvenida.html";
                    }
                }
                
        };
        request.send();
    }
    else {
            swal("Oops!", "Revisa tus datos", "error");
        
        }

};

