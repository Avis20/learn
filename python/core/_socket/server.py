import socket

HOST, PORT = '', 8000


def handle_request(request: bytes) -> bytes:
    request_data = request.decode()
    http_response = f"HTTP/1.1 200 OK\n Content-Type: text/html\n\n {request_data}"
    return http_response.encode()


def server_forever():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
        listen_socket.bind((HOST, PORT))
        listen_socket.listen()
        print(f"Serving HTTP on port {PORT}...")
        while True:
            client_conn, client_addr = listen_socket.accept()
            while client_conn:
                request = client_conn.recv(1024)
                http_response = handle_request(request)
                client_conn.sendall(http_response)


if __name__ == '__main__':
    server_forever()

