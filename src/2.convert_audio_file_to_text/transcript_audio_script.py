import os
import speech_recognition as sr
from pydub import AudioSegment
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
# from gensim.summarization import summarize
nltk.download('punkt')

# pip install sumy

# Directory containing audio files
processing_folder = 'D:\\video_summary\\processing'
extracted_audio_folder = processing_folder+'\\audio_extracted'
segmented_audio_folder = processing_folder+'\\audio_segmented'
transcript_folder_path = processing_folder + "\\Transcripts" 
filenameDir = ""

def createFolder(file_name):
    # Specify the path for the new folder
    folder_path = extracted_audio_folder + "\\" + file_name   
    # Use os.makedirs() to create the folder for each Video Segmentation and its parents if they don't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
        print(f"Directory '{folder_path}' created successfully.")

def get_subfolders(parent_folder):
    subfolders = []
    # Walk through the directory tree
    for root, dirs, files in os.walk(parent_folder):
        # Iterate over subfolders
        for dir_name in dirs:
            # Construct the full path of the subfolder
            subfolder_path = os.path.join(root, dir_name)
            subfolders.append(subfolder_path)
    return subfolders


# # Function to summarize an English article
# def summarize_article(article_text, max_words=1500):
#     # Tokenize the article into sentences
#     sentences = nltk.sent_tokenize(article_text)   
#     # Combine the sentences into a single string
#     article_text_combined = ' '.join(sentences)   
#     # Summarize the article
#     summary = summarize(article_text_combined, word_count=max_words)    
#     return summary



def split_audio(input_file, output_folder, segment_length_ms=60000):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    audio = AudioSegment.from_file(input_file)
    # Calculate the number of segments
    num_segments = len(audio) // segment_length_ms + 1
    for i in range(num_segments):
        start_time = i * segment_length_ms
        end_time = (i + 1) * segment_length_ms
        segment = audio[start_time:end_time]
        # Output filename for each segment
        output_file = os.path.join(output_folder, f"segment_{i+1}.wav")       
        # Export the segment as a WAV file
        segment.export(output_file, format="wav")
        print(f"Segment {i+1} saved as {output_file}")








# Function to transcribe audio file
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


def splitAudios(folder_name):
# Iterate over files in the folder
    Cus_extracted_audio_folder = extracted_audio_folder + folder_name
    for filenameEx in os.listdir(Cus_extracted_audio_folder):
        splitted_folder_file_path=""
        if filenameEx.endswith('.wav') or filenameEx.endswith('.flac'):
            # Spliting Audio .... 1 ....Spliting Audio
            audio_file = os.path.join(Cus_extracted_audio_folder, filenameEx)
            filenameDir =filenameEx.split(".wav")[0]
            # Specify the path for the new folder
            splitted_folder_file_path = segmented_audio_folder + folder_name +"\\"+ filenameDir   
            # Use os.makedirs() to create the splitted audio folder and its parents if they don't exist
            if not os.path.exists(splitted_folder_file_path):
                os.makedirs(splitted_folder_file_path, exist_ok=True)
                print(f"Directory '{splitted_folder_file_path}' created successfully.")
            split_audio(audio_file,  splitted_folder_file_path)
            print(f"Audio_file '{audio_file}' Splitted successfully.")


def createTranscripts(folder_name):
        # Create a folder to hold all transcripts texts files
        Cus_segmented_audio_folder = segmented_audio_folder + folder_name
        Cus_transcript_folder_path= transcript_folder_path + folder_name
        # Use os.makedirs() to create the folder and its parents if they don't exist
        if not os.path.exists(Cus_transcript_folder_path):
            os.makedirs(Cus_transcript_folder_path, exist_ok=True)
            print(f"----- transcript_folder_path '{Cus_transcript_folder_path}' created successfully.") 
        # String variable containing text    
        
        
        
        for splitted_folder_file_path in get_subfolders(Cus_segmented_audio_folder):
            text_content=""
            transcript_file_name = ""
            transcript_file_path = ""
            print("--- splitted_folder_file_path ",splitted_folder_file_path)
            transcript_file_name = splitted_folder_file_path.split("\\")[-1]
            print("--- transcript_file_name ",transcript_file_name)
            transcript_file_path = transcript_folder_path + folder_name+ "\\"+transcript_file_name+".txt"
            print("--- transcript_file_path ",transcript_file_path)
            # Iterate over the segmented audio files to create a transcript called text_content
            for seg_filename in os.listdir(splitted_folder_file_path):
                if seg_filename.endswith('.wav') or seg_filename.endswith('.flac'):
                    seg_audio_file_path = os.path.join(splitted_folder_file_path, seg_filename)
                    text = transcribe_audio(seg_audio_file_path)
                    # Create a transcript text file to store the transcript called text_content
                    if text:
                        text_content += text 
            # Summarize the article
            # summary = summarize_article(text_content)
            print("--- Summarized Successfully ",text_content)
            # Open the file in write mode and write the text summary
            with open(transcript_file_path, 'w') as file:
                file.write(text_content)
            print("---- Text content saved to summary text file:", transcript_file_path)

createTranscripts("\\personal")            
