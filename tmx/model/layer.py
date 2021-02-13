from xml.etree import ElementTree
from typing import Optional, Tuple, Union
from tmx.base import BaseLayer
from .extras import Color
from .extras.data import Data

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

class ImageLayer(BaseLayer):
    def __init__(self, data: ElementTree.Element) -> None:
        super().__init__(data)
        self._child = data.find("image", None)

    @property
    def source(self) -> Optional[str]:
        return self._child.attrib.get("source") \
            if self._child != None else None

    @property
    def width(self) -> Optional[Union[int, float]]:
        try: return int(self._child.attrib.get("width"))
        except ValueError: return float(self._child.attrib.get("width"))
        except: return None

    @property
    def height(self) -> Optional[Union[int, float]]:
        try: return int(self._child.attrib.get("height"))
        except ValueError: return float(self._child.attrib.get("height"))
        except: return None

    @property
    def trans_color(self) -> Color:
        return Color(self._child.attrib.get("trans")) \
            if self._child.attrib.get("trans", None) != None \
            else None

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
