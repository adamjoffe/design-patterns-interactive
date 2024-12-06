from bestql.contract import Contract
from bestql.warehouse import Warehouse

class Storage():
    contract: Contract
    def __new__(cls):
        # Singleton pattern to ensure we only sign one contract for warehouse storage
        if not hasattr(cls, 'instance'):
            cls.instance = super(Storage, cls).__new__(cls)
            cls.instance.contract = Contract()
        return cls.instance


    def get_warehouse(self) -> Warehouse:
        return self.contract.get_warehouse() 
