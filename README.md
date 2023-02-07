# Custom Automation - File Management

In this project, I created several scripts which allowed me to sort photos
and videos on my hard drive. For the longest time I have had all my files 
unorganized within a folder: thousands of photos and videos from throughout 
the years without any type of labelling. Manually cataloguing each file would 
not be acceptable, as there are simply way to many (the main reason why I 
never organized them). So, I decided to do something about it and made 
several scripts to organize my files. Even though the scripts are similar 
between each other, each script deals with a particular use case.

Let us go over each .py file:

### helperFunctions.py
Provides some functions which are crucial for the execution of the scripts.

### filepaths.py

Stores the necessary filepaths, so they do not clutter other .py files.

### extractAudioFromVideo.py
I am a guitar player, and I recorded many musical ideas by placing the 
phone down and recording a video. I felt having the video part was 
redundant, since only the audio was important. Therefore, I used this 
script to extract the audio from the video and save it in its 
separate audio file. I saved all audio files in a particular folder.

### sortFilesInFolder.py
Extracts the creation date of every file in a given base folder and 
sorts each file inside a month folder, which itself is 
inside a year folder, with the month and the year folders representing the 
month and year in which the file was created, respectively.
The year folders can be saved within the base folder, or in some other 
folder of the user's choice.

Note: Third-party users may find these scripts helpful to perform some kind
of automatic organization task.
