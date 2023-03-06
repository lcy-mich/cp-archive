from sys import stdin, stdout

num_of_tests = int(stdin.readline())

def digitSum(x,y):
    x_sum = 0
    y_sum = 0
    for digit in x:
        x_sum += digit
    for digit in y:
        y_sum += digit
    return x_sum+y_sum

while num_of_tests:
    num_of_tests -= 1
    test = int(stdin.readline())

    
