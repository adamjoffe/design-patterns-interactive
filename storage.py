from bestql.contract import Contract

class Storage():
    contract: Contract
    def __new__(cls):
        # Singleton pattern enforced here
        if not hasattr(cls, 'instance'):
            cls.instance = super(Storage, cls).__new__(cls)
            cls.instance.contract = Contract()
        return cls.instance


    def get_warehouse(self):
        self.contract.get_warehouse() 