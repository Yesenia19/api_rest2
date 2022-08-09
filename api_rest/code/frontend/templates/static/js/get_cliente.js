function getCliente() {
    //Accede a la session de la pagina
    var id = window.location.search.substring(1);
    

    var token = sessionStorage.getItem('token');

    var request = new XMLHttpRequest();

    request.open('GET', 'https://8000-yesenia19-apirest2-bisfphn4p0y.ws-us59.gitpod.io/clientes/'+ id, true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + token);
    request.setRequestHeader("Content-Type", "application/json");

    
    request.onload = () => {
            // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente

            if (request.status === 401 || request.status === 403) {
                alert(json.detail);
            }
            else if (request.status == 202){
                const response = request.responseText;
                const json = JSON.parse(response);
                let id_cliente = document.getElementById("id_cliente");
                let nombre = document.getElementById("nombre");
                let email = document.getElementById("email");
                id_cliente.value = json.id_cliente;
                nombre.value =json.nombre;
                email.value =json.email;
            }

            else if(request.status == 404){
                let id_cliente =document.getElementById("id_cliente");
                let nombre =document.getElementById("nombre");
                let email =document.getElementById("email");
                id_cliente.value = "No encontrado";
                nombre.value = "No encontrado";
                email.value = "No encontrado";
                alert(json.detail);
            }
    };
    request.send();
};