from typing import Any


class Warehouse:
    def __init__(self, storage: dict[str, Any]):
        self.__storage = storage
    
    def store_car(self, vin: str, data: Any) -> None:
        ''' Store a car in the warehouse using its VIN '''
        self.__storage[vin] = data

    def retrieve_all_cars(self) -> dict:
        ''' Retrieve all cars in the warehouse '''
        return self.__storage
    
    def retrieve_car_by_vin(self, vin: str) -> Any:
        ''' Retrieve a car in the warehouse by its VIN '''
        return self.__storage.get(vin)
