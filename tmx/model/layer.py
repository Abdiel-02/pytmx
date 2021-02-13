from xml.etree import ElementTree
from typing import Optional, Tuple, Union
from tmx.const import EncodingFormat
from tmx.base import BaseLayer
from .extras import Color

class Data:
    def __init__(self, data: ElementTree.Element):
        self._data = data

    @property
    def encoding(self) -> str:
        return self._data.attrib.get("encoding")

    @property
    def compression(self) -> str:
        return self._data.attrib.get("compression")

    @property
    def value(self) -> Union[bytes, str]:
        if self.encoding == EncodingFormat.BASE64:
            return bytes(self._data.text.strip(), "UTF-8")
        else:
            return self._data.text.strip().replace("\n", "")

class Layer(BaseLayer):
    def __init__(self, data: ElementTree.Element) -> None:
        super().__init__(data)

    @property
    def data(self) -> Data:
        return Data(self._data.find("data"))

    @property
    def height(self) -> int:
        return int(self._data.attrib.get("height"))

    @property
    def width(self) -> int:
        return int(self._data.attrib.get("width"))

class ObjectGroup(BaseLayer):
    def __init__(self, data: ElementTree.Element) -> None:
        super().__init__(data)

    @property
    def color(self) -> Optional[Color]:
        return Color(self._data.attrib.get("color")) \
            if self._data.attrib.get("color", None) \
            else None

    @property
    def draworder(self) -> str:
        return self._data.attrib.get("draworder", "topdown")

    @property
    def height(self) -> Union[int, float]:
        try: return int(self._child.attrib.get("height"))
        except ValueError: return float(self._child.attrib.get("height"))

    @property
    def width(self) -> Union[int, float]:
        try: return int(self._child.attrib.get("width"))
        except ValueError: return float(self._child.attrib.get("width"))

    def get_objects(self) -> None:
        pass
