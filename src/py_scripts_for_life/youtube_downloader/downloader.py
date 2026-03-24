from dataclasses import dataclass
from pathlib import Path

import yt_dlp


@dataclass
class YouTubeDownloader:
    """Handles YouTube video downloading with yt-dlp library."""

    url: str
    save_path: str

    def yt_downloader(self) -> None:
        """
        Download YouTube video in highest resolution MP4 format.

        Validates the save path and handles common download errors.
        """
        try:
            # Ensure save path exists
            Path(self.save_path).mkdir(parents=True, exist_ok=True)

            print(f"Downloading from URL: '{self.url}'")

            # Configure yt-dlp options for MP4 format with best quality
            ydl_opts: dict = {
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "outtmpl": str(Path(self.save_path) / "%(title)s.%(ext)s"),
                "merge_output_format": "mp4",
                "quiet": False,
                "no_warnings": False,
            }

            # Create YoutubeDL instance and download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.extract_info(self.url, download=True)
                print(f"Video downloaded successfully! Saved to: '{self.save_path}'")

        except Exception as e:
            print(f"An error occurred: '{e}'")
            # Print additional debugging info for common issues
            if "400" in str(e) or "403" in str(e):
                print("This might be due to network issues or geo-restrictions.")
                print("Try checking your internet connection.")
            print("You can update yt-dlp with: pip install --upgrade yt-dlp")
        finally:
            pass


def main() -> None:
    """Main entry point for testing purposes."""
    pass


if __name__ == "__main__":
    main()
