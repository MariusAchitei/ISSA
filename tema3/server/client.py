from server.db_interaction.UserRepository import UserRepository
from server.utils import Utils
from server.db.session import session_scope


class Client:

    def __init__(self, client_socket):
        with session_scope() as crt_session:
            self.userRepository = UserRepository(crt_session).get_instance()
        self.is_owner = False
        self.id = None
        self.username = None
        self.is_logged = False
        self.client_socket = client_socket

    def login(self):
        while True:
            username, password = Utils.decode_message(self.client_socket.recv(1024))
            print(username, password)
            user = self.userRepository.get_user_by_username_and_password(username, password)
            if user is None:
                self.client_socket.sendall("False".encode())
                continue
            self.id = user.id
            self.username = user.username
            self.is_owner = user.is_owner
            self.is_logged = True
            self.client_socket.sendall("True".encode())
            break

    def owner_menu(self):
        while True:
            message = "1. Post car\n2. View my cars\n3. delete car\n8. Exit"
            self.client_socket.sendall(message.encode())
            choice = int(self.client_socket.recv(1024).decode())
            print(choice, choice == 1)
            if choice == 1:
                self.post_car()
            elif choice == 2:
                self.view_cars()
            elif choice == 3:
                self.view_requests()
            elif choice == 8:
                break
            else:
                print("Invalid choice. Please enter a valid choice.")
        pass

    def post_car(self):
        # car = Car()
        pass

    def view_cars(self):
        pass

    def view_requests(self):
        pass
    def renter_menu(self):
        pass