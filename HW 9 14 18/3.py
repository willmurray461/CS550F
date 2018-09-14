import sys
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])
answer = (d +(13*(m+1)/5) + (y%100) + (y/4) + (y/100/4) - 2*(y/100))%7
print(str(answer))