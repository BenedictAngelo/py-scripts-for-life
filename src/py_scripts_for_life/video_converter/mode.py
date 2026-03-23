import os
from ..shared import Graphics
from .constants import Paths, FileFormat
from .converter import Converter


class ConversionPrompts:
    @staticmethod
    def single_convert() -> None:

        while True:
            input_file: str = input(
                "Enter the name of the file you want to convert (path/to/[file.fileformat]) (q to quit):"
            )
            if input_file == "q":
                Graphics.closing()
                exit()
            else:
                pass

            output_file: str = input(
                "Enter the ouput file name **ALWAYS PUT '.mp3' after file names** (q to quit): "
            )
            if output_file == "q":
                Graphics.closing()
                exit()
            elif output_file == "":
                print(
                    "Invalid input, output file name must at least have some characters and '.mp3'"
                )
                continue
            else:
                pass

            Converter(input_file, output_file).converter()

    @staticmethod
    def bulk_convert() -> None:

        for i, filename in enumerate(os.listdir(Paths.VIDEOS_PATH)):
            if filename.lower().endswith((FileFormat.MP4, FileFormat.AVI, FileFormat.MKV, FileFormat.MOV))
                Converter(input_file = filename, output_file = f"audio_{i}" + FileFormat.MP3 ).converter()
