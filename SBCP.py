import argparse
import sys
import os
import platform
from chromagnon import cacheParse 

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", type=str,
                    help="Do not autodetect Steam path and force it to specific path")
args = parser.parse_args()

def printCache(cache):
	for item in cache: 
		aux = str(item)
		item = aux[0:aux.index('Creation Time')] + '''\n''' +  aux[aux.index('Creation Time'):aux.index('Key:')]  + '''\n''' +aux[aux.index('Key:'):]
	print(item)

def extractCache(path):
	try:
		print(path)
		cache = cacheParse.parse(path)
		return cache
	except:	
		print("Path error or empty")
		exit()

def main():
    print("Welcome to the Steam browser cache parser")
    if(args.path != None):
		cache = extractCache(args.path)
		printCache(cache)
    else:
		currentos = platform.system()
		if currentos == "Linux" or currentos == "linux2":
			#untested#
			cachePath = os.path.expanduser('~')+"/.steam/config/htmlcache/Cache"
                        cache = extractCache(cachePath)
			printCache(cache)
		elif currentos == "darwin":
			print("TODO")
   		# TODO: MAC OS X
		elif currentos == "win32":
			cachePath = "C:\Users\\" + os.getlogin() + "\AppData\Local\Steam\htmlcache\Cache"
			printCache(cache)

main()
