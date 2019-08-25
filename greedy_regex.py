import re
x = "From: Using the : Character"
y_gdy = re.findall('^F.+:',x ) #Greedy regex
y_n_gdy = re.findall('^F.+?:',x) #Non greedy because of ?
print(y_gdy)
print(y_n_gdy)
