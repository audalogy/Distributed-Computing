#IP Address: 10.0.0.20
#Note: part of code comes from example code provided in class
#Suppression of ping statistics is from: http://stackoverflow.com/questions/4996852/how-to-just-call-a-command-and-not-get-its-output
import subprocess
import threading
import time

def main():
	IP_address = raw_input("My IP address is: ")
	with open('HW10.script.leung.txt', 'a') as fo:
		fo.write('\n**Threaded Script Results**\n')
		fo.write('My IP address is: '+IP_address+'\n')
	threads = []  # create empty list of threads
	# generate list of threads and initialize threads
	thread_gen(IP_address,threads)
	# start timer
	starttime = time.time()
	# start each thread
	print 'Starting threads...\n'
	for thread in threads:
		thread.start()
	# wait for threads to terminate
	for thread in threads:
		thread.join()
	# stop timer
	finishtime = time.time()
	elapsed = str(finishtime-starttime)
	with open('HW10.script.leung.txt', 'a') as fo:
		fo.write("Elapsed time is "+elapsed+' secs')

class PrintThread( threading.Thread ):
	"""Subclass of threading.Thread"""

	def __init__( self, threadName ):
		# Initialize thread
		threading.Thread.__init__( self, name = threadName )
		# print "Thread: %s" % self.getName()

	# overridden Thread run method
	def run( self ):
		#Ping!
		returncode = subprocess.call(['ping','-c','2',self.getName()],stdout=subprocess.PIPE)
		#print IP_address_test
		with open('HW10.script.leung.txt', 'a') as fo:
			if returncode == 0: 
				fo.write('IP Address %s is reachable.\n' % self.getName())
			else:
				fo.write('IP Address %s is unreachable.\n' % self.getName())

def thread_gen(IP_address,threads):
	#generate list of threads from 0-255
	for i in range(0, 256):
		IP_split = IP_address.split('.')
		IP_split[3] = i
		IP_address_test = ".".join(map(str,IP_split))
		#append threads to list
		threads.append(IP_address_test)
		#initialize thread using class PrintThread
		threads[i] = PrintThread(IP_address_test)
	
if __name__ == "__main__":
	main()

