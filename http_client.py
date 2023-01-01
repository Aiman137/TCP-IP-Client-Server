import socket

#Definimos la direccion del host y el puerto
server_address = ('localhost', 8000)
#Definimos el mensaje de la solicitud HTTP
#Solicitud GET para obtener el recurso raiz
message  = b'GET / HTTP/1.1\r\n'
#Direccion del servidor
message += b'Host: http://localhost:8000\r\n'
#Despues de enviar la solicitud cerramos la conexion
message += b'Connection: close\r\n'
message += b'\r\n'
#Creamos el socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Establecemos la conexion con el servidor
sock.connect(server_address)
#Enviamos la peticion al servidor
sock.sendall(message)

#En este bucle recibimos la respuesta del servidor
#en bloques de 1024 bytes
data = b''
while True:
    buf = sock.recv(1024)
    if not buf: #Si no queda informacion en el buffer salimos del bucle
        break
    data += buf

sock.close() #Cerramos el bucle
print(data.decode())#Decodificamos el mensaje en un formato mas entendible
