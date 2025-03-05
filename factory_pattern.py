class Vehicle:
    def __init__(self, make: str, model: str, region_spec: str):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} {self.region_spec}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} {self.region_spec}: Мотор заведено")


class VehicleFactory:
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU")


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Tesla", "model Y")
    us_motorcycle = us_factory.create_motorcycle("Halcyon", "250")

    us_car.start_engine()
    us_motorcycle.start_engine()

    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("Volkswagen", "Tiguan")
    eu_motorcycle = eu_factory.create_motorcycle("Yamaha", "150")

    eu_car.start_engine()
    eu_motorcycle.start_engine()
