"""This script updates the files if a new version is avaialbe at specified web address"""
"""Jacob Lee @ 2019"""
from urllib.request import urlopen, urlretrieve, URLError
import config
import zipfile
import os




def check_internet():
	#check for internet connectivity
	try:
		urlopen("https://www.google.com/")
	except (URLError):
		print("No interent! Connect to update!")
		cont()
		return False
	else:
		return True


def update():
	versionData=[]

 	#Check version file against config version
	#Attempt download of new files from url provided in version file
	try:
		for line in urlopen(config.UPDATE_URL): #read from version url
			versionData.append(line.decode('utf-8'))
	except:
		print("FAILED, Bad URL!")
		cont()

	try:
		updateVersion = versionData[0][:-1]
		updateUrl = versionData[1]
		updateFile = versionData[1].split("/")[-1:][0]

		if float(updateVersion) > config.VERSION: #compare versions
			print("Update Found! Downloading Version:", updateVersion)
			urlretrieve (updateUrl, updateFile) #download file
			print("Download Complete!")
			installUpdate(updateFile)
		else:
			print("Already Running Newest Version:", config.VERSION)
	except:
		print("Download FAILED!")
		cont()



def installUpdate(file):
	#unzip file downloaded
	try:	
		print("Installing...")
		with zipfile.ZipFile(file) as zf:
			for member in zf.infolist():
				if member.filename[-1] == '/': continue
				with open(os.path.basename(member.filename), "w") as outfile:
					outfile.write(zf.read(member).decode('utf-8'))
	

		print("Install Complete!")

		import run #start new run file

	except:
		print("Something Went Wrong!")
		cont()


def cont():
	print("launching old version!")
	import run


	




if check_internet():
	print("Checking for Update...")
	update()





