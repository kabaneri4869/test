n=int(input("Enter the code word: "))
print("The code word entered by the user is: ",n)
parity=0
while(n!=0):
	if((n&1)==1):
		parity^=1
		n>>=1
		print("Parity of the number is: ",parity)
