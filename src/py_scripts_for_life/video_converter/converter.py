import subprocess
from dataclasses import dataclass

from .constants import Paths


@dataclass
class Converter:
    input_file: str
    output_file: str

    def converter(self):
        ffmpeg_cmd: list = [
            "ffmpeg",
            "-i",
            self.input_file,
            "acodec",
            "libmp3lame",
            "-ab",
            "192k",
            "-ar",
            "44100",
            "-y",
            (Paths.MUSIC_PATH + self.output_file),
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print(
                f"\nFile(s) Successfully converted! See in your '{Paths.MUSIC_PATH}' directory"
            )
        except subprocess.CalledProcessError:
            print("\nConversion failed.")
        finally:
            pass


def main():
    pass


if __name__ == "__main__":
    main()
