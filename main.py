def getNumber():
    print('getNumber function started...')
    num=input('enter your fav number:')
    return num

def Main():
    print('Main function started...')
    print('Calling getNumber function')
    output=getNumber()
    print('Above is the output of getNumber function.')
    
if __name__=='__main__':
    Main()
