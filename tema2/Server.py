import socket
import threading

MESSAGE_TYPES = {
    0: "register Rentee",
    1: "register Owner",
    2: "post Car",
    3: "requestCar",
    4: "startRental",
    5: "endRental"
}

def check_permission(client_id, message_id):
    if client_id == 0: # Owner
        return message_id in (1, 2)
    elif client_id == 1: # Renter
        return message_id in (0, 3, 4, 5)
    else:
        return False

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        try:
            client_id, message_id, payload = data.decode().split("|", 2)
            client_id = int(client_id.strip())
            message_id = int(message_id.strip())
            if message_id not in MESSAGE_TYPES:
                response = "Invalid message ID"
            else:
                print(f"Received {MESSAGE_TYPES[message_id]}: {payload.strip()}")
                if not check_permission(client_id, message_id):
                    print(client_id, message_id, check_permission(client_id, message_id))
                    response = "Permission denied"
                else:
                    response = f"Received {MESSAGE_TYPES[message_id]}"

        except ValueError:
            response = "Invalid message format"
        client_socket.sendall(response.encode())
    client_socket.close()


def main():
    server_host = 'localhost'
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print(f"Listening on {server_host}:{server_port}...")

    while True:
        client, addr = server_socket.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == "__main__":
    main()
