from dataclasses import dataclass
import Comparator

@dataclass
class network:
    """
        Do nothing
    """


def test(i: int, j: int) -> Comparator.comparator:
    return Comparator.makeComparator(i, j)
