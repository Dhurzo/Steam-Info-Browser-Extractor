import argparse
import sys
import glob
import os
import platform

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", type=str,
                    help="Do not autodetect Steam path and force it to specific path")
args = parser.parse_args()

def main():
    print("Welcome to the Steam browser local storage extractor")
    if(args.path != None):
        fileList = glob.glob(args.path+"/*")
        for fich in fileList:
            print(fich + "\n")
            F = open(fich,"r")
            print(F.read())
            print("\n\n")
    else:
        currentos = platform.system()
        print("Detecting OS and Steam path...." + str(currentos))
        if currentos == "Linux" or currentos == "linux2":
            fileList = glob.glob(os.path.expanduser('~')+"/.steam/config/htmlcache/Local Storage/*")
            for fich in fileList:
                print(fich + "\n")
                F = open(fich,"r")
                print(F.read())
                print("\n\n")
        elif currentos == "darwin":
            print("TODO")
        # TODO: MAC OS X
        elif currentos == "win32":
            #untested#
            localPath = "C:\Users\\"+ os.getlogin() + "\AppData\Local\Steam\htmlcache\Local Storage" #This is codecrap :D
            fileList = glob.glob(localPath)
            for fich in fileList:
                print(fich + "\n")
                F = open(fich,"r")
                print(F.read())
                print("\n\n")
        
main()