from server.model.car import Car
from sqlalchemy import exc, func


class CarRepository:

    _instance = None

    def __new__(cls, session):
        if cls._instance is None:
            cls._instance = super(CarRepository, cls).__new__(cls)
            cls._instance.session = session
        return cls._instance

    def __init__(self, session):
        pass

    def create_car(self, car: Car):
        self.session.add(car)
        self.session.commit()
        return car

    def get_car_by_id(self, id):
        return self.session.query(Car).filter(Car.id == id).first()

    def get_car_by_owner_id(self, owner_id):
        return self.session.query(Car).filter(Car.owner_id == owner_id).all()

    def get_car_by_registration_number(self, registration_number):
        return self.session.query(Car).filter(Car.registration_number == registration_number).first()

    def get_all_cars(self):
        return self.session.query(Car).all()

    def get_all_available_cars(self):
        return self.session.query(Car).filter(Car.available == 1).all()

    def get_all_registered_cars(self):
        return self.session.query(Car).filter(Car.registered == 1).all()

    def get_all_online_cars(self):
        return self.session.query(Car).filter(Car.onlinee == 1).all()

    def set_car_online(self, id):
        car = self.get_car_by_id(id)
        car.onlinee = 1
        self.session.commit()
        return car

    def set_car_offline(self, id):
        car = self.get_car_by_id(id)
        car.onlinee = 0
        self.session.commit()
        return car

    def set_car_available(self, id):
        car = self.get_car_by_id(id)
        car.available = 1
        self.session.commit()
        return car

    def set_car_unavailable(self, id):
        car = self.get_car_by_id(id)
        car.available = 0
        self.session.commit()
        return car

    def set_car_registered(self, id):
        car = self.get_car_by_id(id)
        car.registered = 1
        self.session.commit()
        return car

    def set_car_unregistered(self, id):
        car = self.get_car_by_id(id)
        car.registered = 0
        self.session.commit()
        return car


