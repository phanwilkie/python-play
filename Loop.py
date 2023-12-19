"""
print 'Hello!'

num = 10
while num >= 2:
    print num
    num -= 2

while num <= 10:
    print num
    num += 2
"""


#Write a while loop that sums the values 1 through end
#if we define end to be 6, your code should print out the result 21
#which is 1 + 2 + 3 + 4 + 5 + 6.
end = 10

#total of 0 to add end to
total = 0

#check to see whether end is down to 0, if not add end to total
while end > 0:
	total += end
	end -= 1

print total




# Here is one of a few ways to solve this problem:
total = 0
current = 1
while current <= end:
    total += current
    current += 1

print total



