#Example IP Address: 10.0.0.20
#Note: part of code comes from example code provided in class
#Suppression of ping statistics is from: http://stackoverflow.com/questions/4996852/how-to-just-call-a-command-and-not-get-its-output
import subprocess
import time

def main():
	#ask user what IP address is. 
	IP_address = raw_input("My IP address is: ")
	#write to file
	with open('HW10.script.leung.txt', 'w') as fo:
		fo.write('**Unthreaded Script Results**\n')
		fo.write('My IP address is: '+IP_address+'\n')

	#Time your program and see how long it takes to execute
	starttime = time.time()
	ping_check(IP_address)
	finishtime = time.time()
	elapsed = str(finishtime-starttime)
	with open('HW10.script.leung.txt', 'a') as fo:
		fo.write("Elapsed time is "+elapsed+' secs\n')

def ping_check(IP_address):
	#loop through pings from 0-255
	for i in range (0, 256):
		IP_split = IP_address.split('.')
		IP_split[3] = i
		IP_address_test = ".".join(map(str,IP_split))
		#get return code 1 or 0 to see whether ping worked or not; suppress other output
		returncode = subprocess.call(['ping','-c','2',IP_address_test],stdout=subprocess.PIPE)
		#Print the results in sorted order
		with open('HW10.script.leung.txt', 'a') as fo:
			if returncode == 0: 
				fo.write('IP Address'+IP_address_test+' is reachable.\n')
			else:
				fo.write('IP Address'+IP_address_test+' is unreachable.\n')

if __name__ == "__main__":
	main()








