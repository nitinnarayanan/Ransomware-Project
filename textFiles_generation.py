print("How many text files do you need ?: ")
n=int(input())


for i in range(n):
	file = open("file-%d.txt"%(i+1),"w")
	file.write("%d is the is FILE NUMBER\n"%(i+1))
	file.write("UniqueID = %d"%(i+1))
	file.close()
	

print("\n%d UNIQUE TEXT FILES GENERATED SUCCESSFULLY..!!"%(i+1))

