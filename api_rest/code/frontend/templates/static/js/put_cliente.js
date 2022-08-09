function putCliente(){
    let id_cliente = document.getElementById("id_cliente");
    let nombre = document.getElementById("nombre");
    let email = document.getElementById("email");
    let payload ={
        "id": id_cliente.value,
        "nombre": nombre.value,
        "email": email.value
    }
    console.log(payload)
    var token = sessionStorage.getItem('token');
    var request = new XMLHttpRequest();
    request.open('PUT', 'https://8000-yesenia19-apirest2-bisfphn4p0y.ws-us59.gitpod.io/clientes/', true);
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
                console.log(json);
                if (request.status == 202){
                    alert("Usuario actualizado")
                    window.location.replace("/bienvenida.html")
                }
            }      
    };
    request.send(JSON.stringify(payload));
};