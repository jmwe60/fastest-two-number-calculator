import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)

sum=lines[0]+lines[1]
#print result
print(sum)
    
#!/bin/sh
python3 first.py
