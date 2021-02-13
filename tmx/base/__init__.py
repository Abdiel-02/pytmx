from xml.etree import ElementTree
from typing import Dict, Optional, Union
from tmx.model.extras import Color

class BaseLayer:
    def __init__(self, data: ElementTree.Element) -> None:
        self._data = data

    @property
    def id(self) -> int:
        return int(self._data.attrib.get("id"))

    @property
    def name(self) -> str:
        return self._data.attrib.get("name")

    @property
    def offsetx(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("offsetx", 0))
        except ValueError: return float(self._data.attrib.get("offsetx"))

    @property
    def opacity(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("opacity", 1))
        except ValueError: return float(self._data.attrib.get("opacity"))

    @property
    def offsety(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("offsety", 0))
        except ValueError: return float(self._data.attrib.get("offsety"))

    @property
    def properties(self) -> Optional[Dict[str, str]]:
        return {
            prop.attrib.get("name"):prop.attrib.get("value")
            for prop in self._data.find("properties").iter("property")
        } if self._data.find("properties") != None else None

    @property
    def tintcolor(self) -> Optional[Color]:
        return Color(self._data.attrib.get("tintcolor")) \
            if self._data.attrib.get("tintcolor", None) != None \
            else None

    @property
    def visible(self) -> bool:
        return bool(int(self._data.attrib.get("visible", 1)))

class BaseObject:
    def __init__(self, data: ElementTree.Element):
        self._data = data

    @property
    def id(self) -> int:
        return int(self._data.attrib.get("id"))

    @property
    def name(self) -> Optional[str]:
        return self._data.attrib.get("name", None)

    @property
    def properties(self) -> Optional[Dict[str, str]]:
        return {
            prop.attrib.get("name"):prop.attrib.get("value")
            for prop in self._data.find("properties").iter("property")
        } if self._data.find("properties") != None else None
    
    @property
    def rotation(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("rotation"))
        except ValueError: return float(self._data.attrib.get("rotation"))
        except TypeError: return 0

    @property
    def type(self) -> Optional[str]:
        return self._data.attrib.get("type", None)

    @property
    def visible(self) -> bool:
        return bool(self._data.attrib.get("visible", 1))

    @property
    def x(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("x"))
        except ValueError: return float(self._data.attrib.get("x"))

    @property
    def y(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("y"))
        except ValueError: return float(self._data.attrib.get("y"))
