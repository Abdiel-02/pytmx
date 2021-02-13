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
    def opacity(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("opacity", 1))
        except ValueError: return float(self._data.attrib.get("opacity"))

    @property
    def tintcolor(self) -> Optional[Color]:
        return Color(self._data.attrib.get("tintcolor")) \
            if self._data.attrib.get("tintcolor", None) != None \
            else None

    @property
    def visible(self) -> bool:
        return bool(int(self._data.attrib.get("visible", 1)))  