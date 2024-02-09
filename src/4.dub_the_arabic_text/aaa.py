from gtts import gTTS
from pydub import AudioSegment
import os

def generate_audio(text, output_file):
    tts = gTTS(text=text, lang='ar')
    tts.save(output_file)

def overlay_audio(voice_file, output_file, background_file):
    background_audio = AudioSegment.from_file(background_file)
    # Load the audio clip
    voice_audio = AudioSegment.from_file(voice_file, format="mp3")
    duration = len(audio) / 1000  # Duration in seconds
    if duration > 190:  # 3 minutes and 10 seconds in seconds
        speed_factor = 190 / duration
        audio = audio.speedup(playback_speed=speed_factor)
    # Define the volume factor (1.0 is the original volume, values greater than 1 increase the volume)
    volume_factor = 10 # Increase the volume by 50%
    # Adjust the volume of the audio clip
    increased_volume_clip = voice_audio + volume_factor
    # Overlay the voice narration on the background tune
    output_audio = increased_volume_clip.overlay(background_audio, position=0)
    # Export the final audio
    output_audio.export(output_file, format="mp3")




def narrate_files(input_folder, output_folder, background_music_path, speed=1.1):
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):  # Assuming all files are text files
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename.replace(".txt", "_narrated.mp3"))
            # Read text from input file
            with open(input_file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            # Generate voice narration
            voice_file = os.path.join(output_folder, filename.replace(".txt", "_voice.mp3"))
            generate_audio(text, voice_file)
            # Overlay voice narration on background tune
            overlay_audio(voice_file, output_file_path, background_music_path)
            # Remove the temporary voice narration file
            os.remove(voice_file)
            print(f"Narration completed for {filename}")


if __name__ == "__main__":
    input_folder = 'D:\\video_summary\\processing\\Transcripts\\Cutseries_film_sumarized_translated' 
    output_folder = 'D:\\video_summary\\processing\\arabic_narrators\\Cutseries_film_narrated0a'
    background_music_path = "D:\\video_summary\\processing\\background_audios\\Sailing.mp3"
    speed = 1.2

    narrate_files(input_folder, output_folder,background_music_path, speed)    

