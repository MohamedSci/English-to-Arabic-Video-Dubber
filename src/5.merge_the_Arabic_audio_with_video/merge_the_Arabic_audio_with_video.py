from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, VideoClip
from moviepy.video.fx.speedx import speedx
import os
from pydub import AudioSegment



def adjust_audio_speed(audio_clip):
    # Calculate duration in milliseconds
    duration_ms = len(audio_clip)
    # Define the target duration (3 minutes and 10 seconds in milliseconds)
    target_duration_ms = 3 * 60 * 1000 + 10 * 1000
    # Check if duration is more than the target duration
    if duration_ms > target_duration_ms:
        # Calculate the speed adjustment factor
        speed_factor = duration_ms / target_duration_ms
        # Adjust the speed of the audio clip
        adjusted_audio = audio_clip.speedup(playback_speed=1/speed_factor)
        return adjusted_audio
    else:
        return audio_clip



def split_video_into_segments(video_clip):
    # Split the video into segments of 3 seconds each
    segment_duration = 3  # seconds
    num_segments = int(video_clip.duration / segment_duration)
    segments = []
    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = start_time + segment_duration
        segment = video_clip.subclip(start_time, end_time)
        segments.append(segment)
    return segments

def process_video(audio_path, video_path, output_path):
    # Load audio clip
    audio_clip = AudioSegment.from_file(audio_path)
    # Adjust audio speed if needed
    adjusted_audio = adjust_audio_speed(audio_clip)
    # Load video clip
    video_clip = VideoFileClip(video_path)
    # Split video into segments
    segments = split_video_into_segments(video_clip)
    # Adjust and merge segments
    final_clips = []
    for segment in segments:
        # Adjust speed of segment to match audio duration
        speed_factor = len(adjusted_audio) / 1000 / segment.duration
        adjusted_segment = segment.speedx(speed_factor)
        final_clips.append(adjusted_segment)
  
    # Concatenate final clips
    final_clip = concatenate_videoclips(final_clips)
    # Remove original audio from segment
    final_clip = final_clip.set_audio(None)
    # Merge adjusted audio with segment
    final_clip = final_clip.set_audio(adjusted_audio)  
    # Write final clip to file
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

def main():
    # Example usage
    input_audio_folder = 'D:\\video_summary\\processing\\arabic_narrators\\Cutseries_film_narrated'
    input_video_folder = 'D:\\video_summary\\videos\\Cutseries_film'
    output_folde_path = 'D:\\video_summary\\videos\\dubbed_videos\\Cutseries_film'
    audio_files_list= os.listdir(input_audio_folder)
    video_files_list = os.listdir(input_video_folder)
        # Process each video in the input folder
    for i in range(len(audio_files_list)):
        if audio_files_list[i] and video_files_list[i]:
            output_file_path= output_folde_path+"\\"+input_audio_folder[i].split(".mp3")[0]+"\\.mp4"
            process_video(input_audio_folder +"\\"+audio_files_list[i],input_video_folder+"\\"+ video_files_list[i],output_file_path )

    

if __name__ == "__main__":
    main()




