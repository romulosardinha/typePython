from typing import List

class User: 
    def __init__(self, name:str, age:int, itens:List[str]):
        self.name = name
        self.age = age
        self.itens = itens

    def falar(self) -> str:
        return f"Olá {self.name}, você tem {self.age} anos"
    
userOnline = User("John Doe", '30', ["item1", "item2"])

res:str = userOnline.falar()

print(res)
