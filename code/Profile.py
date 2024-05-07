from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ProfileEntry:
    count: int
    order: list

    def __post_init__(self):
        if self.count <= 0:
            raise ValueError


@dataclass
class Profile:
    candidates: list
    entries: List[ProfileEntry]

    def __post_init__(self):
        if not self.candidates or not self.entries:
            raise ValueError
        self.m = len(self.candidates)
        self.n = 0
        for entry in self.entries:
            if set(entry.order) != set(self.candidates):
                raise ValueError
            self.n += entry.count
