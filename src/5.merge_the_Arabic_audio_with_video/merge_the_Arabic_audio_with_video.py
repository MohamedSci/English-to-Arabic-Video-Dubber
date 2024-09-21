from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from moviepy.video.fx.speedx import speedx
import os


def adjust_video_speed(video_clip, audio_clip):
    """Adjusts video speed to match audio duration (optional).

    Args:
        video_clip (VideoFileClip): The video clip to adjust.
        audio_clip (AudioFileClip): The audio clip.

    Returns:
        VideoFileClip: The adjusted video clip (if speed was adjusted),
                      or the original video clip otherwise.
    """

    # Check if speed adjustment is needed and adjust if so
    if video_clip.duration > audio_clip.duration:
        speed_factor = video_clip.duration / audio_clip.duration
        return speedx(video_clip, speed_factor)
    else:
        return video_clip


def process_video(vID, video_path, new_audio_path, output_folder, segment_length=5):
    """Processes a video segment with audio replacement and optional removal of subsequent segments.

    Args:
        vID (int): Video ID (might need modification for multiple audio/video pairs).
        video_path (str): Path to the video file.
        new_audio_path (str): Path to the new audio file.
        output_folder (str): Path to the output folder.
        segment_length (int, optional): Segment length in seconds. Defaults to 5.
    """

    # Load video and audio clips
    video_clip = VideoFileClip(video_path)
    new_audio_clip = AudioFileClip(new_audio_path)

    # Iterate through segments (assuming video is longer than segment_length)
    for start_time in range(0, int(video_clip.duration), segment_length):
        # Extract the segment
        segment_clip = video_clip.subclip(start_time, min(start_time + segment_length, video_clip.duration))

        # Define remaining clip (if needed)
        remaining_clip = None

        # Handle segment removal logic (optional)
        if video_clip.duration > (start_time + 3 * segment_length):
            remaining_clip = video_clip.subclip(start_time + segment_length, min(start_time + 4 * segment_length, video_clip.duration))

        # Adjust video speed if needed (optional)
        adjusted_clip = adjust_video_speed(segment_clip, new_audio_clip)

        # Replace audio and create final clip
        final_clip = adjusted_clip.set_audio(new_audio_clip)

        # Concatenate with remaining clip (if applicable)
        if remaining_clip:
            final_clip = concatenate_videoclips([final_clip, remaining_clip])

        # Define output file path
        output_file = os.path.join(output_folder, f"{vID}.{os.path.basename(video_path).split('.')[1]}.mp4")

        # Write the processed video to the output folder
        try:
            final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")
            print(f"Video processed successfully: {output_file}")
        except Exception as e:
            print(f"Error processing video: {e}")

        # Close clips to free up resources
        segment_clip.close()
        if remaining_clip:
            remaining_clip.close()
        final_clip.close()

    # Close the original video clip
    video_clip.close()


input_audio_folder = 'D:\\video_summary\\processing\\arabic_narrators\\Cutseries_film_narrated000'
input_video_folder = 'D:\\video_summary\\videos\\Cutseries_film\\new1'
output_folder = 'D:\\video_summary\\videos\\dubbed_videos\\Cutseries_film\\new1'

def main():
    audio_files_list = os.listdir(input_audio_folder)
    video_files_list = os.listdir(input_video_folder)
    vID = 0

    # Check if both lists have the same length
    if len(audio_files_list) != len(video_files_list):
        print("Error: Number of audio files does not match number of video files")
        return

    # Iterate over the lists up to the length of the shortest list
    for i in range(min(len(audio_files_list), len(video_files_list))):
        if audio_files_list[i] and video_files_list[i]:
            video_path = os.path.join(input_video_folder, video_files_list[i])
            audio_path = os.path.join(input_audio_folder, audio_files_list[i])
            process_video(vID, video_path, audio_path, output_folder)
            vID += 1
        else:
            print(f"Error: Missing audio or video file at index {i}")

if __name__ == "__main__":
    main()