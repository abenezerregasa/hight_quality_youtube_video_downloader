import yt_dlp
import os

def download_youtube_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'bestvideo',  # Download only the best video (no audio)
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Download completed! (Video only, no audio) \nSaved in: {save_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    youtube_url = input("Enter YouTube video URL: ")

    # Set your custom save path
    save_directory = "C:/Users/abene/youtubevideodownloader"

    # Ensure the folder exists
    os.makedirs(save_directory, exist_ok=True)

    download_youtube_video(youtube_url, save_directory)
