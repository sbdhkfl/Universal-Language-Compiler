from dataclasses import dataclass, field
from typing import Any

@dataclass
class Operation:
    kind: str
    data: dict[str, Any] = field(default_factory=dict)

@dataclass
class Program:
    operations: list[Operation] = field(default_factory=list)

    def add(self, kind: str, **data: Any) -> None:
        self.operations.append(Operation(kind, data))
