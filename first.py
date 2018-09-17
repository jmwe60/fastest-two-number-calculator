import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)

int sum=lines[0]+lines[1]

print(sum)
    
