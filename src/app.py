from person import Person
from rich.console import Console
from rich.table import Table

console = Console()

people = [
    Person("Uriel", 25, "uriel@email.com"),
    Person("Valen", 24, "valen@email.com"),
]

table = Table(title="Personas")

table.add_column("Nombre")
table.add_column("Edad")
table.add_column("Email")

for person in people:
    table.add_row(
        person.name,
        str(person.age),
        person.email
    )

console.print(table)