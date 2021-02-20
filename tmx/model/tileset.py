import os
from xml.etree import ElementTree
from typing import Dict, Optional, Tuple
from tmx.base.color import Color
from tmx.error import TmxFileNotFoundError, TmxParseError
from tmx.model.extras import Grid, Tile, TileOffset

class Tileset:
    def __init__(self, data: ElementTree.Element, path: str, internal: bool = True):
        if internal:
            self._data = data

            file = os.path.join(path, self._data.attrib.get("source"))
            try:
                self._child = ElementTree.parse(file).getroot()
            except FileNotFoundError as ex:
                raise TmxFileNotFoundError(ex.filename)
            except ElementTree.ParseError as ex:
                raise TmxParseError(ex)
        else:
            self._data = None
            self._child = data

    @classmethod
    def from_file(cls, file: str, path: str):
        try:
            data = ElementTree.parse(file).getroot()
            return cls(data, path, False)
        except FileNotFoundError as ex:
            raise TmxFileNotFoundError(ex.filename)
        except ElementTree.ParseError as ex:
            raise TmxParseError(ex)
    
    @property
    def firstgid(self) -> Optional[int]:
        return int(self._data.attrib.get("firstgid")) \
            if self._data != None else None

    @property
    def source(self) -> Optional[str]:
        return self._data.attrib.get("source") \
            if self._data != None else None

    @property
    def name(self) -> str:
        return self._child.attrib.get("name")

    @property
    def columns(self) -> int:
        return int(self._child.attrib.get("columns"))

    @property
    def tilecount(self) -> int:
        return int(self._child.attrib.get("tilecount"))

    @property
    def backgroundcolor(self) -> Optional[Color]:
        return Color(self._child.attrib.get("backgroundcolor", None)) \
            if self._child.attrib.get("backgroundcolor", None) != None \
            else None

    @property
    def objectalignment(self) -> Optional[str]:
        return self._data.attrib.get("objectalignment", None) \
            if self._data != None else None

    @property
    def tile_offset(self) -> Optional[TileOffset]:
        return TileOffset(self._child.find("tileoffset")) \
            if self._child.find("tileoffset") != None else None

    @property
    def grid(self) -> Grid:
        return Grid(self._child.find("grid"))

    @property
    def properties(self) -> Optional[Dict[str, str]]:
        return {
            prop.attrib.get("name"):prop.attrib.get("value")
            for prop in self._child.find("properties").iter("property")
        } if self._child.find("properties") != None else None

    @property
    def tiles(self) -> Tuple[Tile]:
        return tuple([Tile(el) for el in self._child.findall("tile")])
