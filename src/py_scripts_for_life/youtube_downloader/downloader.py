import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class YouTubeDownloader:
    """Handles YouTube video downloading using yt-dlp subprocess."""

    url: str
    save_path: str

    def yt_downloader(self) -> None:
        """
        Download YouTube video in highest resolution MP4 format using yt-dlp.

        Uses subprocess to execute yt-dlp command for better isolation and control.
        """
        try:
            # Ensure save path exists
            Path(self.save_path).mkdir(parents=True, exist_ok=True)

            print(f"Downloading from URL: '{self.url}'")

            # Configure yt-dlp command for MP4 format with best quality
            # Added additional flags to handle common YouTube issues
            yt_dlp_cmd: list = [
                "yt-dlp",
                "--format",
                "bv*+ba/b",
                "--merge-output-format",
                "mp4",
                "--output",
                str(Path(self.save_path) / "%(title)200s.%(ext)s"),
                "--no-warnings",
                "--prefer-ffmpeg",
                self.url,
            ]

            # Run yt-dlp as subprocess
            result = subprocess.run(
                yt_dlp_cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            print(f"Video downloaded successfully! Saved to: '{self.save_path}'")

        except subprocess.CalledProcessError as e:
            error_msg = (
                e.stderr.decode("utf-8") if e.stderr else "Unknown error occurred"
            )
            print(f"An error occurred: {error_msg.strip()}")
            # Print additional debugging info for common issues
            if "400" in error_msg or "403" in error_msg:
                print("This might be due to network issues or geo-restrictions.")
                print("Try checking your internet connection.")
            print("You can update yt-dlp with: pip install --upgrade yt-dlp")
        except FileNotFoundError:
            print("Error: yt-dlp not found. Please install yt-dlp to use this feature.")
            print("Install with: pip install yt-dlp")
        except Exception as e:
            print(f"An unexpected error occurred: '{e}'")


def main() -> None:
    """Main entry point for testing purposes."""
    pass


if __name__ == "__main__":
    main()
