class Client:
    def __init__(self, id: int, name: str, address: str):
        self.__id = id
        self.__name = name
        self.__address = address

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def address(self) -> str:
        return self.__address

    def __repr__(self) -> str:
        return self.name

    def change_name(self, new_name: str) -> str:
        if available := True:
            self.__name = new_name
            # TODO save to DB
            return f"Name changed to {self.name}"
        return f"Name {new_name} alredy exists"

    def change_address(self, new_address: str) -> str:
        self.__address = new_address
        # TODO save to DB
        return f"Address changed to {self.address}"
