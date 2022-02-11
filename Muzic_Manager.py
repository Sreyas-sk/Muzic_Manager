########################################################
# Muzic Manager
# Current Version : 3.4.0 
# Description: Shifting from CSV to JSON
# Author : Sreyas S
########################################################
from importlib.resources import path
import subprocess
import time
from os import chdir,listdir,mkdir,getcwd,replace,rmdir
import argparse
import json
######################### PRIMARY SETTING ##############################################
cmd_generic=["youtube-dl","-x","--audio-quality", "0","--audio-format","m4a"] #Download command
cmd_youtube=["youtube-dl","-f","140","--audio-format","m4a"] #Download command
root = getcwd()

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
parser.add_argument("--destination",help="To download songs to new location")
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
    print("# Current Version : 3.4.0")     
    print("########################################################")
    return 0

def console_out(line_out,line_log=log):
    print(line_out)
    if line_log!=None:
        line_log.write("\n"+line_out)
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
    
    console_out("Download file not found or Error in JSON format")
    console_out("Creating file "+str(f_name))
    url_list=open(f_name,'w+')
    print("Fill {} file in the format \n {}".format(f_name,json.dumps({"S1":{"Hash":"[ ]","Name":"Song Name","URL":"URL from Youtube","Format":"m4a","cover":"{path_to_cover_picture}"}},indent=4)))
    url_list.write(json.dumps({"S1":{"Hash":"[ ]","Name":"Song Name","URL":"URL from Youtube","Format":"m4a","cover":"{path_to_cover_picture}"}},indent=4))
    url_list.close()
    console_out("\nOpened & Closed file {}".format(f_name))
    

def download_link(link,file_name,name=''):

    if len(file_name) > 1 :                 # check if file is given
        file_name = files["default"]
    else:
        file_name = file_name[0]

    if arg.destination:
        switch_to_destination(arg.destination)
    else:
        dir_manage(file_name[1])                 # Change directory
    
    dynamic_cmd=command_selection(link[:23],str(arg.over_ride_format or "m4a")) # CMD Selection
    
    #print(dynamic_cmd) # @Debug
    
    dynamic_cmd.append(link)                 # Adding link
    
    if name :                                # Fixing file name
        dynamic_cmd.append("-o")
        dynamic_cmd.append(name+ "."+str(arg.over_ride_format or "m4a"))
    else:
         print("NOTE: Using file name from URL\n")
    
    try:                                        # Download code
        subprocess.run(dynamic_cmd,check=True,timeout=set_timeout)
        console_out("\nDOWNLOADED LINK ------{}\n".format(time.ctime(time.time()))) # If download completes open the file in append mode
        
        switch_folder_back() # Changing Folder to Muzic_Manager
        
        if arg.destination:
            console_out("Destination: {}",format(arg.destination))
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
    
        if not arg.destination:
            update_json(file_name[0], song_collection) # Updating info in json file

    except subprocess.CalledProcessError:
        console_out("\nERROR DOWNLOADING LINK ------{}\n".format(time.ctime(time.time())))    # else dont write to the file
    
    except subprocess.TimeoutExpired :
        console_out("PROCESS TOOK LONGER THAN EXPECTED")    
    return 0



def command_selection(URL,format):
    #print(format) @debug
    if URL=="https://www.youtube.com":
    
        if arg.over_ride_format and arg.over_ride_format!="m4a":
            console_out("USING GENERIC")
            cmd_generic[5]=format
            return cmd_generic[:]
            
        else:
            if format and format!="m4a":
                console_out("USING GENERIC")
                cmd_generic[5]=format
                return cmd_generic[:]
            else:
                console_out("Using YOUTUBE")
                return cmd_youtube[:] 
    else:
        console_out("USING GENERIC")
        cmd_generic[5]=format
        return cmd_generic[:]


def switch_folder_back():
    chdir(root)

def update_json(file_name,song_collection):
    console_out("Updating json")
    song_data = open(file_name,"w+")
    song_data.write(json.dumps(song_collection,indent=4))
    song_data.close()

def Error_log_msg():
    console_out("Ooops......Interrupted")
    console_out("NOTE: There might be partially downloaded files")
    console_out("NOTE: The details of present download might not be recorded")
    log.write("\n--------------------------------------")
    log.close()

