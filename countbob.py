found=0
cnt=0
for char in s:
    if (char == 'b'):
        if (s[cnt:cnt+3] == 'bob'):
            found += 1
    cnt += 1
print ("Number of times bob occurs is:" + str(found))
