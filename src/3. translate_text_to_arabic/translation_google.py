# If you're looking for a free solution, you can utilize the translate method available in the googletrans library. This library provides a simple interface for Google Translate API, which is free to use within certain limits. Please note that the usage limits for Google Translate API apply, and it's always a good idea to review the current terms of service for any changes in limitations or pricing.

# Here's how you can modify the script to use googletrans for translation:

# pip install googletrans==4.0.0-rc1

#  Need Paid plan 20 $ or 80$ As the Free plan has 500000 Char/month

import os
import time
from googletrans import Translator

def translate_text(text, dest='ar', max_retries=3):
    """
    Translates the input text to the target language using googletrans.
    
    Args:
        text (str): The text to be translated.
        dest (str): The target language code. Defaults to 'ar' for Arabic.
        max_retries (int): Maximum number of retries in case of connection errors. Defaults to 3.
        
    Returns:
        str: The translated text.
    """
    translator = Translator()
    for i in range(max_retries):
        try:
            translated = translator.translate(text, dest=dest)
            return translated.text
        except Exception as e:
            print(f"An error occurred: {e}")
            print(f"Retrying... ({i+1}/{max_retries})")
            time.sleep(1)  # Wait before retrying
    print("Translation failed after retries.")
    return None

def translate_file(input_file, output_file):
    """
    Translates the contents of the input file to Arabic and saves the translated text to the output file.
    
    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to save the translated text file.
    """
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
    """
    Translates all text files in the input folder to Arabic and saves the translated text files to the output folder.
    
    Args:
        input_folder (str): Path to the folder containing input text files.
        output_folder (str): Path to the folder to save translated text files.
    """
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
