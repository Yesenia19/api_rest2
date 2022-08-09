var id =window.location.search.substring(1);

let id_cliente = document.getElementById("id_cliente");

id_cliente.value = id;

function deleteCliente(){
    let id_cliente = document.getElementById("id_cliente");
    let nombre = document.getElementById("nombre");
    let email = document.getElementById("email");

    console.log(nombre.value);
    console.log(email.value);
    var token = sessionStorage.getItem('token');
    var request = new XMLHttpRequest();
    request.open('DELETE', 'https://8000-yesenia19-apirest2-bisfphn4p0y.ws-us59.gitpod.io/clientes/'+ id_cliente.value, true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + token)
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
                    alert("Usuario eliminado")
                    window.location.replace("/bienvenida.html")
                }
            }
            

            
    };
    request.send();
};