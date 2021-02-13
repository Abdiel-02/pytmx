from xml.etree import ElementTree
from typing import Dict, Optional, Tuple, Union
from tmx.base import BaseObject
from .color import Color
from .image import Image

########## OBJECTS GROUP SUBMODELS ##########

class Object(BaseObject):
    def __init__(self, data: ElementTree.Element):
        super().__init__(data)

    @property
    def height(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("height"))
        except ValueError: return float(self._data.attrib.get("height"))
        except TypeError: return 0

    @property
    def width(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("width"))
        except ValueError: return float(self._data.attrib.get("width"))
        except TypeError: return 0    

class Ellipse(BaseObject):
    def __init__(self, data: ElementTree.Element):
        super().__init__(data)

    @property
    def height(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("height"))
        except ValueError: return float(self._data.attrib.get("height"))
        except TypeError: return 0

    @property
    def width(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("width"))
        except ValueError: return float(self._data.attrib.get("width"))
        except TypeError: return 0

class Point(BaseObject):
    def __init__(self, data: ElementTree.Element):
        super().__init__(data)

class Polygon(BaseObject):
    def __init__(self, data: ElementTree.Element):
        super().__init__(data)

    @property
    def points(self) -> Tuple[Tuple[int]]:
        return tuple([
            (float(p.split(",")[0]), float(p.split(",")[1]))
            for p in self._data.find("polygon").attrib.get("points").split(" ")
        ])

class Text(BaseObject):
    def __init__(self, data: ElementTree.Element):
        super().__init__(data)

    @property
    def bold(self) -> bool:
        return bool(self._data.attrib.get("bold", 0))

    @property
    def color(self) -> Color:
        return Color(self._data.attrib.get("color"))

    @property
    def fontfamily(self) -> str:
        return self._data.attrib.get("fontfamily")

    @property
    def halign(self) -> str:
        return self._data.attrib.get("halign")

    @property
    def height(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("height"))
        except ValueError: return float(self._data.attrib.get("height"))
        except TypeError: return 0

    @property
    def pixelsize(self) -> int:
        return int(self._data.attrib.get("pixelsize"))

    @property
    def text(self) -> str:
        return self._data.text

    @property
    def valign(self) -> str:
        return self._data.attrib.get("valign")

    @property
    def wrap(self) -> bool:
        return bool(self._data.attrib.get("wrap", 0))

    @property
    def width(self) -> Union[int, float]:
        try: return int(self._data.attrib.get("width"))
        except ValueError: return float(self._data.attrib.get("width"))
        except TypeError: return 0

#############################################

############# TILESET SUBMODELS #############

class Grid:
    def __init__(self, data: ElementTree.Element):
        self._data = data

    @property
    def orientation(self) -> str:
        return self._data.attrib.get("orientation")

    @property
    def width(self) -> int:
        return int(self._data.attrib.get("width"))

    @property
    def height(self) -> int:
        return int(self._data.attrib.get("height"))

class Frame:
    def __init__(self, data: ElementTree.Element):
        self._data = data

    @property
    def tileid(self) -> int:
        return self._data.attrib.get("tileid")
    
    @property
    def duration(self) -> int:
        return self._data.attrib.get("duration")

class Animation:
    def __init__(self, data: ElementTree.Element):
        self._data = data

    @property
    def frames(self) -> Tuple[Frame]:
        return tuple(
            [Frame(data) for data in self._data.findall("frame")]
        )

class TileObjecGroup:
    def __init__(self, data: ElementTree.Element) -> None:
        self._data = data

    @property
    def id(self) -> int:
        return int(self._data.attrib.get("id"))

    @property
    def draworder(self) -> str:
        return self._data.attrib.get("draworder")

    @property
    def objects(self) -> None:
        return None

class Tile:
    def __init__(self, data: ElementTree.Element) -> None:
        self._data = data

    @property
    def id(self) -> int:
        return int(self._data.attrib.get("id"))

    @property
    def animation(self) -> Optional[Animation]:
        return Animation(self._data.find("animation")) \
            if self._data.find("animation") != None \
            else None

    @property
    def image(self) -> Image:
        return Image(self._data.find("image"))

    @property
    def properties(self) -> Optional[Dict[str, str]]:
        return {
            prop.attrib.get("name"):prop.attrib.get("value")
            for prop in self._data.find("properties").iter("property")
        } if self._data.find("properties") != None else None

    @property
    def get_objectGroup(self) -> None:
        return None

#############################################
