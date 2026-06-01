from person import Person
from rich.console import Console
from rich.table import Table

console = Console()

people = [
    Person("Uriel", 25, "uriel@email.com"),
    Person("Valen", 14, "valen@email.com"),
]

table = Table(title="Personas")

table.add_column("Nombre")
table.add_column("Edad")
table.add_column("Email")
table.add_column("Mayor de edad")

for person in people:
    table.add_row(
        person.name,
        str(person.age),
        person.email,
        "Sí" if person.is_adult() else "No"
    )

console.print(table)
