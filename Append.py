########################################################
# Muzic Manager Append Tool
# Current Version : 1.0
# Description: To add music to JSON files
# Author : Sreyas S
########################################################

import argparse
import time
import json

parser = argparse.ArgumentParser()
parser.add_argument("-F","--file_name",help="To download a specific list of songs",choices=["M","H","T","W","D"])
arg = parser.parse_args()

files = ["malayalam.JSON","hindi.JSON","west.JSON","download.JSON","tamil.JSON",]
refer = arg.file_name
if not arg.file_name:
    arg.file_name = files[3]
elif arg.file_name == "M":
    arg.file_name = files[0]
elif arg.file_name == "H":
    arg.file_name = files[1]
elif arg.file_name == "w":
    arg.file_name = files[3]
elif arg.file_name == "d":
    arg.file_name = files[3]
elif arg.file_name == "T":
    arg.file_name = files[4]


def intro () :
    print("########################################################")
    print("# Muzic Manager Append Tool")
    print("# Current Version : 1.0")     
    print("########################################################")
    return 0

def append(Name,URL,Format):
    try:
        with open(arg.file_name,"r") as f:
                song_collection = json.load(f)
    except:
        print("Unable to open {}".format(arg.file_name))
        return 100

    keys=list(song_collection)
    new_key=str(int(keys[-1][1:])+1)
    letter=keys[-1][0]
    
    
    song_collection[letter+new_key]={}
    song_collection[letter+new_key]["Hash"]="[ ]"
    song_collection[letter+new_key]["Name"]=Name
    song_collection[letter+new_key]["URL"]=URL
    song_collection[letter+new_key]["Cover"]=""
    song_collection[letter+new_key]["Format"]=Format
    song_collection[letter+new_key]["Modified"]=time.ctime(time.time())

    song_data = open(arg.file_name,"w+")
    song_data.write(json.dumps(song_collection,indent=4))
    song_data.close()
    
    return 0

if __name__ == '__main__':

    intro()
    
    print("Appending file {}".format(arg.file_name))
    exit = False
    
    while exit!=True:
        print("Enter Song Details")
        print("Name: ",end="")
        name = input()
        print("URL: ",end="")
        URL = input()
        print("Format: ",end="")
        format = str(input() or "m4a")

        status=append(name,URL,format)

        if status==100:
            print("EXITING......")
            print("Run \n$ python Muzic_Manager -F {}".format(refer))
            print("This will create the required base file")
            break
        
        print("Successfully added details!!")
        con=input("would you like to add more to {}? (yes/no)".format(arg.file_name))
        if con.lower()=="yes":
            continue
        else:
            exit = True
            print("Run \n$ python Muzic_Manager -F {}".format(refer))
            print("To download the song")
    