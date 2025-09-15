"""
    Type Hints für Arrays

    List und DIct sind deprecated in neuen Projekten
"""

from typing import List, Tuple, Dict, Set

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

coord: Tuple[float, float] = (56.345, 43.345)

user: Dict[int, str] = {1: "Alice" }
user2: Dict[str, str] = {"firstname": "Alice"}
user3: Dict[str, int] = {"Max": 12}

namen: Set[str] = {"Alice", "Bob", "Bob"}

# Ab Python 3.9 sollte die eingebaute generische Syntax verwenden!!!

