from gtts import gTTS
from pydub import AudioSegment
import os

def generate_audio(text, output_file):
    tts = gTTS(text=text, lang='ar')
    tts.save(output_file)

def overlay_audio(voice_file, output_file, background_file):
    background_audio = AudioSegment.from_file(background_file)
    voice_audio = AudioSegment.from_file(voice_file)
    # Adjust the amplitude of the voice narration
    voice_audio = voice_audio + (voice_audio - voice_audio.dBFS) * 3
    # Overlay the voice narration on the background tune
    output_audio = background_audio.overlay(voice_audio, position=0)
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
    input_folder = 'D:\\video_summary\\processing\\arabic_transcripts' 
    output_folder = 'D:\\video_summary\\processing\\arabic_narrators'
    background_music_path = "D:\\video_summary\\processing\\background_audios\\separation.mp3"
    speed = 1.1

    narrate_files(input_folder, output_folder,background_music_path, speed)    
