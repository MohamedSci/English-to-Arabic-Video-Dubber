import os
import subprocess

def run_download_youtube_videos():
    """Runs the download_youtube_videos.py script."""
    subprocess.run(["python", "download_youtube_videos.py"])

def run_extract_audio():
    """Runs the extract_audio.bat script."""
    subprocess.run(["extract_audio.bat"])

def run_transcript_audio_script():
    """Runs the transcript_audio_script.py script."""
    subprocess.run(["python", "transcript_audio_script.py"])

def run_translation_google():
    """Runs the translation_google.py script."""
    subprocess.run(["python", "translation_google.py"])

def run_man_narrate_arabic_with_background_tune():
    """Runs the man_narrate_arabic_with_background_tune.py script."""
    subprocess.run(["python", "man_narrate_arabic_with_background_tune.py"])

def run_merge_the_Arabic_audio_with_video():
    """Runs the merge_the_Arabic_audio_with_video.py script."""
    subprocess.run(["python", "merge_the_Arabic_audio_with_video.py"])

def main():
    run_download_youtube_videos()
    run_extract_audio()
    run_transcript_audio_script()
    run_translation_google()
    run_man_narrate_arabic_with_background_tune()
    run_merge_the_Arabic_audio_with_video()

if __name__ == "__main__":
    main()