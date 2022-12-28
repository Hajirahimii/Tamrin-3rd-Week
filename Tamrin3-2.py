# Hamid HajiRahimi
# Tamrin: 3-2
# Print Checkboard (n,m)

############################################################

#def printcheckboard(n,m):   
Rows=int(input("Number of Rows: "))
Coloumns=int(input("Number of Columns: " ))  
T=1
for i in range(1,Rows+1):
    for j in range(1,Coloumns+1):
        if T==1:
            print("*", end="")
        else:
            print("#", end="")
        T=-T
    if i*j % 2 == 0: 
        T=-T
    print()            

#printcheckboard(n,m)
