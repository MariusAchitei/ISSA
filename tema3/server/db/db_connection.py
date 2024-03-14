from sqlalchemy import create_engine
from server.db.db_settings import mysql


class Database:
    """
    The class that handles the database connection
    Attributes

    connection : Database
                provides database connection

    engine : Engine
           instance of Engine class, helps the connectivity

    Functions

    get_instance()
        Returns the specific instance of the database class.
    """
    connection = None

    @staticmethod
    def get_instance():
        """
        Returns a specific instance of the database class.

        :return: a specific instance of the database class
        """
        if Database.connection is None:
            Database()
        return Database.connection

    def __init__(self):
        if Database.connection is not None:
            raise Exception("Error! Creating more instances of a singleton is not allowed")
        else:
            Database.connection = self
            url = 'mysql://{user}:{passwd}@{host}:{port}/{db}'.format(
                user=mysql['user'], passwd=mysql['password'], host=mysql['host'],
                port=mysql['port'], db=mysql['db'])
            try:
                self.engine = create_engine(url, pool_size=50)
                print("Connected to PostgreSQL database!")
            except IOError:
                print("Failed to connect to the database.")
