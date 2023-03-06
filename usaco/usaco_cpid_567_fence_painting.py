import sys

sys.stdin = open('paint.in', 'r')
sys.stdout = open('paint.out','w')

painted = [list(map(int,input().split())) for i in range(2)]
print(((painted[0][1]-painted[0][0])+(painted[1][1]-painted[1][0]))-max(min(painted[0][1],painted[1][1])-max(painted[0][0],painted[1][0]),0))
