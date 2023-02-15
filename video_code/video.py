import os
import subprocess

# Set the input and output folders
input_folder = '/home/mussab/videos_input_folder'
output_folder = '/home/mussab/video_output_folder'

# Set the codec and format for the output videos
codec = 'h264'
format = 'mp4'

# Loop through all the video files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith('.mp4') or file_name.endswith('.avi'):
        # Set the input and output file paths
        input_path = os.path.join(input_folder, file_name)
        output_file_name = os.path.splitext(file_name)[0] + '.' + format
        output_path = os.path.join(output_folder, output_file_name)

        # Run FFmpeg command to convert the video
        command = f'ffmpeg -i "{input_path}" -vcodec {codec} "{output_path}"'
        subprocess.call(command, shell=True)
