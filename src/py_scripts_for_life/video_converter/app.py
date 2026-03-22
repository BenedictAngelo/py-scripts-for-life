from ..shared import Graphics
from .converter import Converter


def app() -> None:
    """Main application loop for Video converter."""
    title: str = "Video converter"
    Graphics.script_title(title)
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
            "Enter the ouput file name (output automatically stored in 'Music' directory) (q to quit): "
        )
        if output_file == "q":
            Graphics.closing()
            exit()
        else:
            pass

        Converter(input_file, output_file).converter()


def main() -> None:
    app()
    """Entry point for YouTube Downloader application."""


if __name__ == "__main__":
    main()
