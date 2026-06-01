class Person:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Nombre: {self.name}, Edad: {self.age}, Email: {self.email}"

    def is_adult(self):
        return self.age >= 18
