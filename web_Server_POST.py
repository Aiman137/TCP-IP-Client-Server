import socket

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)
print("Trying to connect at, http://localhost/8000")
while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Check if the request is a POST or PUT request
    if request.startswith("POST") or request.startswith("PUT"):
        # Split the request into separate lines
        lines = request.split("\n")

        # Get the content length from the request headers
        for line in lines:
            if line.startswith("Content-Length:"):
                content_length = int(line.split(":")[1].strip())

        # Read the content of the request from the socket
        content = client_connection.recv(content_length).decode()

        # Save the content to a file
        with open("htdocs/index.html", "w") as fout:
            fout.write(content)

        # Send HTTP response
        response = 'HTTP/1.0 200 OK\n\n' + content
    else:
        # Send HTTP response with the contents of the index.html file
        with open("htdocs/index.html") as fin:
            content = fin.read()
        response = 'HTTP/1.0 200 OK\n\n' + content

    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()

