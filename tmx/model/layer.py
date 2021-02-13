from xml.etree import ElementTree
from typing import Optional, Tuple, Union
from tmx.const import EncodingFormat
from tmx.base import BaseLayer

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