#merge two sorted arrays 
#arr1[0..n1-1] and 
#arr2[0..n2-1] into 
#arr3[0..n1+n2-1]

def mergeArrays(arr1,arr2,n1,n2):
    arr3=[None]*(n1+n2)
    i=0
    j=0
    k=0
    
    #Traverse both the array and compare the first value of both and store the values to arr3 accordingly
    
    while i<n1 and j<2:
        if arr1[i]<arr2[j]:
            arr3[k]=arr1[i]
            k=k+1
            i=i+1
        else:
            arr3[k]=arr2[j]
            k=k+1
            j=j+1
            
    #storing remaining elements of first array 
    while i<n1:
        arr3[k]=arr1[i]
        k=k+1
        i=i+1
        
    #storing remaining elements of second array 
    while j<n2:
        arr3[k]=arr2[j]
        k=k+1
        j=j+1
        
    #printing the array after merge
    print('Array after merge')
    for i in range(n1+n2):
        print(str(arr3[i]),end='')
        
#Defining array to run this code 
arr1=[11,23,25,37]
print('Here is the first array',arr1)
n1=len(arr1)
print('Lenght of the first array',n1)

arr2=[19,24,56,88]
print('Here is the second array',arr2)
n2=len(arr2)
print('Length of the second array',n2)

#calling the mergearray function
mergeArrays(arr1,arr2,n1,n2)
