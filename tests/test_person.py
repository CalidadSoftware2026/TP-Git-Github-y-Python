from src.person import Person


def test_create_person():
    person = Person(
        "Octavio",
        24,
        "octavio@email.com"
    )

    assert person.name == "Octavio"
    assert person.age == 24
    assert person.email == "octavio@email.com"


def test_is_adult_true():
    person = Person(
        "Juan",
        20,
        "juan@email.com"
    )

    assert person.is_adult() is True


def test_is_adult_false():
    person = Person(
        "Pedro",
        15,
        "pedro@email.com"
    )

    assert person.is_adult() is False

    def test_valid_email():
    person = Person(
        "Uriel",
        25,
        "uriel@email.com"
    )

    assert person.has_valid_email() is True


def test_invalid_email():
    person = Person(
        "Uriel",
        25,
        "urielemail.com"
    )

    assert person.has_valid_email() is False