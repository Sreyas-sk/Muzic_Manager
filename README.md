# Muzic_Manager

Muzic_Manager is a simple song manager that helps you keep all your music in  `JSON`  file. Thus in an adverse case of loosing your music collection, restoring it is jsut a command away. 

> NOTE : The script can only download primarily youtube songs or any link that youtube-dl supports.

## PRE REQUISITE

- Python setup
- FFmpeg
- Youtube-dl

## SETTING UP

### FFmpeg

Official [FFmpeg](https://ffmpeg.org/download.html#repositories) website

### Youtube-dl

For Windows

- Dowload[Youtube-dl.exe](https://yt-dl.org/latest/youtube-dl.exe) and add it to the path variable

For Mac

- Download using Homebrew

```
brew install youtube-dl
```

Or

Follow the official git repository [Youtube-dl](https://github.com/ytdl-org/youtube-dl)

## INITIAL SET UP

-  Clone this repo
- Run the following command. This sets up the required files and folders

	```
	python Muzic_Manager.py
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

## USAGE

```
python Muzic_Manager [OPTIONS]
```

### OPTIONS

```
$ python Muzic_Manager.py --help
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
python Muzic_Manager.py -F D
```

The above command only checks the download.JSON file and downlods any undownloaded songs. For more info refer **OPTIONS** section

> **NOTE :** 
> All the downloaded songs have "Hash" value "[#]" and songs which are not downloaded or had error during download has "Hash" value "[ ]"

### ADDING LINKS

There are three ways to add new songs to the collection.

### METHOD I
This is the easiest method to adding details to `.JSON` files. Use the `Append.py`  tool. Run the program and follow the instructions to add links to respective files. 
````
python Append.py
````
By default `download.JSON`  is selected.

You can select specific files by passing the -F parameter
````
python Append.py -F H
````
The above command selects `hindi.JSON` to add songs

### METHOD II

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

>NOTE
>Take care of the spaces and notations while manually adding details as uneven data can lead to failure during execution.

### METHOD III

The second method is if you dont want the hassle of writting all the details in the file. You can download a song on the fly with just the link passing the -L argument followed by the link. 
```
python Muzic_Manager.py -L <LINK>
```

You can passes a name to the downloded music using the -O argument followed by the name in double quotes

```
python Muzic_Manager.py -L <LINK> -O "NAME_OF_SONG"
```

>Here if none of the files are specified using the -F argument then the song detials are added to the default `download.JSON` file.

With this method the song if downloaded gets added to the download.JSON ( by default ) file with all  properties.

## UPCOMING UPDATES

- Download all the songs again **OVERRIDE**
- Remove extension condition for files	 [#]
- Adding crl+C
- Timeout process either too slow or not responding  [#]
- Identify if the network is slow

## CONCLUSION

The project might look a bit tedious but when you get the hang of it its pretty simple.Hope you have a fun time setting this up and using this script.

Keep track of all you muzic and keep enjoying the beats 🎶😉