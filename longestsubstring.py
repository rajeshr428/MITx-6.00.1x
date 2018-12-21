long_substring=""
strptr=0
newstr=""
strlen=len(s)
for char in s:
    ptr=strptr
    newstr=s[ptr]
    while ((ord(s[ptr]) - ord(s[ptr+1]) <=0 ) and ptr < strlen - 2):
           newstr += s[ptr+1]
           ptr += 1
    if ((ptr == strlen -2) and (ord(newstr[-1]) - ord(s[-1]) < 0)):
            newstr += s[-1]
    if len(newstr) > len(long_substring):
        long_substring = newstr
    if (strptr < strlen -2):
        strptr += 1
print ("Longest substring in alphabetical order is:" + long_substring)
