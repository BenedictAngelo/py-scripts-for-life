from ..shared import Graphics
from ..shared.authenticators import Authenticators
from ..shared.constants import Paths
from .downloader import YouTubeDownloader


def app() -> None:
    """Main application loop for YouTube Downloader."""
    title: str = "YouTube Downloader"
    Graphics.script_title(title)

    # Display instructions
    print(f"Download YouTube videos to '{Paths.VIDEOS_PATH}'")
    print("")

    while True:
        # Get YouTube URL with validation
        what_url: str = Authenticators.get_user_input(
            "Enter the YouTube URL you want to download (q to quit): ",
            allow_quit=True,
        )

        # Validate URL format (basic check)
        if not what_url.startswith(("http://", "https://")):
            print("Please enter a valid URL starting with http:// or https://")
            continue

        what_save_path: str = Paths.VIDEOS_PATH
        YouTubeDownloader(url=what_url, save_path=what_save_path).yt_downloader()


def main() -> None:
    """Entry point for YouTube Downloader application."""
    app()


if __name__ == "__main__":
    main()
