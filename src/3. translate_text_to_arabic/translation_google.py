import os
import time
from googletrans import Translator

def translate_text(text, dest='ar', max_retries=3):
    translator = Translator()
    for i in range(max_retries):
        try:
            translated = translator.translate(text, dest=dest)
            return translated.text
        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"Retrying... ({i+1}/{max_retries})")
            time.sleep(1)
    print("Translation failed after retries.")
    return None

def translate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    translated_text = translate_text(text)
    if translated_text:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated_text)
        print(f"Translation of {input_file} complete.")
    else:
        print(f"Translation of {input_file} failed.")

def translate_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.txt'):
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name)
            translate_file(input_file, output_file)

if __name__ == "__main__":
    input_folder = 'D:\\video_summary\\processing\\Transcripts'
    output_folder = 'D:\\video_summary\\processing\\arabic_transcripts'
    translate_folder(input_folder, output_folder)
    print("All translations complete.")