import socket


# Define socket host and port
SERVER_HOST = socket.gethostname()
SERVER_PORT = 8000

# Create socket
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mi_socket.bind((SERVER_HOST, SERVER_PORT))
mi_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)
print("Trying to connect at, http://localhost/8000")
while True:    
    # Wait for client connections
    client_connection, client_address = mi_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    fin = open('htdocs/index.html') 
    content = fin.read()
    fin.close()
    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()
