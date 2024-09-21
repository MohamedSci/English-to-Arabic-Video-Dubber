**English to Arabic Video Dubber**

This Python project automatically dubs English videos into Arabic videos. 

**Features**

* Extracts audio from English videos
* Transcribes the extracted audio into English text
* Translates the English text into Arabic text
* Generates Arabic audio from the translated text
* Merges the generated Arabic audio with the original video

**Requirements**

* Python 3.x
* ffmpeg ([https://ffmpeg.org/](https://ffmpeg.org/))
* External libraries (see Installation)

**Installation**

1. Clone this repository:

```bash
git clone https://github.com/<your_username>/english_to_arabic_video_dubber.git
```

2. Install required libraries:

   Create a requirements.txt file with the following content:

   ```
   pydub
   moviepy
   googletrans
   gTTS
   # Add other required libraries here
   ```

   Then install the libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

3.  (Optional) Set up Google Cloud Text-to-Speech and Translate APIs (for improved quality and features):

   * Create a Google Cloud project and enable the Text-to-Speech and Translate APIs.
   * Create a service account and download the credentials file (JSON).
   * Configure the script to use your credentials file (see Usage).

**Usage**

```bash
python main.py --input_video <path/to/video.mp4> --output_video <path/to/output.mp4> [--target_voice <voice_name>] [--credentials <path/to/credentials.json>]

--input_video          Path to the English video file
--output_video         Path to the output Arabic video file (optional, defaults to input_video_dubbed.mp4)
--target_voice         Target voice name for Google Text-to-Speech (optional, see Google Cloud documentation for available voices)
--credentials         Path to your Google Cloud credentials file (optional, required for Text-to-Speech and Translate APIs)
```

**Example**

```bash
python main.py --input_video "my_english_video.mp4" --output_video "arabic_dubbed_video.mp4" --target_voice "ar-US-Wavenet-A" --credentials "my_credentials.json"
```

**Development**

This project is under development. Feel free to contribute by creating pull requests!

