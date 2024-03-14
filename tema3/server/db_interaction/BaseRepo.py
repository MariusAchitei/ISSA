class BaseRepo:
    _instance = None

    def __new__(cls, session):
        if cls._instance is None:
            cls._instance = super(BaseRepo, cls).__new__(cls)
            cls._instance.session = session
        return cls._instance

    @staticmethod
    def get_instance():
        return BaseRepo._instance
