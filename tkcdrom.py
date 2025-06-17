#!/usr/bin/python3
# CD-ROM scanning too to create md5sum > SUID. With checking and logging of entries

import hashlib
import shortuuid
import time
import os
import subprocess
import csv


file_path = os.path.realpath(__file__)
file_dir = os.path.dirname(__file__)
archive = "/disco.txt"


def makerommd5():
	p = 0
	t = 0
	md5_hash = hashlib.md5()
	with open('/dev/cdrom',"rb") as f:
		# Read and update hash in chunks of 4K
		print('Starting md5.....')
		for byte_block in iter(lambda: f.read(4096),b""):
			t=t+1
			p=p+1
			if p >= 114474:
				report = int(t/114474)
				p = 0
				dreport = str(report)+"0%           "
				print(dreport, end='\r')

			md5_hash.update(byte_block)
			out = md5_hash.hexdigest()
		print('Finished.....')
	return out

def makesuid(md5):
	udid = shortuuid.uuid(md5)
	return udid

def opentray():
	os.system("eject -rF /dev/sr0")

def closetray():
	os.system("eject -t /dev/cdrom")

def getromlabel():
	label = subprocess.check_output("blkid -o value -s LABEL /dev/sr0", shell=True, text=True).strip()
	return label

def getromuuid():
	duuid = subprocess.check_output("blkid -o value -s UUID /dev/sr0", shell=True, text=True).strip()
	return duuid

def getromsize():
	size = subprocess.check_output("df -h --output=used /dev/sr0", shell=True, text=True).strip()
	used = size.strip('Used \n ')
	return used

def clearterm():
	command = 'cls' if os.name == 'nt' else 'clear'
	os.system(command)

def search_archive(string):
    with open(file_dir+archive, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            for j, column in enumerate(row):
                if string in column:
                    return row
    return "0"

def writelog(rlabel,rsize,rid, rmd,rsid):
	writelog = input("Write To Log? y/n Enter=y ")
	if writelog == "N" or writelog == "n":
		quit()
	getindex = input("Enter 4 digit index#: ")
	ts = time.strftime('%Y%m%d%H%M')
	trak = str(getindex)+","+rlabel+","+rsize+","+rid+","+rmd+","+rsid+","+ts+"\n"
	with open(file_dir+archive, "a") as f:
		f.write(str(trak))
	print('Added '+getindex+" "+romlabel+' to log file.\n')

if not os.path.exists(file_dir+archive):
    os.mknod(file_dir+archive)

clearterm()
closetray()
romlabel = getromlabel()
print("ROM Label: "+romlabel)
print("Searching Archive ....", end='\r')
analyse = search_archive(romlabel) # Search for ROM

try:
	# ROM found do analysis and append to archive line
	if analyse[3] >= "0":
		print("ROM Found in Archive....")
		print("\n-----Archive Data-----")
		print("INDEX: "+analyse[0])
		print("Label: "+analyse[1])
		print("Size: "+analyse[2])
		print("ID: "+analyse[3])
		print("SUID: "+analyse[5])
		print("Stamp: "+analyse[6])
		archive_md5 = analyse[4]
		dmd5 = makerommd5()
		print("Archive md5sum: "+archive_md5)
		print("CD-ROM md5sum : "+dmd5)
		opentray()

except:
	# do scann and add to archive
	print("ROM Not Found In Archive ....")
	print("Scanning New ROM ....", end='\r')
	romuuid = getromuuid()
	romsize = getromsize()
	dmd5 = makerommd5()
	romsuid = makesuid(dmd5)
	writelog(romlabel,romsize,romuuid,dmd5,romsuid)
	opentray()