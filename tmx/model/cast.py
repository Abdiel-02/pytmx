from typing import Any, Dict

class Position:
    def __init__(self, pos: Dict[str, int]):
        self._pos = pos

    @property
    def x(self) -> int: 
        return self._pos.get("x")

    @property
    def y(self) -> int: 
        return self._pos.get("y")

    @property
    def top(self) -> int:
        return self._pos.get("top")
    
    @property
    def left(self) -> int:
        return self._pos.get("left")
    
    @property
    def bottom(self) -> int:
        return self._pos.get("bottom")
    
    @property
    def right(self) -> int:
        return self._pos.get("right")

class Cast:
    def __init__(self, data: Dict[str, Any]):
        self._data = data

    @property
    def file(self) -> str:
        return self._data.get("file")

    @property
    def width(self) -> int:
        return self._data.get("width")

    @property
    def height(self) -> int:
        return self._data.get("height")

    @property
    def pos(self) -> Position:
        return self._data.get("pos")

    @property
    def flipx(self) -> bool:
        return self._data.get("flipx")

    @property
    def flipy(self) -> bool:
        return self._data.get("flipy")

    @property
    def flipz(self) -> bool:
        return self._data.get("flipz")