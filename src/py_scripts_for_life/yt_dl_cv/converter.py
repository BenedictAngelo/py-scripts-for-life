from dataclasses import dataclass

from .constants import Genre


@dataclass
class Converter:
    input_file: str
    output_file: str


@dataclass
class MetaData:
    title: str
    author: str
    genre: Genre
