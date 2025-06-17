Create a simple alias to run this script from the command line.
alias chkcdrom='python3 /location/to/trkcdrom/trkcdrom.py'

now when you add or create new media just run the command chkcdrom in your terminal to begin the scan.

this program will create a txt file that is in a comma seperated value format and will store all your rom data there.

the data collected from the roms for loggin include

Disk ID
Disk Label
Disk Size
generates Disk md5sum
generates short uid for the rom based off the md5sum
time stamp

if the disk is in the archive allready it will display disc data along with a current md5sum scan for comparrison.

if the disk is not found you will be asked for an index number, (can be any lenth alpha numaric as you please.) then all data gathered is added to the archive at the end of the file.
