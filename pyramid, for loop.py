n=int(input("Enter the number of rows:"))  
k = 1*n-2  
for i in range(0,n):  
    for j in range(0, k+1):  
        print(end=" ")  
    k=k-1 
    for j in range(0,i+1):  
        print("* ",end="") 
    print("")
