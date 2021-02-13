from enum import Enum

class EncodingFormat:
    BASE64 = "base64"
    CSV = "csv"

class CompresionFormat:
    GZIP = "gzip"
    ZLIB = "zlib"
    ZSTANDARD = "zstd"

class ObjectsTypes:
    OBJECTS = "object"
    ELLIPSE = "ellipse"
    POINT = "point"
    POLYGON = "polygon"
    TEXT = "text"

class RenderOrder:
    RIGHT_DOWN = "right-down"
    RIGHT_UP = "right-up"
    LEFT_DOWN = "left-down"
    LEFT_UP = "left-up"

class ObjectAlignment:
    TOP_LEFT = "topleft"
    TOP = "top"
    TOP_RIGHT = "topright"
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    BOTTOM_LEFT = "bottomleft"
    BOTTOM = "bottom"
    BOTTOM_RIGHT = "bottomright"

class Flipped_Flags(Enum):
    FLIPPED_HORIZONTALLY_FLAG = int("0x80000000", 16)
    FLIPPED_VERTICALLY_FLAG = int("0x40000000", 16)
    FLIPPED_DIAGONALLY_FLAG = int("0x20000000", 16)
