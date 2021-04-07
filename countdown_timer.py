#countdown timer

import time
counter=10

for i in reversed(range(counter+1)):
	if i>0:
		print(i,end='')
		time.sleep(1)
	else:	
		print('Started')


