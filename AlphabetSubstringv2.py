s = 'azcbobobegghakl'

dummy = final = s[0] #a

for i in range(1, len(s)): 			#return number 1-14
    if s[i] >= dummy[-1]:  			#for each letter greater than or equal to first letter
        dummy += s[i]				#
        if len(dummy) > len(final):
            final = dummy
    else:
        dummy = s[i]

print 'Longest substring in alphabetical order is:', final
