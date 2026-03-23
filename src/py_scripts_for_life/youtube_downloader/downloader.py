from dataclasses import dataclass

from .constants import Paths


@dataclass
class Downloader:
    url: str
    destination: Paths
