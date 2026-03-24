import subprocess
from dataclasses import dataclass
from pathlib import Path

from ..shared import Paths


@dataclass
class Converter:
    """Handles video to audio conversion using FFmpeg."""

    input_file: str
    output_file: str

    def converter(self) -> None:
        """
        Convert video file to MP3 audio using FFmpeg.

        Uses libmp3lame codec with 192k bitrate and 44100 Hz sample rate.
        Output files are saved to the MUSIC_PATH directory.
        """
        # Create full output path
        output_path = Path(Paths.MUSIC_PATH) / self.output_file

        # Ensure music directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Corrected FFmpeg command
        ffmpeg_cmd: list = [
            "ffmpeg",
            "-i",
            self.input_file,
            "-acodec",
            "libmp3lame",
            "-ab",
            "192k",
            "-ar",
            "44100",
            "-y",
            str(output_path),
        ]

        try:
            print(f"\nConverting '{self.input_file}' to '{self.output_file}'...")
            subprocess.run(
                ffmpeg_cmd,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
            )
            print(f"\nFile successfully converted! Saved to '{output_path}'")
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode() if e.stderr else "Unknown error"
            print(f"\nConversion failed: {error_msg}")
        except FileNotFoundError:
            print(
                "\nError: FFmpeg not found. Please install FFmpeg to use this feature."
            )
        except Exception as e:
            print(f"\nUnexpected error during conversion: {str(e)}")


def main() -> None:
    """Main entry point for testing purposes."""
    pass


if __name__ == "__main__":
    main()
