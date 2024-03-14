import socket
from server.client import Client

MESSAGE_TYPES = {
    0: "register Rentee",
    1: "register Owner",
    2: "post Car",
    3: "requestCar",
    4: "startRental",
    5: "endRental"
}


def send_formatted_message(client_socket, messages):
    message = concatenate_message(messages)
    send_message(client_socket, message)


def concatenate_message(messages):
    return "|".join(messages)


def send_message(client_socket, message):
    client_socket.sendall(message.encode())
    # data = client_socket.recv(1024)
    # print('Received from server:', data.decode())


def login(client_socket):
    username = input("Enter username: ")
    password = input("Enter password: ")
    send_formatted_message(client_socket, [username, password])
    succes = client_socket.recv(1024)
    if succes.decode() == "True":
        print("Login succesful")
        return True
    else:
        print("Login failed")
        return False


def main_loop(client_socket):
    menu = client_socket.recv(1024)
    print(menu.decode())
    choice = input("Enter your choice: ")
    send_message(client_socket, choice)


def main():
    server_host = 'localhost'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    is_login = False

    while not is_login:
        is_login = login(client_socket)

    while True:
        main_loop(client_socket)

    client_socket.close()


if __name__ == "__main__":
    main()
