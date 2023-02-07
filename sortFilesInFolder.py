import os
from helperFunctions import destructure_file_creation_date, get_extension_and_filename
from filepaths import your_source_folder, your_destination_folder

""" 
This script sorts every file in a given folder by year and month.
Personally, I used this script to sort my photos and videos.

Note: if you want to sort the file within the same folder, you can always give both arguments the same value
Example:

folder_to_organize_filepath = 'my_folder_filepath'
folder_to_send_files_to = 'my_folder_filepath'
sort_files_by_year_and_month(folder_to_organize_filepath, folder_to_send_files_to)
"""


def sort_files_by_year_and_month(source_folder_to_organize_filepath, send_to_folder_filepath):
    for current_file in os.listdir(source_folder_to_organize_filepath):
        source_filepath = fr'{source_folder_to_organize_filepath}/{current_file}'
        extension, filename = get_extension_and_filename(current_file)

        # sometime Python recognises and hidden file as beginning with a " _ " instead of a " . "
        # therefore, I considered both scenarios juts to be sure
        if filename.startswith('_') or filename.startswith('.'):
            # if the file is a hidden file, return immediately
            return

        year, month_number, month_name = destructure_file_creation_date(source_filepath)

        final_folder = fr'{send_to_folder_filepath}/{year}/{month_number} - {month_name}'

        if not os.path.exists(final_folder):
            os.makedirs(final_folder)

        destination_filepath = fr'{final_folder}/{current_file}'
        os.rename(source_filepath, destination_filepath)


# sort_files_by_year_and_month(your_source_folder, your_destination_folder)
