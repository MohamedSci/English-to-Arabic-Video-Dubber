import os
import speech_recognition as sr
from pydub import AudioSegment
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

nltk.download('punkt')

# Directory containing audio files
processing_folder = 'D:\\video_summary\\processing'
extracted_audio_folder = processing_folder + '\\audio_extracted'
segmented_audio_folder = processing_folder + '\\audio_segmented'
transcript_folder_path = processing_folder + "\\Transcripts"

def create_folder(file_name):
    folder_path = extracted_audio_folder + "\\" + file_name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

def get_subfolders(parent_folder):
    subfolders = []
    for root, dirs, files in os.walk(parent_folder):
        for dir_name in dirs:
            subfolder_path = os.path.join(root, dir_name)
            subfolders.append(subfolder_path)
    return subfolders

def split_audio(input_file, output_folder, segment_length_ms=60000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    audio = AudioSegment.from_file(input_file)
    num_segments = len(audio) // segment_length_ms + 1
    for i in range(num_segments):
        start_time = i * segment_length_ms
        end_time = (i + 1) * segment_length_ms
        segment = audio[start_time:end_time]
        output_file = os.path.join(output_folder, f"segment_{i+1}.wav")
        segment.export(output_file, format="wav")

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def split_audios(folder_name):
    Cus_extracted_audio_folder = extracted_audio_folder + folder_name
    for filenameEx in os.listdir(Cus_extracted_audio_folder):
        if filenameEx.endswith('.wav') or filenameEx.endswith('.flac'):
            audio_file = os.path.join(Cus_extracted_audio_folder, filenameEx)
            filenameDir = filenameEx.split(".wav")[0]
            splitted_folder_file_path = segmented_audio_folder + folder_name + "\\" + filenameDir
            if not os.path.exists(splitted_folder_file_path):
                os.makedirs(splitted_folder_file_path, exist_ok=True)
            split_audio(audio_file, splitted_folder_file_path)

def create_transcripts(folder_name):
    Cus_segmented_audio_folder = segmented_audio_folder + folder_name
    Cus_transcript_folder_path = transcript_folder_path + folder_name
    if not os.path.exists(Cus_transcript_folder_path):
        os.makedirs(Cus_transcript_folder_path, exist_ok=True)
    for splitted_folder_file_path in get_subfolders(Cus_segmented_audio_folder):
        text_content = ""
        transcript_file_name = splitted_folder_file_path.split("\\")[-1]
        transcript_file_path = transcript_folder_path + folder_name + "\\" + transcript_file_name + ".txt"
        for seg_filename in os.listdir(splitted_folder_file_path):
            if seg_filename.endswith('.wav') or seg_filename.endswith('.flac'):
                seg_audio_file_path = os.path.join(splitted_folder_file_path, seg_filename)
                text = transcribe_audio(seg_audio_file_path)
                if text:
                    text_content += text
        with open(transcript_file_path, 'w') as file:
            file.write(text_content)

create_transcripts("\\personal")