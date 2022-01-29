########################################################
# Muzic Manager
# Current Version : 3.2.2 
# Description: Shifting from CSV to JSON
# Author : Sreyas S
########################################################
import subprocess
import time
from os import remove,rename
from os import chdir,curdir,mkdir,getcwd
import argparse
import json
######################### PRIMARY SETTING ##############################################
cmd_generic=["youtube-dl","-x","--audio-quality", "0","--audio-format","m4a"] #Download command
cmd_youtube=["youtube-dl","-f","140","--audio-format","m4a"] #Download command

# Log file to keep track of the errors    
log = open("log.txt","a")

set_timeout = 240   # In seconds

######################### ARGUMENT SETTINGS ############################################

# Setting up argument to be captured from the console
parser=argparse.ArgumentParser()
parser.add_argument("-F","--file_name",help="To download a specific list of songs",choices=["M","H","T","W","D"])
parser.add_argument("-L","--link",help="Pass the link to download individual song")
parser.add_argument("-O","--name",help="Give name to file or else name from URL will be used.")
parser.add_argument("--over-ride",help="Used to download all songs again",action="store_true")
parser.add_argument("--destination",help="To download songs to new location with over-ride",action="store_true")
parser.add_argument("--over-ride-format",help="This format will be used to download all songs",choices=["m4a","mp3","opus","FLAC"])
arg = parser.parse_args()


files={"malayalam":["malayalam.JSON","../TEKKU"],"hindi":["hindi.JSON","../BOLLY"],"tamil":["tamil.JSON","../TAMIZH"],"west":["west.JSON","../WEST"],"default":["download.JSON",".."]} 

# Changing directory according to the argument passed

if not arg.file_name:
    arg.file_name=[files["malayalam"],files["hindi"],files["tamil"],files["west"],files["default"]]
    #dr_name=".."
elif arg.file_name=="M":
    arg.file_name=[files["malayalam"]]
    #dr_name="../TEKKU" 
elif arg.file_name=="H":
    arg.file_name=[files["hindi"]]
    #dr_name="../BOLLY"
elif arg.file_name=="T":
    arg.file_name=[files["tamil"]]
    #dr_name="../TAMIZH"
elif arg.file_name=="W":
    arg.file_name=[files["west"]]
    #dr_name="../WEST"
elif arg.file_name=="D":
    arg.file_name=[files["default"]]

if arg.over_ride_format:
    cmd_generic[5]=arg.over_ride_format

######################### FUNCTION DEFENITIONS ############################################

def intro () :
    print("########################################################")
    print("# Muzic Manager")
    print("# Current Version : 3.2.2")     
    print("########################################################")
    return 0

def console_out(line_out,line_log=log):
    print(line_out)
    if line_log!=None:
        line_log.write(line_out)
    return 0

def dir_manage(dname):
    try:
        chdir(dname)
    except FileNotFoundError:
        console_out("\nNo Directory {} Found".format(dname.strip("../")))
        console_out("\nCreating Directory {}".format(dname.strip("../")))
        mkdir(dname)
        chdir(dname)
    return 0

def Exception_error(f_name):
    
    console_out("Download file not found")
    console_out("Creating file "+str(f_name))
    url_list=open(f_name,'w+')
    print("Fill {} file in the format \n {}".format(f_name,json.dumps({"S1":{"Hash":"[ ]","Name":"Song Name","URL":"URL from Youtube","Format":".m4a","cover":"{path_to_cover_picture}"}},indent=4)))
    url_list.write(json.dumps({"S1":{"Hash":"[ ]/[#]","Name":"Song Name","URL":"URL from Youtube","Format":".m4a","cover":"{path_to_cover_picture}"}},indent=4))
    url_list.close()
    console_out("\nOpened & Closed file {}".format(f_name))
    

def download_link(link,file_name,name=''):

    if len(file_name) > 1 :                 # check if file is given
        file_name = files["default"]
    else:
        file_name = file_name[0]

    dir_manage(file_name[1])                 # Change directory
    
    if link[:23]=="https://www.youtube.com":
        if arg.over_ride_format and arg.over_ride_format!="m4a":
            print("USING GENERIC")
            dynamic_cmd=cmd_generic[:]
        else:
            print("Using YOUTUBE")
            dynamic_cmd=cmd_youtube[:]
    else:
        print("USING GENERIC")
        dynamic_cmd=cmd_generic[:]
    
    dynamic_cmd.append(link)                 # Adding link
    
    if name :                                # Fixing file name
        dynamic_cmd.append("-o")
        dynamic_cmd.append(name+ "."+str(arg.over_ride_format or "m4a"))
    else:
         print("NOTE: Using file name from URL\n")
    
    try:                                        # Download code
        subprocess.run(dynamic_cmd,check=True,timeout=set_timeout)
        console_out("\nDOWNLOADED LINK ------{}\n".format(time.ctime(time.time()))) # If download completes open the file in append mode
        
       
        if file_name[1]=="..":
            chdir(getcwd()+"/Muzic_Manager")           # chdir(getcwd()+"/DEV_DIR") chdir(getcwd()+"/Downloader")
        else:            
            chdir("../Muzic_Manager")                  # chdir("../DEV_DIR") chdir("../Downloader")
        
        try:
            with open(file_name[0],"r") as f:
                song_collection = json.load(f)
        except:
            Exception_error(file_name[0])
            with open(file_name[0],"r") as f:
                song_collection = json.load(f)
        
        keys=list(song_collection)
        new_key=str(int(keys[-1][1:])+1)
        letter=keys[-1][0]
        
        song_collection[letter+new_key]={}
        song_collection[letter+new_key]["Hash"]="[#]"
        song_collection[letter+new_key]["Name"]=name
        song_collection[letter+new_key]["URL"]=link
        song_collection[letter+new_key]["Cover"]=""
        song_collection[letter+new_key]["Format"]=str(arg.over_ride_format or "m4a")
        song_collection[letter+new_key]["Modified"]=time.ctime(time.time())
    
        song_data = open(file_name[0],"w+")
        song_data.write(json.dumps(song_collection,indent=4))
        song_data.close()

    except subprocess.CalledProcessError:
        console_out("\nERROR DOWNLOADING LINK ------{}\n".format(time.ctime(time.time())))    # else dont write to the file
    
    except subprocess.TimeoutExpired :
        print("PROCESS TOOK LONGER THAN EXPECTED")    
    return 0

