from typing import Tuple

class Color:
    def __init__(self, hexcolor: str):
        self._hexcolor = hexcolor.replace("#", "")

    @property
    def r(self) -> int:
        return int(self._hexcolor[:2], 16)

    @property
    def g(self) -> int:
        return int(self._hexcolor[2:4], 16)

    @property
    def b(self) -> int:
        return int(self._hexcolor[4:6], 16)

    @property
    def rgb(self) -> Tuple[int]:
        return (
            int(self._hexcolor[:2], 16),
            int(self._hexcolor[2:4], 16),
            int(self._hexcolor[4:6], 16)
        )

    @property
    def hex(self) -> str:
        return f"#{self._hexcolor}"