from pydub import AudioSegment
import os

def overlay_audio(voice_file, output_file_path, background_music_path):
    background_audio = AudioSegment.from_file(background_music_path)
    audio = AudioSegment.from_file(voice_file)
    
    duration = len(audio) / 1000  # Duration in seconds

    if duration > 190:  # 3 minutes and 10 seconds in seconds
        speed_factor = 190 / duration
        audio = audio.speedup(playback_speed=speed_factor)

    audio = audio + 10  # Increase volume level by 10 times
    merged_audio = audio.overlay(background_audio)

    merged_audio.export(output_file_path, format="mp3")  # Adjust format as needed

def narrate_files(input_folder, output_folder, background_music_path, speed):
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            voice_file = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)
            overlay_audio(voice_file, output_file_path, background_music_path)

# Example usage
input_folder = 'D:\\video_summary\\processing\\Transcripts\\Cutseries_film_sumarized_translated' 
output_folder = 'D:\\video_summary\\processing\\arabic_narrators\\Cutseries_film_narrated0a'
background_music_path = "D:\\video_summary\\processing\\background_audios\\Sailing.mp3"
speed = 1.2            

narrate_files(input_folder, output_folder, background_music_path, speed)
