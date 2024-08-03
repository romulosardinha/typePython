from typing import TypedDict, List

class UserDict(TypedDict):
    name: str
    age: int
    itens: List[str]

userOnline: UserDict = {
    "name": "John Doe",
    "age": 30,
    "itens": ["item1", "item2"]
}

def falar(user: UserDict) -> str:
    return f"Olá {user['name']}, você tem {user['age']} anos"\

res:str = falar(userOnline)

print(res)
