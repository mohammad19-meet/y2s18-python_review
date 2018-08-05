# Write your solution for 1.4 here!
x = input("nn")
def is_prime(x):
	for i in range(2,int(x/2)):
		if int(x) % i == 0:
			print("notprime")
			#x = input("number?")
		else: print("it's prime")

is_prime(x)