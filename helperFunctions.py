import os
from moviepy.editor import VideoFileClip
import datetime

MONTH_DICT = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
              '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}


def get_all_file_extensions_in_folder(full_absolute_folder_path):
    """
    Receives: the FULL ABSOLUTE FILE PATH to given FOLDER
    Returns: a List with all the extensions in the given folder
    """
    all_extensions = []
    for item in os.listdir(full_absolute_folder_path):
        extension, filename = get_extension_and_filename(item)
        if extension not in all_extensions:
            all_extensions.append(extension)
    return all_extensions


def get_extension_and_filename(input_file):
    """
    Receives: a filename
    Returns: file extension and file name (in that order)
    """
    file_extension = input_file[::-1].split('.')[0][::-1]
    file_name = input_file[::-1].split('.')[1][::-1]
    return file_extension, file_name


def get_video_duration(full_absoluter_filepath_to_video_file):
    """
    Receives: the FULL ABSOLUTE FILE PATH to given VIDEO file
    Returns: a FLOAT with the video duration in SECONDS
    """
    try:
        clip = VideoFileClip(full_absoluter_filepath_to_video_file)
        duration = clip.duration
        return duration
    except:
        return 'File is most likely not a video. Please check.'


def get_file_creation_date(full_absolute_filepath_to_file):
    """
    Receives: the FULL ABSOLUTE FILE PATH to given FILE
    Returns: a STRING with format yyyy-mm-dd (example: 2023-01-02)

    BIG NOTE:
    The date will only be CORRECT when you are dealing with 100% ORIGINAL FILES

    What does that mean?
    Well, let me illustrate:
    Let us say, I shot a video in Egypt on 2022-03-09, and then I uploaded it to my hard drive on 2022-04-01
    If I retrieve the creation date of the original video that was shot on 2022-03-09 and uploaded to my hard drive on 2022-04-01,
    The creation date will be 2022-03-09, which is CORRECT, nothing out of the ordinary.

    HOWEVER,
    If I copy/paste the original video (which had been uploaded to my hard drive on 2022-04-01),
    on 2023-01-25, essentially creating a duplicate video, when I retrieve the creation date of the duplicate video,
    the creation date will be 2022-04-01, the DAY THE ORIGINAL VIDEO WAS UPLOADED
    """
    timestamp_creation_date = os.stat(full_absolute_filepath_to_file).st_birthtime
    creation_date = str(datetime.datetime.fromtimestamp(timestamp_creation_date))[0:10]
    return creation_date


def destructure_file_creation_date(full_absolute_filepath_to_file):
    """
    Receives: absolute file path of a file
    Returns: file's creation year, creation month number (e.g. 02 for February), creation month name (in order)
    """
    creation_date = get_file_creation_date(full_absolute_filepath_to_file)
    year, month_number, day_number = creation_date.split('-')
    month_name = MONTH_DICT[month_number]
    return year, month_number, month_name
