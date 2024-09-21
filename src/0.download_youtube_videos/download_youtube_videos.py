import csv
import youtube_dl

def download_videos_from_csv(csv_file, download_dir):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            video_url = row[2]
            download_video(video_url, download_dir)

def download_video(video_url, download_dir):
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': f'{download_dir}/%(title)s.%(ext)s'
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            ydl.download([video_url])
        except Exception as e:
            print(f"Error downloading video '{video_url}': {e}")

if __name__ == "__main__":
    csv_file = "D:\\video_summary\\0.download_youtube_videos\\all_videos_data.csv"
    download_dir = "D:\\video_summary\\youtube_downloaded_videos"
    download_videos_from_csv(csv_file, download_dir)