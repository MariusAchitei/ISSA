import socket
import threading

from server.client import Client

MESSAGE_TYPES = {
    0: "register Rentee",
    1: "register Owner",
    2: "post Car",
    3: "requestCar",
    4: "startRental",
    5: "endRental"
}


def check_permission(client_id, message_id):
    if client_id == 0:  # Owner
        return message_id in (1, 2)
    elif client_id == 1:  # Renter
        return message_id in (0, 3, 4, 5)
    else:
        return False


def handle_client(client_socket):
    client = Client(client_socket)
    while True:
        try:
            client.login()
            if client.is_owner:
                client.owner_menu()
            else:
                client.renter_menu()
        except ValueError:
            print("Invalid input. Please enter valid integers for client ID and message ID.")


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
