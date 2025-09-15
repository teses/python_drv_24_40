"""

    # Ab Python 3.9 kann man statt typing.List etc. die eingebaute generische Syntax verwenden:


"""

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

coord: tuple[float, float] = (56.345, 43.345)

user: dict[int, str] = {1: "Alice" }
user2: dict[str, str] = {"firstname": "Alice"}
user3: dict[str, int] = {"Max": 12}

namen: set[str] = {"Alice", "Bob", "Bob"}

