from dataclasses import dataclass
from pathlib import Path

from pytube import YouTube


@dataclass
class YouTubeDownloader:
    """Handles YouTube video downloading with pytube library."""

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
            yt = YouTube(self.url)

            # Filter for progressive streams (audio + video) in MP4 format
            streams = yt.streams.filter(progressive=True, file_extension="mp4")

            if not streams:
                print("No suitable streams found for this video.")
                return

            # Get highest resolution stream
            highest_res_stream = streams.get_highest_resolution()

            if not highest_res_stream:
                print("Could not find highest resolution stream.")
                return

            # Download the video
            print(f"Downloading '{yt.title}'...")
            filename = highest_res_stream.download(output_path=self.save_path)
            print(f"Video downloaded successfully! Saved to: {filename}")

        except Exception as e:
            print(f"An error occurred: '{e}'")
            # Print additional debugging info for common issues
            if "400" in str(e):
                print("This might be due to YouTube API changes or network issues.")
                print("Try checking your internet connection or updating pytube.")
                print("You can update pytube with: pip install --upgrade pytube")
        finally:
            pass


def main() -> None:
    """Main entry point for testing purposes."""
    pass


if __name__ == "__main__":
    main()
