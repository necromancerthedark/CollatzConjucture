#pylint:disable=C0103
#pylint:disable=C0103
#pylint:disable=W0312
count= 0

'''def oddeven(n):
	if n%2 ==0:
		return 1
	elif n%2 == 1:
		return 0'''

n = int(input("Enter A number:"))



while n!=1:
	#a = int(oddeven(n))
	if n%2==0:
		n=n/2
	elif n%2==1:
		n=3*n +1
	count = count+1
	print (int(n))

print("No. of steps Taken",count)
b=input()