def switch_to_destination(dest):
    try:
        chdir(dest)
    except:
        console_out("Destination not valid")
        #print("@@@"+getcwd()) # @Debug
        try:
            console_out("Trying to create {}".format(dest))
            mkdir(dest)
            console_out("Successfully created {}".format(dest))
            chdir(dest)
            console_out("Successfully switched to {}".format(dest))
        except:
            console_out("Error creating {}".format(dest))
            console_out("Creating folder 'Downloads'")
            mkdir("../Downloads")
            chdir("../Downloads")
    return 0

######################### MAIN PROGRAM ############################################

if __name__=='__main__':                            # Starting of the program --- Opening the requird file
    
    try:
        intro()

        if arg.link :

            console_out("given name: ",str(arg.name or "None"))
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

                if arg.destination:
                    switch_to_destination(arg.destination)
                else:
                    dir_manage(current[1])                          # Changing directory

                #print(getcwd()) # @Debug
                
                if skip :
                    
                    switch_folder_back()

                # Looking for title from the files
                #if not skip:
                else:
                    if arg.over_ride:
                        mkdir("Temp")
                        chdir("Temp")
                    
                    for key in song_collection:

                        if not arg.destination and arg.over_ride_format:
                            #if arg.over_ride_format:                        # Over-ride-format by changing Format
                            song_collection[key]["Format"]=arg.over_ride_format
                            console_out("Updating format in json")
                        
                        if song_collection[key]["Hash"]!="[#]" or arg.over_ride:

                            dynamic_cmd=command_selection(song_collection[key]["URL"][:23],(arg.over_ride_format if arg.over_ride_format else song_collection[key]["Format"])) # CMD Selection
                            
                            #print(dynamic_cmd) # @Debug

                            try:
                                if song_collection[key]["URL"]:
                                    dynamic_cmd.append(song_collection[key]["URL"].strip())
                            except:
                                console_out("Song URL not Found")
                            
                            #print(dynamic_cmd) # @Debug

                            if song_collection[key]["Name"]!="":
                                dynamic_cmd.append("-o")
                                dynamic_cmd.append(song_collection[key]["Name"]+"."+(arg.over_ride_format if arg.over_ride_format else str(song_collection[key]["Format"] or "m4a")))
                            else:
                                print("NOTE: Using file name from URL\n")

                            try:               
                                #print(dynamic_cmd) # @Debug
                                subprocess.run(dynamic_cmd,check=True,timeout=set_timeout)
                                console_out("\nDOWNLOADED SONG {}------{}\n".format(key,time.ctime(time.time())))
                                song_collection[key]["Hash"]="[#]"
                                
                                if arg.over_ride:
                                    song_collection[key]["Over-ride"]=time.ctime(time.time())
                                else:
                                    song_collection[key]["Modified"]=time.ctime(time.time())

                            # Download process underway
                            except subprocess.CalledProcessError:
                                console_out("ERROR DOWNLOADING SONG {}------{}\n".format(key,time.ctime(time.time())))
                                
                                if arg.over_ride:
                                    console_out("Error downloading while over-ride song {}".format(key))
                                elif arg.destination:
                                    console_out("Error downloading to destination song {}".format(key))
                                else:
                                    song_collection[key]["Hash"]="[ ]"
                            # If error occurs the log file is updated and the program moves on....    
                        else:
                            print("SKIPPING THROUGH {}".format(key),end="\r")

                        # If the link has already been downloaded then the program skips those links
                    console_out("\nClosed file {}".format(current[0]))
                    
                    if arg.over_ride:
                        #temp=str(song_collection[key]["Name"]+"."+(arg.over_ride_format if arg.over_ride_format else str(song_collection[key]["Format"] or "m4a")))
                        flag=0
                        for temp in listdir(path="."):
                            try:
                                replace(temp,str("../"+temp)) # @Debug - Check when file doesnt exist
                            except:
                                print("Unable to replace file {}".format(temp))
                                flag=1

                        if flag!=1:
                            chdir("../")
                            rmdir("Temp")
                        else:
                            console_out("Some files could not be replaced...they are in Temp Folder")

                    switch_folder_back() # Changing Folder to Muzic_Manager
                    
                    update_json(current[0],song_collection) # Updating info in json file

        log.write("\n--------------------------------------")
        log.close()

    except KeyboardInterrupt:
        Error_log_msg()
####################################### END ############################################