#Python program to illsutrate main function
#main function
'''As we know any program starts from 'main' function...
lets create a main function like in many other programming languages'''

def getInteger():
    result=int(input("Enter Integer:"))
    return result

def Main():
    print("Main function Started...")
    
    #Calling the getInteger function and 
    #storing its returned value in the output variable
    
    output=getInteger()
    print(output)
    
#Now we are required to tell Python
#for 'Main' function existence 

if __name__ == "__main__":
    Main()
