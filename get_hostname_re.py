data = 'From test@gmail.com Sat blah blah'
atpos = data.find('@')
print(atpos)

space_pos = data.find(' ', atpos)
print(space_pos)

host = data[atpos+1 : space_pos]
print(host)


words = data.split()
print(words[1])
email = words[1]
host = email.split('@')
print(host[1])
