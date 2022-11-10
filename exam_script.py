import sys

print(sys.argv)
print(sys.argv[0])

sum = 0

for i in range(3, len(sys.argv)):
	sum += float(sys.argv[i])
print("The total for {} {} is {}".format(sys.argv[1],sys.argv[2], sum))