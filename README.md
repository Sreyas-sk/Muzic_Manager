# Muzic_Manager

TESTING BRANCHES

Muzic_Manager is a simple song manager that helps you keep all your music in `JSON` file.Thus in an adverse case of loosing your music collection, restoring it is jsut a command away.

#### Check out the [Latest Updates!!](https://github.com/Sreyas-sk/Muzic_Manager/blob/master/Update_log.md)

> 👀 **NOTE :** The script can only download primarily youtube songs or any link that youtube-dl supports.
> 
> But dont think of this as a limitation because if you think about it most of the music that you and me listen primirly comes from youtube!! 😎

## PRE REQUISITE :triangular_flag_on_post:


- Youtube-dl
- Python 3.7+ (OPTIONAL)
- FFmpeg (OPTIONAL) 

## SETTING UP :gear:

###  Youtube-dl 

For Windows

- Dowload[Youtube-dl.exe](https://yt-dl.org/latest/youtube-dl.exe) and add it to the path variable

For Mac

- Download using Homebrew :beer: 

```
brew install youtube-dl
```

Or

Follow the official git repository [Youtube-dl](https://github.com/ytdl-org/youtube-dl)


### FFmpeg (OPTIONAL) :movie_camera:

Official [FFmpeg](https://ffmpeg.org/download.html#repositories) website

FFmpeg is an open source tool to handle manipulation of audio and video files.In this project FFmpeg is used to convert downloaded files to the required audio format specified by the user. 

:thought_balloon: This tool is not a requirement unless you wish to have songs in other formats like `mp3`, `FLAC` and so on...

>By default the audio format is `m4a`. This format consumes less space and provides decent quality of music (128kbps) better than `mp3` format. Although most of the music players out there supports this format, its not an absolute guarantee, so its best to check with your favourite music player. 

## PYTHON (OPTIONAL) :snake:

Set up python if you intend to run the tool directly using scripts

## INITIAL SET UP :tv:

- Download the latest release
- Extract the downloaded zip
- Rename the extracted folder to **Muzic_Manager**
>:warning: **NOTE :**  Renaming is an essential step. If not done, the program breaks
    
- Open CLI in the folder and run the following command. This sets up the required files and folders
    
    ```
    ./Muzic_Manager
  ```
    

## FOLDER STRUCTURE 

This is the folder structure the initial setup creates.

```
Root Folder ( Your Folder with cloned repo )
│
│ Downloaded songs from download.JSON
│
└─ Muzic_Manager
│  │	Muzic_Manager.py	
│  │	README.md
│  │	Update_log.md
│  │	log.txt
│  │	download.JSON
│  │	malayalam.JSON
│  │	hindi.JSON
│  │	tamil.JSON
│  │	west.JSON
│
└─ TEKKU
│  │
│  │  Downloaded songs from malayalam.JSON
│  │
│
└─ BOLLY
│  │
│  │  Downloaded songs from hindi.JSON
│  │
│
└─ TAMIZH
│  │
│  │  Downloaded songs from tamil.JSON
│  │
│
└─ WEST
│  │
│  │  Downloaded songs from west.JSON
│  │
```

## USAGE :art:

```
./Muzic_Manager [OPTIONS]
```

### OPTIONS :game_die:

```
$ ./Muzic_Manager --help
usage: Muzic_Manager.py [-h] [-F {M,H,T,W,D}] [-L LINK] [-O NAME]

optional arguments:
  -h, --help            show this help message and exit
  -F {M,H,T,W,D}, --file_name {M,H,T,W,D}
                        To download a specific list of songs
  -L LINK, --link LINK  Pass the link to download individual song
  -O NAME, --name NAME  Give name to file or else name from URL will be used.
```

By Default the script checks all the following files and tries to download all the songs which are not downloaded.

- `download.JSON`
- `malayalam.JSON`
- `tamil.JSON`
- `hindi.JSON`
- `west.JSON`

If you want to selectively download songs from a file the -F argument is passed follwed by the letter denoting the file

```
./Muzic_Manager -F D
```

The above command only checks the download.JSON file and downlods any undownloaded songs. For more info refer **OPTIONS** section

> 💡**NOTE :**
> All the downloaded songs have "Hash" value "\[#\]" and songs which are not downloaded or had error during download has "Hash" value "\[ \]"

### ADDING LINKS :link:

There are three ways to add new songs to the collection.

### METHOD I :white_check_mark:

This is the easiest method to adding details to `.JSON` files. Use the `Append.py` tool. Run the program and follow the instructions to add links to respective files.

```
./Append
```

By default `download.JSON` is selected.

You can select specific files by passing the -F parameter

```
./Append -F H
```

The above command selects `hindi.JSON` to add songs

### METHOD II :ballot_box_with_check:

In this method the song details are manually added to the respective JSON files in JSON format. Then `Muzic_Manager.py` is run and the song gets downloaded.

The songs needs to be added in the followong format in the `.JSON` files

```
 {
    "S1": {
        "Hash": "[ ]",
        "Name": "Song1 Name",
        "URL": "URL from Youtube",
        "Format": ".m4a",
        "cover": "{path_to_cover_picture}"
    },
    "S2": {
        "Hash": "[ ]",
        "Name": "Song2 Name",
        "URL": "URL from Youtube",
        "Format": ".m4a",
        "cover": "{path_to_cover_picture}"
    }
}
```

> NOTE
> Take care of the spaces and notations while manually adding details as uneven data can lead to failure during execution.

### METHOD III :airplane:

The second method is if you dont want the hassle of writting all the details in the file. You can download a song on the fly with just the link passing the -L argument followed by the link.

```
./Muzic_Manager -L "LINK"
```

You can passes a name to the downloded music using the -O argument followed by the name in double quotes

```
./Muzic_Manager -L "LINK" -O "NAME_OF_SONG"
```

> Here if none of the files are specified using the -F argument then the song detials are added to the default `download.JSON` file.

With this method the song if downloaded gets added to the download.JSON ( by default ) file with all properties.

## UPCOMING UPDATES 🔥

- Tool to add Cover Art (Extending the tool to other metadata under consideration) ❗️
- Adding deletion and updation feature in Append tool ❗️
- Download all the songs again **OVERRIDE** :❗️
- Remove extension condition for files ✅
- Adding crl+C ❗️
- Timeout process either too slow or not responding ✅
- Identify if the network is slow ❗️

## CONCLUSION :checkered_flag:

The project might look a bit tedious but when you get the hang of it its pretty simple.Hope you have a fun time setting this up and using the scripts.

Keep track of all your muzic and keep enjoying the beats 🎶😉
