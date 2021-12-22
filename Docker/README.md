# DOCKER IMPLEMENTATION
## PREREQUISITES
- Git 
- Docker installed and running

## 1. BUILD IMAGE

- create a directory where you want to keep your files and `cd` into it
    ```
    mkdir ~/music
    cd /music
    ```
- clone this repository
    ```
    git clone https://github.com/Sreyas-sk/Muzic_Manager.git
    ```
- change directory into `/Docker` in the cloned repository
    ```
    cd Muzic_Manager/Docker
    ```
- `Run docker build` with the following parameters
    ````
    docker build -t Muzic_Manager .
    ````
- The image will be created and will be available among docker images
    ```
    $ docker images
    ```

## 2. RUN CONTAINER
- Run the following command
    ```
    docker run -it --name Muzic_Manager -v ~/music:/music Muzic_Manager
    ```

The above command gives you an interactive shell with which you can interact with the container. The container is associated with the local directory `~/music` which was created earlier.

## 3. DOWNLOADING SONGS

Downloading songs remains the same as is documented in the `root` folder of this repository  [Muzic_Manager](https://github.com/Sreyas-sk/Muzic_Manager).

**ENVIRONMENT VARIABLE** 

The image is configured with command **`music`** which can be used in place of **`python Muzic_Manager.py`**

For example
````
music -F H
````
This will download all undownloaded songs from file `hindi.JSON`

**OR**

```
music -F D -L <Link> -O "NAME_OF_SONG"
```
which download the song from the given link, renames the file to the given file name and stores song detials in `download.JSON` file