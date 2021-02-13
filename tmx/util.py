import base64
import numpy as np
from typing import Dict, List, Tuple, Union
from tmx.model.cast import Cast, Position
from tmx.model.layer import Layer
from tmx.model.extras import Tile
from .const import CompresionFormat, EncodingFormat, Flipped_Flags

def b64decode(data: bytes) -> bytes:
    return base64.b64decode(data)

def csv(data: str) -> List[int]:
    return [int(i) for i in data.split(",")]

def decompres(data: bytes, format: str) -> bytes:
    if format == CompresionFormat.GZIP:
        import gzip
        return gzip.decompress(b64decode(data))
    elif format == CompresionFormat.ZLIB:
        import zlib
        return zlib.decompress(b64decode(data))
    elif format == CompresionFormat.ZSTANDARD:
        import zstandard
        return zstandard.decompress(b64decode(data))
    else:
        return b64decode(data)

def to_array(data: Union[bytes, int], cols: int) -> np.ndarray:
    if type(data) == bytes:
        temp = [data[i] | (data[i + 1] << 8) |
            (data[i + 2] << 16) | (data[i + 3] << 24)
            for i in range(0, len(data), 4)
        ]
        arr = [temp[i:i+cols] for i in range(0, len(temp), cols)]
        return np.array(arr)
    else:
        arr = [data[i:i+cols] for i in range(0, len(data), cols)]
        return np.array(arr)

def get_flipping(value: int) -> Tuple[bool]:
    return (
        bool((value & Flipped_Flags.FLIPPED_HORIZONTALLY_FLAG.value)),
        bool((value & Flipped_Flags.FLIPPED_VERTICALLY_FLAG.value)),
        bool((value & Flipped_Flags.FLIPPED_DIAGONALLY_FLAG.value))
    )

def get_gid(value: int) -> int:
    return value & ~(
        Flipped_Flags.FLIPPED_HORIZONTALLY_FLAG.value |
        Flipped_Flags.FLIPPED_VERTICALLY_FLAG.value |
        Flipped_Flags.FLIPPED_DIAGONALLY_FLAG.value
    )

def get_pos(row: int, col: int, layer: Layer, tilewidth: int, tileheight: int) -> Position:
    offset_x = layer.offsetx if layer.offsetx else 0
    offset_y = layer.offsety if layer.offsety else 0

    pos = dict(
        x = col * tilewidth,
        y = row * tileheight,
        top = (row * tileheight) + offset_y,
        left = (col * tilewidth) + offset_x,
        bottom = (row * tileheight) + offset_y + tileheight,
        right = (col * tilewidth) + offset_x + tilewidth
    )

    return Position(pos)

def compile(tile: Tile, pos: Position, flipping: Tuple[bool]) -> Dict[str, str]:
    return dict(
        file = tile.image.source,
        width = tile.image.width,
        height = tile.image.height,
        pos = pos,
        flipx = flipping[0],
        flipy = flipping[1],
        flipz = flipping[2]
    )

def build(layer: Layer, tilesets: Tuple[Layer], tilewidth: int, tileheight: int) -> Tuple[Cast]:
    temp = None

    if layer.data.encoding == EncodingFormat.BASE64:
        data = decompres(layer.data.value, layer.data.compression)
        temp = to_array(data, layer.width)
    elif layer.data.encoding == EncodingFormat.CSV:
        data = csv(layer.data.value)
        temp = to_array(data, layer.width)

    array = np.argwhere(temp)
    cast = list()

    for point in array:
        row, col = point[0:2]
        value = temp[row, col]
        gid = get_gid(value)

        for tileset in tilesets:
            result = list(filter(
                lambda tile: tile.id == abs(gid - tileset.firstgid),
                tileset.tiles
            ))
            if len(result) < 1: continue
            
            tile = result[0]
            pos = get_pos(row, col, layer, tilewidth, tileheight)
            flipping = get_flipping(value)

            cast.append(Cast(compile(tile, pos, flipping)))
            break
    
    return tuple(cast)