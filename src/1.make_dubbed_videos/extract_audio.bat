@echo off
setlocal enabledelayedexpansion

set "input_folder=D:\video_summary\videos\personal_videos"
set "output_folder=D:\\video_summary\\processing\\audio_extracted\\personal_videos_audios_extracted"

for %%i in ("%input_folder%\*.mp4") do (
    set "output_file=!output_folder!\%%~ni.wav"
    ffmpeg -i "%%i" -vn -acodec pcm_s16le -ar 44100 -ac 2 "!output_file!"
)

endlocal
