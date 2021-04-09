import os
import sys
while 1:
    i = input("$")
    params = i.split()
    if params[0] == "cd":
	os.chdir(params[1])
    else:
	newpid = os.fork()
    	if newpid == 0:
        print("I am the child process")
        #exit()
        os.execvp(params[0],params)
    	else:
		print("I am the parent process")
        	print("The child process id is",newpid)
        	os.wait()
