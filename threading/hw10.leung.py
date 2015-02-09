#IP Address: 10.142.186.7
import subprocess
import time

def main():
	IP_address = raw_input("My IP address is: ")
	starttime = time.clock()
	ping_check(IP_address)
	finishtime = time.clock()
	print "Elapsed time is ", (finishtime - starttime)

def ping_check(IP_address):
	for i in range (0, 256):
		IP_split = IP_address.split('.')
		IP_split[3] = i
		IP_address_test = ".".join(map(str,IP_split))
		print IP_address_test
		returncode = subprocess.call(['ping','-c','2',IP_address_test])
		if returncode == 0: 
			print 'IP Address',IP_address_test,' is reachable.'
		else:
			print 'IP Address',IP_address_test,' is unreachable.'

if __name__ == "__main__":
	main()

#ask user what IP address is. 
#loop through pings from 0-250
#find way to suppress the other output
#store in list whether successful or not

#bonus: figure out what user's IP address is

#part (7) - convert script to be threaded version. Each IP address will be different thread (i.e. returncode1, returncode2, returncode3, etc.)
#max length you are waiting is the max time that one of thing will take (the longest one)
#kick off bunch of threads, wait until they're done, and wait for results.
#doug posted .rar file

