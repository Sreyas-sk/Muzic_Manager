# Version 3.3.0
 - Publishing the first release for the project **Muzic_Manager v3.3.0**
 - Removing python as a dependency
 - Removing ffmpeg as a dependency
 - Converted all python scripts to standalone binaries
 - Updated README to accomodate latest changes
 - Added Append tool to add songs from CLI instead of directly editting the respective JSON files
 - Deletion and updation features will be added in future 
# Version 3.2.2
- Found youtube has audio only download by passing format agument as 140 (.m4a)
- Using -f 140 avoids the post download extracting of audio using FFmpeg
- Handling youtube and generic links separately
- Added properties modified-time and cover
- Cover property expects a valid location to a cover art 
- Tool to add cover art to songs will be added in future updates, for now its just a backbone laid out. 
# Version 3.2.1
- Shifting from CSV to JSON
- Conversion script ToJSON.py converts the existing CSV to JSON format
- Download script that downloads using JSON file
# Version 3.2
- Download directly from CLI passing a link
- Pass -F followed by choice to update the download link to the respective category of file
- Pass -O or --name <download_name.extension> to give name to the downloading song
For more info on downloading using links use --help while execution
- Added timeout for download process (current timeout 4 mins,but can be changed with set_timeout variable)
# Version 3.1
- Minor fixes
# Version 3.0
- Added individual downloading of musics of malayalam,hindi,tamil,west and a default
- The default is for keeping other music links
- Individual downloading is done by passing the flag -F or --file_name while executing the program with values [M,H,T,W] which represents the corresponding files to look for for downloading

````py
$ python Muzic_Manager.py -F H
````
- If no file is passed all the music files will be searched and all undownloaded files will be downloaded
- Different language musics are stored in separate folders with corresponding folder names
- Fixed a bug that causes a mishandling of the file names
# Version 2.0
- Changed the format of adding links
- In previous version the link and the title were separated using space hence the title could not have any space thus '_' had to be used instead
- Now the space is removed instead ';' is used to separate link and title thus from this version title can have spaces
# VERSION 1.0
- Add links to the download.txt file and the program downloads links on each line