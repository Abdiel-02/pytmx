from xml.etree import ElementTree

class Image:
    def __init__(self, data: ElementTree.Element):
        self._data = data

    @property
    def width(self) -> int:
        return int(self._data.attrib.get("width"))

    @property
    def height(self) -> int:
        return int(self._data.attrib.get("height"))

    @property
    def source(self) -> str:
        return self._data.attrib.get("source")