######################### MAIN PROGRAM ############################################

if __name__=='__main__':                            # Starting of the program --- Opening the requird file
    
    try:
        intro()

        if arg.link :

            print("given name ",arg.name)
            download_link(arg.link,arg.file_name,arg.name)

        else :
            for current in arg.file_name:
                skip=False
                try:
                    with open(current[0],"r") as f:
                        song_collection = json.load(f) 
                    console_out("\nOpened file {}".format(current[0]))

                except:
                    Exception_error(current[0])
                    skip=True

                dir_manage(current[1])                          # Changing directory

                if skip :
                    if current[1]=="..":
                        chdir(getcwd()+"/Muzic_Manager")   # chdir(getcwd()+"/DEV_DIR") chdir(getcwd()+"/Downloader")
                    else:
                        chdir("../Muzic_Manager")  # chdir("../DEV_DIR") chdir("../Downloader")

                # Looking for title from the files
                if not skip:
                
                    for key in song_collection:

                        if arg.over_ride:                               # Over-ride changing Hash
                            song_collection[key]["Hash"]="[ ]"
                        
                        if not arg.destination:
                            if arg.over_ride_format:                        # Over-ride-format by changing Format
                                song_collection[key]["Format"]=arg.over_ride_format

                        if song_collection[key]["Hash"]!="[#]":

                            if song_collection[key]["URL"][:23]=="https://www.youtube.com":
                                
                                if arg.over_ride_format and arg.over_ride_format!="m4a":
                                    print("USING GENERIC")
                                    dynamic_cmd=cmd_generic[:]
                                else:
                                    print("Using YOUTUBE")
                                    dynamic_cmd=cmd_youtube[:]            
                            else:
                                print("USING GENERIC")
                                dynamic_cmd=cmd_generic[:]    

                            if song_collection[key]["URL"]:
                                dynamic_cmd.append(song_collection[key]["URL"].strip())
                            if song_collection[key]["Name"]:
                                if song_collection[key]["Name"]!="":
                                    dynamic_cmd.append("-o")
                                    dynamic_cmd.append(song_collection[key]["Name"]+"."+song_collection[key]["Format"])
                                else:
                                    print("NOTE: Using file name from URL\n")
                            else:
                                print("NOTE: Using file name from URL\n")

                            try:               
                                subprocess.run(dynamic_cmd,check=True,timeout=set_timeout)
                                console_out("\nDOWNLOADED SONG {}------{}\n".format(key,time.ctime(time.time())))
                                song_collection[key]["Hash"]="[#]"
                                song_collection[key]["Cover"]=""
                                #ong_collection[key]["Format"]="m4a"
                                
                                if arg.over_ride:
                                    song_collection[key]["Over-ride"]=time.ctime(time.time())
                                else:
                                    song_collection[key]["Modified"]=time.ctime(time.time())
                            
                            # Download process underway
                            except subprocess.CalledProcessError:
                                console_out("ERROR DOWNLOADING SONG {}------{}\n".format(key,time.ctime(time.time())))
                                song_collection[key]["Hash"]="[ ]"

                            # If error occurs the log file is updated and the program moves on....    
                        else:
                            print("SKIPPING THROUGH {}".format(key),end="\r")

                        # If the link has already been downloaded then the program skips those links
                    console_out("\nClosed file {}".format(current[0]))

                    if current[1]=="..":
                        chdir(getcwd()+"/Muzic_Manager")   # chdir(getcwd()+"/DEV_DIR") chdir(getcwd()+"/Downloader")
                    else:
                        chdir("../Muzic_Manager")  # chdir("../DEV_DIR") chdir("../Downloader")
                    
                    song_data = open(current[0],"w+")
                    song_data.write(json.dumps(song_collection,indent=4))
                    song_data.close()

        log.write("\n--------------------------------------")
        log.close()

    except KeyboardInterrupt:
        print("Ooops......Interrupted")
        print("NOTE: There might be partially downloaded files")
        print("NOTE: The details of present download might not be recorded")
        log.write("\nOoops......Interrupted\nNOTE: There might be partially downloaded files\nNOTE: The details of present download might not be recorded")
        log.write("\n--------------------------------------")
        log.close()
####################################### END ############################################