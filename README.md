Track your CD's DVD's, recordable or store baught, this will create md5 chcksum of a rom and store the data in a flat file for later access. simply drop the ROM in your tray and start the program to begin the scan. first it finds the label and compairs it to the archive, so your leabels should be unique other wise you will need to append a number after each additional like labels.



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
if the disk is not found you will be asked for an index number, then all data gathered is added to the archive at the end of the file.

you can add prefix's to your index number to track multiple collections if you like, M001 or AUDIO01 but for now it does not check if used allready or not.
