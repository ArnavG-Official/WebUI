from __future__ import annotations
from typing import Callable


class State:
    def __init__(self, value: object | None = None) -> None:
        self._value = value
        self._listeners: list[Callable[[object | None], None]] = []

    @property
    def value(self) -> object | None:
        return self._value

    def set(self, value: object | None) -> None:
        self._value = value
        for listener in list(self._listeners):
            listener(value)

    def subscribe(self, callback: Callable[[object | None], None]) -> None:
        self._listeners.append(callback)
