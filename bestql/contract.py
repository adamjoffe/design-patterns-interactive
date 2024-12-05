import time
from typing import Any
from bestql.warehouse import Warehouse


class Contract:
    def __init__(self):
        self.__establish_contract()
        self.__storage: dict[str, Any] = {}

    def __establish_contract(self) -> None:
        ''' Complete a long boring legal contract to work with the company '''
        print("Signing boring paperwork...")
        time.sleep(3)

    def get_warehouse(self) -> Warehouse:
        ''' Get access to a warehouse to store and retrieve cars '''
        return Warehouse(self.__storage)
