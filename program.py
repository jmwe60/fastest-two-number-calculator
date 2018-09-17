import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)

int sum=int(lines[0]) + int(lines[1])

print(sum)
return 0
