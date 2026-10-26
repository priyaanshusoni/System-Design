class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self._make = make
        self._model = model
        self._year = year

    def start_engine(self):
        print("Engine Started")

    def stop_engine(self):
        print("Engine Stopped")

    def display_info(self):
        print(f"{self._make} {self._model} {self._year}")


class ElectricCar(Vehicle):
    def __init__(self, make: str, model: str, year: int, batter_capacity) -> None:
        super().__init__(make, model, year)
        self._battery_capacity = batter_capacity

    def charge_battery(self):
        print(f"Charging {self._battery_capacity}kWh battery")


class GasCar(Vehicle):
    def __init__(self, make: str, model: str, year: int, fuel_tank_size: float):
        super().__init__(make, model, year)
        self._fuel_tank_size = fuel_tank_size

    def fill_tank(self):
        print(f"Filling {self._fuel_tank_size}L fuel tank")
