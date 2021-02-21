from xml.etree import ElementTree
from typing import Union
from ...const import EncodingFormat

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
