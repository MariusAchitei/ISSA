from server.model.user import User
from sqlalchemy import exc, func
import datetime
from server.db_interaction.BaseRepo import BaseRepo


class UserRepository:
    _instance = None

    def __new__(cls, session):
        if cls._instance is None:
            cls._instance = super(UserRepository, cls).__new__(cls)
            cls._instance.session = session
        return cls._instance

    @staticmethod
    def get_instance():
        return UserRepository._instance

    def __init__(self, session):
        pass

    def create_user(self, username, is_owner, password):
        user = User()
        user.username = username
        user.is_owner = is_owner
        user.password = password
        self.session.add(user)
        self.session.commit()
        return user

    def get_user_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_user_by_id(self, id):
        return self.session.query(User).filter(User.id == id).first()

    def get_user_by_username_and_password(self, username, password):
        return self.session.query(User).filter(User.username == username, User.password == password).first()
