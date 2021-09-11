import sys

math_expression = sys.stdin.readline().split('-')

snum = 0 
for num in math_expression[0].split('+') :
    snum += int(num)

mnum = 0
for i in range(1, len(math_expression)) :
    for num in math_expression[i].split('+') :
        mnum += int(num)

print(snum - mnum)
