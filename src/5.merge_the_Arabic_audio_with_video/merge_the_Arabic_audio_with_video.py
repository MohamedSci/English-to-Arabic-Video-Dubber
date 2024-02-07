from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from moviepy.video.fx.speedx import speedx
import os


def adjust_video_speed(video_clip,audio_clip):
    # Perform speed adjustment here if necessary
    speed_factor = video_clip.duration / audio_clip.duration  # Double the speed
    return speedx(video_clip, speed_factor)


def process_video(vID,video_path, audio_folder, output_folder):
    # Load the original video clip
    video_clip = VideoFileClip(video_path)
    # Get the duration of the video clip
    duration = video_clip.duration
    # Define the segment length (in seconds)
    segment_length = 5

    # Iterate through each segment
    for i in range(0, int(duration), segment_length):
        if i>0:
            break
        # Extract the segment
        if min(i + segment_length, duration) > i:
            segment_clip = video_clip.subclip(i, min(i + segment_length, duration))
        # Remove the following three segments
        if duration > (i + 3 * segment_length):
            remaining_clip = video_clip.subclip(i, min(i + segment_length, duration))
        # Concatenate the remaining clip with the current segment
        final_clip = concatenate_videoclips([segment_clip, remaining_clip])
        # Load new audio clip from the input folder
        audio_files = os.listdir(audio_folder)
        audio_file = audio_files[i // segment_length % len(audio_files)]  # Choose audio based on segment
        new_audio_path = os.path.join(audio_folder, audio_file)
        new_audio_clip = AudioFileClip(new_audio_path)
                    # Adjust video speed if needed
        adjusted_clip = adjust_video_speed(video_clip,new_audio_clip)
        # Replace the original audio with the new audio
        final_clip = adjusted_clip.set_audio(new_audio_clip)
         # Define the output file path
        output_file = os.path.join(output_folder, f"{vID}.{os.path.basename(video_path).split('.')[1]}.mp4")
        # Write the processed video to the output folder
        final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        # Close the clips to free up resources
        segment_clip.close()
        remaining_clip.close()
        final_clip.close()
    # Close the original video clip
    video_clip.close()



# Define input and output folders
input_video_folder = 'D:\\video_summary\\videos\\Cutseries'
output_folder = 'D:\\video_summary\\videos\\dubbed_videos'
input_audio_folder = 'D:\\video_summary\\processing\\arabic_narrators'




def main():
    audio_files_list= os.listdir(input_audio_folder)
    video_files_list = os.listdir(input_video_folder)
    vID=0
    # Process each video in the input folder
    for i in range(len(audio_files_list)):
        if audio_files_list[i] and video_files_list[i]:
            video_file=video_files_list[i]
            if video_file.endswith(".mp4"):
                video_path = os.path.join(input_video_folder, video_file)
                process_video(vID,video_path, input_audio_folder, output_folder)
                vID = vID +1

if __name__ == "__main__":
    main()        
