from typing import List, Protocol, Tuple

class ANNOracle(Protocol):
    def query(self, q: list[float], r: int, k: int) -> list[int]:
        ...

class DummyANN:
    def __init__(self, n: int):
        self.n = n

    def query(self, q: list[float], r: int, k: int) -> list[int]:
        return list(range(min(k, self.n)))
