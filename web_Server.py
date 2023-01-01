import socket

# Host local
SERVER_HOST = '127.0.0.1'
#Puerto de escucha del servidor
SERVER_PORT = 8000 

# Creamos el socket
# Especificamos la IPv4 y el protocolo TCP
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
mi_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Asignamos los recursos
mi_socket.bind((SERVER_HOST, SERVER_PORT)) 
#Escuchamos y aceptamos como maximo una peticion
mi_socket.listen(1) 
print('Escuchando el puerto %s ...' % SERVER_PORT)
print("Intentando connectar a, http://localhost/8000")
while True:    
    # Esperamos a que el cliente se conecte
    client_connection, client_address = mi_socket.accept()
    # Miramos la peticion del cliente
    request = client_connection.recv(1024).decode()
    print(request)
    # Leemos el archivo HTML
    fin = open('htdocs/index.html') 
    content = fin.read()
    fin.close()
    # Enviamos una respuesta al cliente con el contenido HTML
    response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close() #Cerramos la conexion

# Close socket
server_socket.close()
