import os
from pathlib import Path

from ..shared.authenticators import Authenticators
from .constants import FileFormat, Paths
from .converter import Converter


class ConversionPrompts:
    """Handles user interaction for video conversion modes."""

    @staticmethod
    def single_convert() -> None:
        """Handle single file conversion mode with user input validation."""
        while True:
            # Get input file path with validation
            input_file: str = Authenticators.get_user_input(
                "Enter the path to the file you want to convert (q to quit): ",
                allow_quit=True,
            )

            # Validate that file exists
            if not os.path.exists(input_file):
                print(
                    f"\nError: File '{input_file}' not found. Please check the path.\n"
                )
                continue

            # Get output file name with validation
            output_file: str = Authenticators.get_user_input(
                "Enter the output file name (include .mp3 extension) (q to quit): ",
                validation_func=lambda x: x.endswith(".mp3") and len(x) > 4,
                allow_quit=True,
            )

            # Perform conversion
            Converter(input_file, output_file).converter()

    @staticmethod
    def bulk_convert() -> None:
        """Handle bulk conversion of all supported video files in the Videos directory."""
        videos_path = Path(Paths.VIDEOS_PATH)

        # Check if videos directory exists
        if not videos_path.exists():
            print(f"\nError: Videos directory '{videos_path}' not found.\n")
            return

        # Find all supported video files
        video_files = [
            f
            for f in videos_path.iterdir()
            if f.is_file()
            and f.suffix.lower()
            in (FileFormat.MP4, FileFormat.AVI, FileFormat.MKV, FileFormat.MOV)
        ]

        if not video_files:
            print(f"\nNo supported video files found in '{videos_path}'\n")
            return

        # Confirm with user before proceeding
        print(f"\nFound {len(video_files)} video file(s) to convert:")
        for video_file in video_files:
            print(f"  - {video_file.name}")

        confirm: bool = Authenticators.get_yes_no_input(
            "\nAre you sure you want to convert all these files to MP3? (y/n) (q to quit): "
        )

        if not confirm:
            print("\nBulk conversion cancelled.\n")
            return

        # Convert each video file
        music_path = Path(Paths.MUSIC_PATH)
        music_path.mkdir(parents=True, exist_ok=True)  # Ensure music directory exists

        for i, video_file in enumerate(video_files):
            # Create output filename based on input filename
            output_filename = f"{video_file.stem}.mp3"
            print(
                f"\nConverting ({i + 1}/{len(video_files)}): {video_file.name} -> {output_filename}"
            )

            # Perform conversion
            converter = Converter(str(video_file), output_filename)
            converter.converter()

        print(f"\nBulk conversion completed! Files saved to '{music_path}'\n")
