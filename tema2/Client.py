import socket

MESSAGE_TYPES = {
    0: "register Rentee",
    1: "register Owner",
    2: "post Car",
    3: "requestCar",
    4: "startRental",
    5: "endRental"
}
def main ():
    server_host = 'localhost'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    while True:
        try:
            client_id = int(input("Enter your client ID (0 for Owner, 1 for Renter): "))
            if client_id not in (0, 1):
                print("Invalid client ID. Please enter 0 or 1.")
                continue
            message_id = int(input(f"Enter message ID (0-5): \n{MESSAGE_TYPES}\n"))
            if message_id not in MESSAGE_TYPES:
                print("Invalid message ID. Please enter a number between 0 and 5.")
                continue
            payload = input("Enter payload: ")
            message = f"{client_id}|{message_id}|{payload}"
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print('Received from server:', data.decode())
        except ValueError:
            print("Invalid input. Please enter valid integers for client ID and message ID.")

    client_socket.close()


if __name__ == "__main__":
    main()