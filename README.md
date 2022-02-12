# Muzic_Manager

Muzic_Manager is a simple song manager that helps you keep all your music in `JSON` file.Thus in an adverse case of loosing your music collection, restoring it is jsut a command away.

#### Check out the [Latest Updates!!](https://github.com/Sreyas-sk/Muzic_Manager/blob/master/Update_log.md)

> 👀 **NOTE :** The script can only download primarily youtube songs or any link that youtube-dl supports.
> 
> But dont think of this as a limitation because if you think about it most of the music that you and me listen primirly comes from youtube!! 😎

## PRE REQUISITE 🚩

- Youtube-dl
- Python 3.7+ (OPTIONAL)
- FFmpeg (OPTIONAL)

## SETTING UP ⚙️

### Youtube-dl

For Windows

- Dowload[Youtube-dl.exe](https://yt-dl.org/latest/youtube-dl.exe) and add it to the path variable

For Mac

- Download using Homebrew 🍺

```
brew install youtube-dl
```

Or

Follow the official git repository [Youtube-dl](https://github.com/ytdl-org/youtube-dl)

### FFmpeg (OPTIONAL) 🎥

Official [FFmpeg](https://ffmpeg.org/download.html#repositories) website

FFmpeg is an open source tool to handle manipulation of audio and video files.In this project FFmpeg is used to convert downloaded files to the required audio format specified by the user.

💭 This tool is not a requirement unless you wish to have songs in other formats like `mp3`, `FLAC` and so on...

> By default the audio format is `m4a`. This format consumes less space and provides decent quality of music (128kbps) better than `mp3` format. Although most of the music players out there supports this format, its not an absolute guarantee, so its best to check with your favourite music player.

## PYTHON (OPTIONAL) 🐍

Set up python if you intend to run the tool directly using scripts

## INITIAL SET UP 📺

- Download the latest release
- Extract the downloaded zip
- Rename the extracted folder to **Muzic_Manager**

> ⚠️ **NOTE :** Renaming is an essential step. If not done, the program breaks

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

## USAGE 🎨

```
./Muzic_Manager [OPTIONS]
```

### OPTIONS 🎲

```
$ ./Muzic_Manager --help
usage: Muzic_Manager.py [-h] [-F {M,H,T,W,D}] [-L LINK] [-O NAME] [--over-ride] [--destination DESTINATION]
                        [--over-ride-format {m4a,mp3,opus,FLAC}]

optional arguments:
  -h, --help            show this help message and exit
  -F {M,H,T,W,D}, --file_name {M,H,T,W,D}
                        To download a specific list of songs
  -L LINK, --link LINK  Pass the link to download individual song
  -O NAME, --name NAME  Give name to file or else name from URL will be used.
  --over-ride           Used to download all songs again
  --destination DESTINATION
                        To download songs to new location
  --over-ride-format {m4a,mp3,opus,FLAC}
                        This format will be used to download all songs
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

### ADDING LINKS 🔗

There are three ways to add new songs to the collection.

### METHOD I ✅

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

### METHOD II ☑️

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

### METHOD III ✈️

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

## OVER-RIDE FEATURE

The **Over-ride Feature Suit** added with **V3.4.0** includes 3 inter usable arguments that can be passed while managing your songs

- **--over-ride** : Used to re-download all songs from the list of downloaded songs
- **--over-ride-format** : Used to change the format of exiting songs while over-riding. This can also be used while following **method III**
- **--destination** : Used to download the songs to a specific location if the provided location is valid or else the songs are downloaded to folder named **Downloads**
    

**EXAMPLE - 1**

```
./Muzic_Manager --over-ride
```

The above command re-downloads all the song from all `JSON` file and replaces the existing files.

**EXAMPLE - 2**

```
./Muzic_Manager --over-ride --over-ride-format mp3
```

The above command give the same results as **--over-ride** but the format will be mp3.

> NOTE
> Here the existing files will only be replaced if the format is same as mp3

**EXAMPLE - 3**

```
./Muzic_Manager --over-ride --destination "../New_Download"
```

The above command downloads all the songs from all `JSON` files to the destination **. . /New_Download**

**EXAMPLE - 4**

```
./Muzic_Manager -L "LINK" -O "NAME_OF_SONG" --destination "../New_Folder" --over-ride-format mp3 
```

Here the song with the given link and name will be downloaded into folder **. . /New_Folder** with the format **.mp3**

> NOTE
> Here the details wont be updated in the JSON file

The above discussed commands are just a few combinations that can used. These arguments can be mixed and matched for your needs.The **-F** argument can also be used with these combinations

## UPCOMING UPDATES 🔥

- Tool to add Cover Art (Extending the tool to other metadata under consideration) ❗️
- Adding deletion and updation feature in Append tool ❗️
- Download all the songs again **OVERRIDE** : ✅
- Remove extension condition for files ✅
- Adding crl+C  ✅
- Timeout process either too slow or not responding ✅

## CONCLUSION 🏁

The project might look a bit tedious but when you get the hang of it its pretty simple.Hope you have a fun time setting this up and using the scripts.

Keep track of all your muzic and keep enjoying the beats 🎶😉