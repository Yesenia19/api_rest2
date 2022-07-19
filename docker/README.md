# API-REST
API-REST

## crear la imagen del docker
'''bash
docker build -t api_rest:10.06.22 .
'''

## crear un contenedor
'''bash
docker run -it -v /workspace/api_rest2/api_rest:/home/api_rest --net=host --name api_rest -h api_rest api_rest:18.07.22
'''

## ver contenedores
'''bash
docker ps -a
'''

## eliminar contenedor
'''bash
docker rm
'''

## eliminar imagen
'''bash
docker rmi
'''

## ver todos los contenedores
'''bash
docker ps -a
'''


## ver todas las imagenes
'''bash
docker images
'''

## parar un contenedor
'''bash
docker stop f4968afc0253
'''