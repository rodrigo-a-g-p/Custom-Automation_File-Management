import time
import moviepy.editor as mp
import os
from helperFunctions import destructure_file_creation_date
from filepaths import your_source_video_folder, your_destination_audio_folder

"""
This script extracts the audio from every video file in a particular folder and saves the audio in its particular 
audio file in a designated folder
"""


def extract_and_save_audio_files(original_filepath, filepath_to_save):
    for index, file in enumerate(sorted(os.listdir(original_filepath))):

        # If it's a hidden file, do nothing
        if not file.startswith('.') or file.startswith('_'):
            file_location = f'{original_filepath}/{file}'
            year, month_number, month_name = destructure_file_creation_date(file_location)
            save_folder_path = f'{filepath_to_save}/{year}/{month_number} - {month_name}'

            # Create folder with creation_year if it does not exist
            if not os.path.exists(save_folder_path):
                os.makedirs(save_folder_path)

            # Designate file name
            save_here = f'{save_folder_path}/riff_{index + 1}.mp3'

            my_clip = mp.VideoFileClip(fr"{file_location}")
            my_clip.audio.write_audiofile(fr"{save_here}")

            time.sleep(2)


# extract_and_save_audio_files(your_source_video_folder, your_destination_audio_folder)
