from xml.etree import ElementTree
from typing import Optional, Tuple, Union
from ..base import BaseLayer
from ..const import ObjectsTypes
from .extras import Color, Object, Ellipse, Point, Polygon, Text
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

    def get_objects(self) -> Optional[Tuple[Union[Object, Ellipse, Point, Polygon, Text]]]:
        result = list()

        for child in self._data.findall("object"):
            if child.find(ObjectsTypes.ELLIPSE) != None:
                result.append(Ellipse(child))
            elif child.find(ObjectsTypes.POINT) != None:
                result.append(Point(child))
            elif child.find(ObjectsTypes.POLYGON) != None:
                result.append(Polygon(child))
            elif child.find(ObjectsTypes.TEXT) != None:
                result.append(Text(child))
            else:
                result.append(Object(child))

        return tuple(result)
        