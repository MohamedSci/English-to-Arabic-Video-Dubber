import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.utils import mediainfo

def generate_audio(text, output_file):
    """Generates audio from the given text using Google Text-to-Speech.

    Args:
        text (str): The text to be converted to audio.
        output_file (str): The path to save the audio file.
    """
    tts = gTTS(text=text, lang='ar')
    tts.save(output_file)

def get_audio_duration(file_path):
    """Gets the duration of the audio file in milliseconds.

    Args:
        file_path (str): The path to the audio file.

    Returns:
        int: The duration of the audio file in milliseconds.
    """
    info = mediainfo(file_path)
    duration_ms = float(info['duration']) * 1000
    return duration_ms

def adjust_audio_speed(audio_file_path, max_duration_ms=190000):
    """Adjusts the playback speed of the audio file if it exceeds the maximum duration.

    Args:
        audio_file_path (str): The path to the audio file.
        max_duration_ms (int): The maximum allowed duration in milliseconds.

    Returns:
        AudioSegment: The adjusted audio segment.
    """
    audio_clip_duration = get_audio_duration(audio_file_path)
    if audio_clip_duration > max_duration_ms:
        speed_factor = max_duration_ms / audio_clip_duration
        audio = AudioSegment.from_file(audio_file_path)
        adjusted_audio = audio.speedup(playback_speed=speed_factor)
        return adjusted_audio
    else:
        return AudioSegment.from_file(audio_file_path)

def overlay_audio(voice_file, output_file, background_file):
    """Overlays the voice narration audio on the background music.

    Args:
        voice_file (str): The path to the voice narration audio file.
        output_file (str): The path to save the output audio file.
        background_file (str): The path to the background music file.
    """
    background_audio = AudioSegment.from_file(background_file)
    voice_audio = adjust_audio_speed(voice_file)
    volume_factor = 10  # Increase the volume by 50%
    increased_volume_clip = voice_audio + volume_factor
    output_audio = increased_volume_clip.overlay(background_audio, position=0)
    output_audio.export(output_file, format="mp3")

def narrate_files(input_folder, output_folder, background_music_path, speed=1.1):
    """Narrates the text files in the input folder and saves the output to the output folder.

    Args:
        input_folder (str): The path to the input folder containing text files.
        output_folder (str): The path to the output folder to save the narrated audio files.
        background_music_path (str): The path to the background music file.
        speed (float): The playback speed factor (default is 1.1).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename.replace(".txt", "_narrated.mp3"))
            with open(input_file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            voice_file = os.path.join(output_folder, filename.replace(".txt", "_voice.mp3"))
            generate_audio(text, voice_file)
            overlay_audio(voice_file, output_file_path, background_music_path)
            os.remove(voice_file)
            print(f"Narration completed for {filename}")

if __name__ == "__main__":
    input_folder = 'D:\\video_summary\\processing\\Transcripts\\Cutseries_film_sumarized_translated'
    output_folder = 'D:\\video_summary\\processing\\arabic_narrators\\Cutseries_film_narrated000'
    background_music_path = "D:\\video_summary\\processing\\background_audios\\Sailing.mp3"
    speed = 1.2

    narrate_files(input_folder, output_folder, background_music_path, speed)